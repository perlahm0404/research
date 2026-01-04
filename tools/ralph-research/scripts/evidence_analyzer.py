#!/usr/bin/env python3
"""
Evidence analyzer for documentation quality
Analyzes [FACT], [INFERENCE], and [CRITICAL GAP] tag usage
"""

import sys
import re
from pathlib import Path
from typing import Dict, List, Any

# Add scripts dir to path
sys.path.insert(0, str(Path(__file__).parent))
from utils import extract_frontmatter, count_evidence_tags, parse_markdown_sections


def analyze_evidence(file_path: str) -> Dict[str, Any]:
    """
    Analyze evidence classification tags in document.

    Returns:
        {
            'score': int,  # Max 25 points
            'fact_count': int,
            'inference_count': int,
            'gap_count': int,
            'citation_ratio': float,
            'details': Dict,
            'issues': List[str],
            'warnings': List[str]
        }
    """
    issues = []
    warnings = []
    details = {}

    # Read file
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {
            'score': 0,
            'fact_count': 0,
            'inference_count': 0,
            'gap_count': 0,
            'citation_ratio': 0.0,
            'details': {},
            'issues': [f'Failed to read file: {e}'],
            'warnings': []
        }

    # Extract frontmatter and body
    fm, body = extract_frontmatter(content)

    # Count evidence tags
    tag_counts = count_evidence_tags(body)
    fact_count = tag_counts['fact_count']
    inference_count = tag_counts['inference_count']
    gap_count = tag_counts['gap_count']

    details['fact_count'] = fact_count
    details['inference_count'] = inference_count
    details['gap_count'] = gap_count

    # Analyze FACT tags with citations
    fact_pattern = r'\[FACT[^\]]*\](.*?)(?=\n\[|\n##|$)'
    facts = re.findall(fact_pattern, body, re.DOTALL)

    facts_with_citations = 0
    facts_with_sources = 0
    facts_with_quotes = 0

    for fact_text in facts:
        if 'Citation:' in fact_text:
            facts_with_citations += 1
        if 'Source:' in fact_text or 'https://' in fact_text:
            facts_with_sources += 1
        if 'Quote:' in fact_text or '> ' in fact_text:
            facts_with_quotes += 1

    citation_ratio = facts_with_citations / fact_count if fact_count > 0 else 0
    source_ratio = facts_with_sources / fact_count if fact_count > 0 else 0
    quote_ratio = facts_with_quotes / fact_count if fact_count > 0 else 0

    details['facts_with_citations'] = facts_with_citations
    details['facts_with_sources'] = facts_with_sources
    details['facts_with_quotes'] = facts_with_quotes
    details['citation_ratio'] = round(citation_ratio, 2)
    details['source_ratio'] = round(source_ratio, 2)
    details['quote_ratio'] = round(quote_ratio, 2)

    # Check citation quality
    if citation_ratio < 0.5:
        issues.append(f'Low citation ratio: {citation_ratio:.0%} (target: 50%+)')

    if source_ratio < 0.5:
        issues.append(f'Low source URL ratio: {source_ratio:.0%} (target: 50%+)')

    # Analyze INFERENCE tags
    inference_pattern = r'\[INFERENCE[^\]]*\](.*?)(?=\n\[|\n##|$)'
    inferences = re.findall(inference_pattern, body, re.DOTALL)

    inferences_with_reasoning = 0
    for inf_text in inferences:
        if 'Reasoning:' in inf_text or 'Rationale:' in inf_text:
            inferences_with_reasoning += 1

    reasoning_ratio = inferences_with_reasoning / inference_count if inference_count > 0 else 1.0
    details['inferences_with_reasoning'] = inferences_with_reasoning
    details['reasoning_ratio'] = round(reasoning_ratio, 2)

    if inference_count > 0 and reasoning_ratio < 0.7:
        warnings.append(f'Low reasoning ratio for inferences: {reasoning_ratio:.0%} (target: 70%+)')

    # Check evidence density targets
    # TIER-1 targets: 50+ facts, 5+ inferences, 3+ gaps
    if fact_count < 50:
        warnings.append(f'Fact count below TIER-1 target: {fact_count} (target: 50+)')

    if inference_count < 5:
        warnings.append(f'Inference count below target: {inference_count} (target: 5+)')

    if gap_count < 3:
        warnings.append(f'Gap documentation below target: {gap_count} (target: 3+)')

    # Analyze evidence distribution across sections
    sections = parse_markdown_sections(body)
    section_evidence = {}

    for section_name, section_content in sections.items():
        section_tags = count_evidence_tags(section_content)
        section_evidence[section_name] = {
            'facts': section_tags['fact_count'],
            'inferences': section_tags['inference_count'],
            'gaps': section_tags['gap_count']
        }

    # Find sections with no evidence
    empty_sections = [name for name, tags in section_evidence.items()
                      if tags['facts'] == 0 and len(sections[name]) > 200]

    if empty_sections:
        details['empty_sections'] = empty_sections
        warnings.append(f'{len(empty_sections)} substantial sections have no [FACT] tags')

    details['section_evidence'] = section_evidence

    # Calculate score (25 points max)
    # - Fact count (10 points): min(10, fact_count / 5)
    # - Citation ratio (5 points): citation_ratio * 5
    # - Source ratio (5 points): source_ratio * 5
    # - Inference quality (3 points): reasoning_ratio * 3
    # - Gap documentation (2 points): min(2, gap_count / 3 * 2)

    fact_score = min(10, fact_count // 5)
    citation_score = int(citation_ratio * 5)
    source_score = int(source_ratio * 5)
    inference_score = int(reasoning_ratio * 3)
    gap_score = min(2, int((gap_count / 3) * 2))

    total_score = fact_score + citation_score + source_score + inference_score + gap_score

    details['fact_score'] = fact_score
    details['citation_score'] = citation_score
    details['source_score'] = source_score
    details['inference_score'] = inference_score
    details['gap_score'] = gap_score

    return {
        'score': total_score,
        'fact_count': fact_count,
        'inference_count': inference_count,
        'gap_count': gap_count,
        'citation_ratio': citation_ratio,
        'details': details,
        'issues': issues,
        'warnings': warnings
    }


def main():
    """CLI entry point"""
    if len(sys.argv) < 2:
        print("Usage: evidence_analyzer.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not Path(file_path).exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    result = analyze_evidence(file_path)

    # Print results
    print(f"Evidence Analysis: {file_path}")
    print(f"Score: {result['score']}/25")
    print()
    print(f"Evidence Tags:")
    print(f"  [FACT]: {result['fact_count']}")
    print(f"  [INFERENCE]: {result['inference_count']}")
    print(f"  [CRITICAL GAP]: {result['gap_count']}")
    print()
    print(f"Citation Quality:")
    print(f"  Citation Ratio: {result['citation_ratio']:.0%}")
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

    # Exit with error if significant issues
    sys.exit(0 if len(result['issues']) == 0 else 1)


if __name__ == '__main__':
    main()
