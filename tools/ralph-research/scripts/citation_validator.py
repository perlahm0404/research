#!/usr/bin/env python3
"""
Citation validator for documentation quality
Validates citation format, URL validity, and source hierarchy
"""

import sys
import re
from pathlib import Path
from typing import Dict, List, Any
from urllib.parse import urlparse

# Add scripts dir to path
sys.path.insert(0, str(Path(__file__).parent))
from utils import extract_frontmatter, extract_citations, validate_url


def validate_citations(file_path: str) -> Dict[str, Any]:
    """
    Validate citation quality in document.

    Returns:
        {
            'score': int,  # Max 15 points
            'total_facts': int,
            'with_citation': int,
            'with_url': int,
            'with_quote': int,
            'malformed_urls': List[str],
            'issues': List[str],
            'warnings': List[str],
            'passed': bool
        }
    """
    issues = []
    warnings = []

    # Read file
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {
            'score': 0,
            'total_facts': 0,
            'with_citation': 0,
            'with_url': 0,
            'with_quote': 0,
            'malformed_urls': [],
            'issues': [f'Failed to read file: {e}'],
            'warnings': [],
            'passed': False
        }

    # Extract body
    fm, body = extract_frontmatter(content)

    # Extract all citations
    citations = extract_citations(body)
    total_facts = len(citations)

    with_citation = sum(1 for c in citations if c['has_citation'])
    with_url = sum(1 for c in citations if c['has_source'])
    with_quote = sum(1 for c in citations if c['has_quote'])

    # Calculate ratios
    citation_ratio = with_citation / total_facts if total_facts > 0 else 0
    url_ratio = with_url / total_facts if total_facts > 0 else 0
    quote_ratio = with_quote / total_facts if total_facts > 0 else 0

    # Check citation quality thresholds
    if citation_ratio < 0.5:
        issues.append(
            f'Citation ratio below threshold: {citation_ratio:.0%} '
            f'({with_citation}/{total_facts} facts have citations)'
        )

    if url_ratio < 0.5:
        issues.append(
            f'Source URL ratio below threshold: {url_ratio:.0%} '
            f'({with_url}/{total_facts} facts have URLs)'
        )

    # Validate URLs
    malformed_urls = []
    gov_domain_count = 0
    non_gov_count = 0

    for citation in citations:
        if citation['source_url']:
            url = citation['source_url']

            # Basic URL validation
            if not validate_url(url):
                malformed_urls.append(url)
                continue

            # Parse domain
            try:
                parsed = urlparse(url)
                domain = parsed.netloc.lower()

                # Check for .gov domain (preferred)
                if '.gov' in domain:
                    gov_domain_count += 1
                else:
                    non_gov_count += 1

            except Exception:
                malformed_urls.append(url)

    if malformed_urls:
        warnings.append(f'{len(malformed_urls)} potentially malformed URLs found')

    # Check source hierarchy preference
    if total_facts > 0:
        gov_ratio = gov_domain_count / total_facts
        if gov_ratio < 0.5:
            warnings.append(
                f'Low .gov domain ratio: {gov_ratio:.0%} '
                f'(prefer statute/admin code from official .gov sources)'
            )

    # Check for common citation issues
    citation_issues = check_citation_patterns(body)
    issues.extend(citation_issues['issues'])
    warnings.extend(citation_issues['warnings'])

    # Calculate score (15 points max)
    # - Citation field present (5 points): citation_ratio * 5
    # - Source URL present (5 points): url_ratio * 5
    # - Quote/evidence (3 points): quote_ratio * 3
    # - URL quality (2 points): -1 per 5 malformed URLs

    citation_score = int(citation_ratio * 5)
    url_score = int(url_ratio * 5)
    quote_score = int(quote_ratio * 3)
    quality_penalty = min(2, len(malformed_urls) // 5)
    quality_score = max(0, 2 - quality_penalty)

    total_score = citation_score + url_score + quote_score + quality_score

    # Determine if passed (minimum 10/15 points = 67%)
    passed = total_score >= 10

    return {
        'score': total_score,
        'total_facts': total_facts,
        'with_citation': with_citation,
        'with_url': with_url,
        'with_quote': with_quote,
        'gov_domain_count': gov_domain_count,
        'non_gov_count': non_gov_count,
        'malformed_urls': malformed_urls,
        'citation_ratio': round(citation_ratio, 2),
        'url_ratio': round(url_ratio, 2),
        'quote_ratio': round(quote_ratio, 2),
        'issues': issues,
        'warnings': warnings,
        'passed': passed
    }


def check_citation_patterns(body: str) -> Dict[str, List[str]]:
    """
    Check for common citation format issues.

    Returns:
        {
            'issues': List[str],
            'warnings': List[str]
        }
    """
    issues = []
    warnings = []

    # Check for incomplete citations
    incomplete_patterns = [
        (r'Citation:\s*\(pending\)', 'Citations marked as pending'),
        (r'Source:\s*\(TBD\)', 'Sources marked as TBD'),
        (r'Citation:\s*TBD', 'Citations marked as TBD'),
        (r'\[FACT\].*\(no source\)', 'Facts explicitly marked with no source'),
        (r'\[FACT\].*\(unable to verify\)', 'Facts marked as unable to verify')
    ]

    for pattern, description in incomplete_patterns:
        matches = re.findall(pattern, body, re.IGNORECASE)
        if matches:
            issues.append(f'{description}: {len(matches)} instances')

    # Check for source hierarchy markers
    statute_count = len(re.findall(r'\[FACT\s*-\s*STATUTE\]', body))
    admin_count = len(re.findall(r'\[FACT\s*-\s*ADMIN_CODE\]', body))
    board_count = len(re.findall(r'\[FACT\s*-\s*BOARD\]', body))

    total_classified = statute_count + admin_count + board_count

    if total_classified > 0:
        # Good: using source hierarchy
        hierarchy_ratio = total_classified / len(re.findall(r'\[FACT', body))
        if hierarchy_ratio < 0.5:
            warnings.append(
                f'Only {hierarchy_ratio:.0%} of facts use source hierarchy tags '
                f'([FACT - STATUTE/ADMIN_CODE/BOARD])'
            )

    return {
        'issues': issues,
        'warnings': warnings
    }


def main():
    """CLI entry point"""
    if len(sys.argv) < 2:
        print("Usage: citation_validator.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not Path(file_path).exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    result = validate_citations(file_path)

    # Print results
    print(f"Citation Validation: {file_path}")
    print(f"Score: {result['score']}/15")
    print(f"Passed: {result['passed']}")
    print()
    print(f"Citation Statistics:")
    print(f"  Total [FACT] tags: {result['total_facts']}")
    print(f"  With Citation field: {result['with_citation']} ({result['citation_ratio']:.0%})")
    print(f"  With Source URL: {result['with_url']} ({result['url_ratio']:.0%})")
    print(f"  With Quote/evidence: {result['with_quote']} ({result['quote_ratio']:.0%})")
    print()
    print(f"Source Quality:")
    print(f"  .gov domains: {result['gov_domain_count']}")
    print(f"  Non-.gov domains: {result['non_gov_count']}")
    print(f"  Malformed URLs: {len(result['malformed_urls'])}")
    print()

    if result['issues']:
        print(f"Issues ({len(result['issues'])}):")
        for issue in result['issues']:
            print(f"  - {issue}")
        print()

    if result['warnings']:
        print(f"Warnings ({len(result['warnings'])}):")
        for warning in result['warnings']:
            print(f"  - {warning}")
        print()

    if result['malformed_urls'][:5]:  # Show first 5
        print(f"Sample Malformed URLs:")
        for url in result['malformed_urls'][:5]:
            print(f"  - {url}")
        print()

    # Exit with error if not passed
    sys.exit(0 if result['passed'] else 1)


if __name__ == '__main__':
    main()
