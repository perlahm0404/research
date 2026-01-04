#!/usr/bin/env python3
"""
Frontmatter validator for v3.0 compliance
Validates YAML frontmatter against v3.0 template requirements
"""

import sys
from pathlib import Path
from typing import Dict, List, Any

# Add scripts dir to path for imports
sys.path.insert(0, str(Path(__file__).parent))
from utils import extract_frontmatter


# v3.0 Required top-level fields
REQUIRED_V3_FIELDS = {
    'document_type',
    'state_abbr',
    'state_name',
    'tier',
    'license_type',
    'research_date',
    'version',
    'board_name',
    'board_website'
}

# v3.0 Required complex sections
REQUIRED_V3_SECTIONS = {
    'governance': ['framework', 'authority_level', 'primary_statute'],
    'soc2_compliance': ['scope', 'data_classification'],
    'iso_standards': ['applicable_standards'],
    'scope': ['included', 'excluded'],
    'tier_classification': ['tier_level', 'rationale'],
    'research_quality': ['completeness_percentage', 'validation_level'],
    'critical_gaps': None,  # Array, can be empty
    'high_gaps': None,  # Array, can be empty
    'medium_gaps': None  # Array, can be empty
}


def validate_frontmatter(file_path: str) -> Dict[str, Any]:
    """
    Validate v3.0 frontmatter compliance.

    Returns:
        {
            'valid': bool,
            'version': str,  # Detected version
            'errors': List[str],
            'warnings': List[str],
            'score': int,  # Max 25 points
            'details': Dict
        }
    """
    errors = []
    warnings = []
    details = {}

    # Read file
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {
            'valid': False,
            'version': 'unknown',
            'errors': [f'Failed to read file: {e}'],
            'warnings': [],
            'score': 0,
            'details': {}
        }

    # Extract frontmatter
    fm, body = extract_frontmatter(content)

    if fm is None:
        return {
            'valid': False,
            'version': 'none',
            'errors': ['No valid YAML frontmatter found'],
            'warnings': [],
            'score': 0,
            'details': {'has_frontmatter': False}
        }

    # Detect version
    version = fm.get('version', 'unknown')
    details['version'] = version
    details['has_frontmatter'] = True

    # Check if v3.0
    if version != '3.0' and version != 3.0:
        warnings.append(f'Document version is {version}, expected 3.0')

    # Check required top-level fields
    missing_fields = []
    for field in REQUIRED_V3_FIELDS:
        if field not in fm:
            missing_fields.append(field)
            errors.append(f'Missing required field: {field}')

    details['missing_fields'] = missing_fields
    details['present_fields'] = [f for f in REQUIRED_V3_FIELDS if f in fm]

    # Check required sections
    missing_sections = []
    incomplete_sections = []

    for section, required_subfields in REQUIRED_V3_SECTIONS.items():
        if section not in fm:
            missing_sections.append(section)
            errors.append(f'Missing required section: {section}')
            continue

        # Check if section is array (gaps) or dict
        if required_subfields is None:
            # Array sections (gaps) - must exist but can be empty
            if not isinstance(fm[section], list):
                errors.append(f'Section {section} must be an array')
        else:
            # Dict sections - check required subfields
            if not isinstance(fm[section], dict):
                errors.append(f'Section {section} must be a dictionary')
                continue

            for subfield in required_subfields:
                if subfield not in fm[section]:
                    incomplete_sections.append(f'{section}.{subfield}')
                    errors.append(f'Missing required field: {section}.{subfield}')

    details['missing_sections'] = missing_sections
    details['incomplete_sections'] = incomplete_sections

    # Check completion percentage consistency
    if 'completion_percentage' in fm and 'research_quality' in fm:
        if isinstance(fm['research_quality'], dict):
            rq_completion = fm['research_quality'].get('completeness_percentage')
            top_completion = fm.get('completion_percentage')

            if rq_completion and top_completion and abs(rq_completion - top_completion) > 5:
                warnings.append(
                    f'Completion percentage mismatch: '
                    f'top-level={top_completion}, research_quality={rq_completion}'
                )

    # Check gap arrays populated
    gap_counts = {
        'critical': len(fm.get('critical_gaps', [])),
        'high': len(fm.get('high_gaps', [])),
        'medium': len(fm.get('medium_gaps', []))
    }
    details['gap_counts'] = gap_counts

    total_gaps = sum(gap_counts.values())
    if total_gaps == 0:
        warnings.append('All gap arrays are empty - consider documenting research gaps')

    # Calculate score (25 points max)
    # - 10 points: All required fields present
    # - 10 points: All required sections present and complete
    # - 5 points: Version 3.0 compliance

    field_score = max(0, 10 - len(missing_fields) * 2)
    section_score = max(0, 10 - len(missing_sections) * 2 - len(incomplete_sections))
    version_score = 5 if version in ['3.0', 3.0] else 0

    score = field_score + section_score + version_score

    details['field_score'] = field_score
    details['section_score'] = section_score
    details['version_score'] = version_score

    return {
        'valid': len(errors) == 0,
        'version': str(version),
        'errors': errors,
        'warnings': warnings,
        'score': score,
        'details': details
    }


def main():
    """CLI entry point"""
    if len(sys.argv) < 2:
        print("Usage: frontmatter_validator.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not Path(file_path).exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    result = validate_frontmatter(file_path)

    # Print results
    print(f"Frontmatter Validation: {file_path}")
    print(f"Version: {result['version']}")
    print(f"Valid: {result['valid']}")
    print(f"Score: {result['score']}/25")
    print()

    if result['errors']:
        print(f"Errors ({len(result['errors'])}):")
        for error in result['errors']:
            print(f"  - {error}")
        print()

    if result['warnings']:
        print(f"Warnings ({len(result['warnings'])}):")
        for warning in result['warnings']:
            print(f"  - {warning}")
        print()

    if result['details']:
        print("Details:")
        for key, value in result['details'].items():
            print(f"  {key}: {value}")

    # Exit with error code if invalid
    sys.exit(0 if result['valid'] else 1)


if __name__ == '__main__':
    main()
