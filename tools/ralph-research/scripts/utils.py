#!/usr/bin/env python3
"""
Shared utilities for Ralph Research verification scripts
"""

import re
import yaml
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any


def extract_frontmatter(content: str) -> Tuple[Optional[Dict[str, Any]], str]:
    """
    Extract YAML frontmatter from markdown content.

    Returns:
        Tuple of (frontmatter_dict, body_content)
        frontmatter_dict is None if no valid frontmatter found
    """
    if not content.startswith('---'):
        return None, content

    # Find end of frontmatter
    end_idx = content.find('\n---\n', 3)
    if end_idx == -1:
        # Try alternative format (--- without newline)
        end_idx = content.find('\n---', 3)
        if end_idx == -1:
            return None, content

    frontmatter_text = content[4:end_idx]  # Skip first '---\n'
    body = content[end_idx + 5:]  # Skip '\n---\n'

    try:
        fm = yaml.safe_load(frontmatter_text)
        return fm, body
    except yaml.YAMLError as e:
        return None, content


def parse_markdown_sections(content: str) -> Dict[str, str]:
    """
    Parse markdown content into sections based on headings.

    Returns:
        Dict mapping section heading to section content
    """
    sections = {}

    # Split by h2/h3 headings (## or ###)
    heading_pattern = r'^(#{2,3})\s+(.+)$'
    lines = content.split('\n')

    current_section = None
    current_content = []

    for line in lines:
        match = re.match(heading_pattern, line)
        if match:
            # Save previous section
            if current_section:
                sections[current_section] = '\n'.join(current_content)

            # Start new section
            current_section = match.group(2).strip()
            current_content = []
        else:
            if current_section:
                current_content.append(line)

    # Save last section
    if current_section:
        sections[current_section] = '\n'.join(current_content)

    return sections


def count_evidence_tags(content: str) -> Dict[str, int]:
    """
    Count evidence classification tags in content.

    Returns:
        Dict with counts for fact, inference, gap tags
    """
    fact_pattern = r'\[FACT(?:\s*-\s*(?:STATUTE|ADMIN_CODE|BOARD))?\]'
    inference_pattern = r'\[INFERENCE(?:\s*-\s*(?:HIGH|MEDIUM|LOW)\s+CONFIDENCE)?\]'
    gap_pattern = r'\[CRITICAL GAP\]'

    return {
        'fact_count': len(re.findall(fact_pattern, content)),
        'inference_count': len(re.findall(inference_pattern, content)),
        'gap_count': len(re.findall(gap_pattern, content))
    }


def extract_citations(content: str) -> List[Dict[str, str]]:
    """
    Extract citation information from content.

    Returns:
        List of dicts with citation info (text, source, url, quote)
    """
    citations = []

    # Pattern to match [FACT] blocks with citations
    # Looks for [FACT...] followed by text containing Citation: and optionally Source: and Quote:
    fact_pattern = r'\[FACT[^\]]*\](.*?)(?=\n\[|$)'

    for match in re.finditer(fact_pattern, content, re.DOTALL):
        fact_text = match.group(1)

        citation_info = {
            'text': fact_text[:100],  # First 100 chars
            'has_citation': False,
            'has_source': False,
            'has_quote': False,
            'source_url': None
        }

        # Check for Citation field
        if 'Citation:' in fact_text:
            citation_info['has_citation'] = True

        # Extract Source URL
        source_match = re.search(r'Source:\s*(https?://[^\s\)]+)', fact_text)
        if source_match:
            citation_info['has_source'] = True
            citation_info['source_url'] = source_match.group(1)

        # Check for Quote field
        if 'Quote:' in fact_text or '> ' in fact_text:
            citation_info['has_quote'] = True

        citations.append(citation_info)

    return citations


def load_config(config_path: Path) -> Dict[str, str]:
    """
    Load configuration from file.
    Supports simple key=value format.

    Returns:
        Dict of config key-value pairs
    """
    config = {}

    if not config_path.exists():
        return config

    with open(config_path, 'r') as f:
        for line in f:
            line = line.strip()

            # Skip comments and empty lines
            if not line or line.startswith('#'):
                continue

            # Parse key=value
            if '=' in line:
                key, value = line.split('=', 1)
                config[key.strip()] = value.strip()

    return config


def load_required_sections(config_path: Path) -> List[str]:
    """
    Load required sections list from config file.

    Returns:
        List of required section headings
    """
    sections = []

    if not config_path.exists():
        return sections

    with open(config_path, 'r') as f:
        for line in f:
            line = line.strip()

            # Skip comments and empty lines
            if not line or line.startswith('#'):
                continue

            sections.append(line)

    return sections


def check_section_presence(content: str, required_sections: List[str]) -> Dict[str, bool]:
    """
    Check which required sections are present in content.

    Returns:
        Dict mapping section name to presence boolean
    """
    presence = {}

    for section in required_sections:
        # Match as h2 or h3 heading
        pattern = rf'##+ {re.escape(section)}'
        presence[section] = bool(re.search(pattern, content))

    return presence


def calculate_completion_percentage(
    sections_present: int,
    total_sections: int,
    fact_count: int,
    citation_ratio: float,
    line_count: int
) -> int:
    """
    Calculate estimated completion percentage based on metrics.

    Returns:
        Integer percentage (0-100)
    """
    # Weight different factors
    section_score = (sections_present / total_sections) * 30 if total_sections > 0 else 0
    evidence_score = min(30, (fact_count / 50) * 30)  # Target: 50+ facts
    citation_score = citation_ratio * 20  # Citations are important
    length_score = min(20, (line_count / 450) * 20)  # Target: 450+ lines

    total = section_score + evidence_score + citation_score + length_score

    return int(total)


def format_error_message(errors: List[str], context: str = "") -> str:
    """
    Format error messages for display.

    Returns:
        Formatted error string
    """
    if not errors:
        return ""

    message = ""
    if context:
        message += f"{context}\n"

    for i, error in enumerate(errors, 1):
        message += f"  {i}. {error}\n"

    return message


def get_document_tier(filename: str) -> Optional[str]:
    """
    Extract tier classification from filename or document.

    Returns:
        'TIER-1', 'TIER-2', 'TIER-3', or None
    """
    tier_match = re.search(r'TIER-(\d)', filename)
    if tier_match:
        return f"TIER-{tier_match.group(1)}"

    return None


def validate_url(url: str) -> bool:
    """
    Basic URL validation.

    Returns:
        True if URL appears valid
    """
    url_pattern = r'^https?://[^\s/$.?#].[^\s]*$'
    return bool(re.match(url_pattern, url))


def get_state_from_filename(filename: str) -> Optional[str]:
    """
    Extract state abbreviation from filename.
    Expects format: XX-MD-* or XX-DO-*

    Returns:
        State abbreviation (e.g., 'GA', 'ID') or None
    """
    match = re.match(r'^([A-Z]{2})-(MD|DO)-', filename)
    if match:
        return match.group(1)
    return None


def get_license_type_from_filename(filename: str) -> Optional[str]:
    """
    Extract license type from filename.

    Returns:
        'MD' or 'DO' or None
    """
    match = re.match(r'^[A-Z]{2}-(MD|DO)-', filename)
    if match:
        return match.group(1)
    return None
