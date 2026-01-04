#!/usr/bin/env python3
"""
Quality threshold checker - implements 100-point audit rubric
Combines all validators to calculate comprehensive quality score
"""

import sys
import json
from pathlib import Path
from typing import Dict, List, Any

# Add scripts dir to path
sys.path.insert(0, str(Path(__file__).parent))
from utils import (
    extract_frontmatter,
    parse_markdown_sections,
    load_required_sections,
    check_section_presence
)
from frontmatter_validator import validate_frontmatter
from evidence_analyzer import analyze_evidence
from citation_validator import validate_citations


def check_section_completeness(file_path: str, config_dir: Path) -> Dict[str, Any]:
    """
    Check if all required sections are present and complete.

    Returns:
        {
            'score': int,  # Max 20 points
            'required_count': int,
            'present_count': int,
            'missing_sections': List[str],
            'short_sections': List[str]
        }
    """
    # Load required sections
    required_sections_file = config_dir / 'required-sections.conf'
    required_sections = load_required_sections(required_sections_file)

    if not required_sections:
        # Fallback to default
        required_sections = [
            'Executive Summary',
            'Board Information',
            'Lifecycle Phases',
            'CME Requirements - Total Hours',
            'CME Topic Requirements',
            'Controlled Substance',
            'Audit & Verification',
            'Exemptions',
            'Renewal Fees',
            'Lapsed License',
            'CME Tracking',
            'State-Specific',
            'Research Gaps',
            'Sources Cited'
        ]

    # Read file
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {
            'score': 0,
            'required_count': len(required_sections),
            'present_count': 0,
            'missing_sections': required_sections,
            'short_sections': []
        }

    fm, body = extract_frontmatter(content)

    # Check which sections are present
    presence = check_section_presence(body, required_sections)
    present_sections = [s for s, present in presence.items() if present]
    missing_sections = [s for s, present in presence.items() if not present]

    # Parse sections and check length
    sections = parse_markdown_sections(body)
    short_sections = []

    for section_name, section_content in sections.items():
        # Sections should have substantial content (>100 chars)
        if len(section_content.strip()) < 100:
            short_sections.append(section_name)

    # Calculate score (20 points max)
    # - 15 points: section presence (15 * present/required)
    # - 5 points: section completeness (no short sections)

    presence_score = int((len(present_sections) / len(required_sections)) * 15)
    completeness_penalty = min(5, len(short_sections))
    completeness_score = max(0, 5 - completeness_penalty)

    total_score = presence_score + completeness_score

    return {
        'score': total_score,
        'required_count': len(required_sections),
        'present_count': len(present_sections),
        'missing_sections': missing_sections,
        'short_sections': short_sections,
        'presence_score': presence_score,
        'completeness_score': completeness_score
    }


def check_gap_documentation(file_path: str) -> Dict[str, Any]:
    """
    Check gap documentation quality.

    Returns:
        {
            'score': int,  # Max 10 points
            'gaps_in_frontmatter': int,
            'gaps_in_body': int,
            'consistency': bool
        }
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return {
            'score': 0,
            'gaps_in_frontmatter': 0,
            'gaps_in_body': 0,
            'consistency': False
        }

    fm, body = extract_frontmatter(content)

    # Count gaps in frontmatter
    gaps_in_fm = 0
    if fm:
        gaps_in_fm += len(fm.get('critical_gaps', []))
        gaps_in_fm += len(fm.get('high_gaps', []))
        gaps_in_fm += len(fm.get('medium_gaps', []))

    # Count [CRITICAL GAP] tags in body
    import re
    gaps_in_body = len(re.findall(r'\[CRITICAL GAP\]', body))

    # Check consistency (gaps documented in both places)
    consistency = abs(gaps_in_fm - gaps_in_body) <= 2  # Allow small variance

    # Calculate score (10 points max)
    # - 5 points: gaps documented (min 3 for full points)
    # - 3 points: consistency between frontmatter and body
    # - 2 points: gap quality (has descriptions in frontmatter)

    gap_count_score = min(5, (gaps_in_body // 3) * 5) if gaps_in_body > 0 else 0
    consistency_score = 3 if consistency else 0

    quality_score = 0
    if fm and gaps_in_fm > 0:
        # Check if gaps have descriptions
        for gap_array in ['critical_gaps', 'high_gaps', 'medium_gaps']:
            gaps = fm.get(gap_array, [])
            if gaps and isinstance(gaps, list) and len(gaps) > 0:
                if isinstance(gaps[0], dict) and 'description' in gaps[0]:
                    quality_score = 2
                    break

    total_score = gap_count_score + consistency_score + quality_score

    return {
        'score': total_score,
        'gaps_in_frontmatter': gaps_in_fm,
        'gaps_in_body': gaps_in_body,
        'consistency': consistency,
        'gap_count_score': gap_count_score,
        'consistency_score': consistency_score,
        'quality_score': quality_score
    }


def check_congruency_tracking(file_path: str) -> Dict[str, Any]:
    """
    Check cross-source congruency tracking.

    Returns:
        {
            'score': int,  # Max 5 points
            'congruency_documented': bool
        }
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return {
            'score': 0,
            'congruency_documented': False
        }

    # Look for congruency tracking markers
    import re
    congruency_markers = [
        r'cross-source',
        r'congruency',
        r'verified across.*sources',
        r'consistent with.*statute'
    ]

    found_markers = 0
    for marker in congruency_markers:
        if re.search(marker, content, re.IGNORECASE):
            found_markers += 1

    congruency_documented = found_markers >= 2

    # Simple scoring: 5 points if documented, 0 if not
    score = 5 if congruency_documented else 0

    return {
        'score': score,
        'congruency_documented': congruency_documented,
        'markers_found': found_markers
    }


def calculate_quality_score(file_path: str, config_dir: Path = None) -> Dict[str, Any]:
    """
    Calculate comprehensive quality score using 100-point rubric.

    Rubric breakdown:
    - Frontmatter (25 points)
    - Section completeness (20 points)
    - Evidence classification (25 points)
    - Citation quality (15 points)
    - Gap documentation (10 points)
    - Cross-source congruency (5 points)

    Returns:
        {
            'total_score': int,
            'passed_85': bool,
            'breakdown': Dict[str, int],
            'details': Dict,
            'recommendations': List[str]
        }
    """
    if config_dir is None:
        # Default to config dir relative to this script
        script_dir = Path(__file__).parent.parent
        config_dir = script_dir / 'config'

    recommendations = []

    # Phase 1: Frontmatter (25 points)
    fm_result = validate_frontmatter(file_path)
    fm_score = fm_result['score']

    if not fm_result['valid']:
        recommendations.append(
            f"Apply v3.0 frontmatter template (would add ~{25 - fm_score} points)"
        )

    # Phase 2: Section Completeness (20 points)
    sections_result = check_section_completeness(file_path, config_dir)
    sections_score = sections_result['score']

    if sections_result['missing_sections']:
        recommendations.append(
            f"Add missing sections: {', '.join(sections_result['missing_sections'][:3])}"
        )

    # Phase 3: Evidence Classification (25 points)
    evidence_result = analyze_evidence(file_path)
    evidence_score = evidence_result['score']

    if evidence_result['fact_count'] < 50:
        recommendations.append(
            f"Increase [FACT] tag usage (current: {evidence_result['fact_count']}, target: 50+)"
        )

    # Phase 4: Citation Quality (15 points)
    citation_result = validate_citations(file_path)
    citation_score = citation_result['score']

    if citation_result['citation_ratio'] < 0.5:
        recommendations.append(
            "Add citations to [FACT] tags (target: 50%+ with citations)"
        )

    # Phase 5: Gap Documentation (10 points)
    gap_result = check_gap_documentation(file_path)
    gap_score = gap_result['score']

    if gap_result['gaps_in_body'] < 3:
        recommendations.append(
            "Document research gaps using [CRITICAL GAP] tags"
        )

    # Phase 6: Cross-Source Congruency (5 points)
    congruency_result = check_congruency_tracking(file_path)
    congruency_score = congruency_result['score']

    # Calculate total
    total_score = (
        fm_score +
        sections_score +
        evidence_score +
        citation_score +
        gap_score +
        congruency_score
    )

    passed_85 = total_score >= 85

    return {
        'total_score': total_score,
        'passed_85': passed_85,
        'breakdown': {
            'frontmatter': fm_score,
            'sections': sections_score,
            'evidence': evidence_score,
            'citations': citation_score,
            'gaps': gap_score,
            'congruency': congruency_score
        },
        'details': {
            'frontmatter': fm_result,
            'sections': sections_result,
            'evidence': evidence_result,
            'citations': citation_result,
            'gaps': gap_result,
            'congruency': congruency_result
        },
        'recommendations': recommendations
    }


def main():
    """CLI entry point"""
    if len(sys.argv) < 2:
        print("Usage: quality_threshold_check.py <file_path> [--json]")
        sys.exit(1)

    file_path = sys.argv[1]
    output_json = '--json' in sys.argv

    if not Path(file_path).exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    # Calculate score
    result = calculate_quality_score(file_path)

    if output_json:
        # JSON output for scripting
        print(json.dumps(result, indent=2))
    else:
        # Human-readable output
        print(f"Quality Threshold Check: {Path(file_path).name}")
        print(f"{'='*60}")
        print(f"Total Score: {result['total_score']}/100")
        print(f"Threshold (85%): {'PASS' if result['passed_85'] else 'FAIL'}")
        print()
        print("Score Breakdown:")
        for category, score in result['breakdown'].items():
            max_scores = {
                'frontmatter': 25,
                'sections': 20,
                'evidence': 25,
                'citations': 15,
                'gaps': 10,
                'congruency': 5
            }
            max_score = max_scores[category]
            bar_length = int((score / max_score) * 30)
            bar = '█' * bar_length + '░' * (30 - bar_length)
            print(f"  {category:15} {score:2}/{max_score:2} {bar}")
        print()

        if result['recommendations']:
            print("Recommendations to improve score:")
            for i, rec in enumerate(result['recommendations'], 1):
                print(f"  {i}. {rec}")
            print()

    # Exit with error if below threshold
    sys.exit(0 if result['passed_85'] else 1)


if __name__ == '__main__':
    main()
