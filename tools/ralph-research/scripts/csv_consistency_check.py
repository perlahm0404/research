#!/usr/bin/env python3
"""
CSV consistency checker
Validates consistency between CSV trackers and markdown documents
"""

import sys
import csv
import re
from pathlib import Path
from typing import Dict, List, Any, Tuple

# Add scripts dir to path
sys.path.insert(0, str(Path(__file__).parent))
from utils import (
    extract_frontmatter,
    get_state_from_filename,
    get_license_type_from_filename
)


def load_csv_tracker(csv_path: Path) -> Dict[str, Dict[str, str]]:
    """
    Load CSV tracker and return dict keyed by state-license.

    Returns:
        Dict mapping 'STATE-LICENSE' to row data
    """
    tracker = {}

    if not csv_path.exists():
        return tracker

    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Create key from state abbreviation and license type
                state = row.get('state_abbr', row.get('State', '')).strip()
                license_type = row.get('license_type', row.get('License', '')).strip()

                if state and license_type:
                    key = f"{state}-{license_type}"
                    tracker[key] = row

    except Exception as e:
        print(f"Warning: Failed to load {csv_path}: {e}", file=sys.stderr)

    return tracker


def find_document_files(repo_root: Path) -> List[Path]:
    """
    Find all state document markdown files.

    Returns:
        List of Path objects for MD/DO documents
    """
    documents = []

    # Pattern: XX-MD-*.md or XX-DO-*.md (where XX is state abbreviation)
    for md_file in repo_root.glob('*-MD-*.md'):
        if get_state_from_filename(md_file.name):
            documents.append(md_file)

    for md_file in repo_root.glob('*-DO-*.md'):
        if get_state_from_filename(md_file.name):
            documents.append(md_file)

    return documents


def check_document_csv_consistency(
    doc_path: Path,
    csv_tracker: Dict[str, Dict[str, str]]
) -> Dict[str, Any]:
    """
    Check consistency between a document and CSV tracker.

    Returns:
        {
            'consistent': bool,
            'issues': List[str],
            'warnings': List[str]
        }
    """
    issues = []
    warnings = []

    # Get state and license type from filename
    state = get_state_from_filename(doc_path.name)
    license_type = get_license_type_from_filename(doc_path.name)

    if not state or not license_type:
        issues.append(f"Cannot parse state/license from filename: {doc_path.name}")
        return {'consistent': False, 'issues': issues, 'warnings': warnings}

    key = f"{state}-{license_type}"

    # Check if entry exists in CSV
    if key not in csv_tracker:
        issues.append(f"No CSV entry for {key}")
        return {'consistent': False, 'issues': issues, 'warnings': warnings}

    csv_row = csv_tracker[key]

    # Read document frontmatter
    try:
        with open(doc_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        issues.append(f"Failed to read document: {e}")
        return {'consistent': False, 'issues': issues, 'warnings': warnings}

    fm, body = extract_frontmatter(content)

    if fm is None:
        issues.append("No frontmatter found in document")
        return {'consistent': False, 'issues': issues, 'warnings': warnings}

    # Check completion percentage consistency
    fm_completion = fm.get('completion_percentage', 0)
    csv_completion_fields = [
        'completion_percentage',
        'claimed_completion_%',
        'md_completion_%',
        'do_completion_%'
    ]

    csv_completion = None
    for field in csv_completion_fields:
        if field in csv_row and csv_row[field]:
            try:
                csv_completion = float(csv_row[field])
                break
            except ValueError:
                pass

    if csv_completion is not None:
        if abs(fm_completion - csv_completion) > 5:  # Allow 5% variance
            issues.append(
                f"Completion % mismatch: "
                f"Frontmatter={fm_completion}%, CSV={csv_completion}%"
            )
    else:
        warnings.append("No completion % found in CSV")

    # Check status consistency
    fm_status = fm.get('status', '').upper()
    csv_status_fields = ['status', 'document_status', 'Status']

    csv_status = None
    for field in csv_status_fields:
        if field in csv_row and csv_row[field]:
            csv_status = csv_row[field].upper()
            break

    if csv_status:
        # Normalize status values
        status_map = {
            'COMPREHENSIVE': 'COMPLETE',
            'PARTIAL': 'IN_PROGRESS',
            'STUB': 'PENDING'
        }

        fm_normalized = status_map.get(fm_status, fm_status)
        csv_normalized = status_map.get(csv_status, csv_status)

        if fm_normalized != csv_normalized:
            warnings.append(
                f"Status mismatch: "
                f"Frontmatter={fm_status}, CSV={csv_status}"
            )

    # Check document filename matches CSV reference
    csv_filename_fields = ['document_filename', 'filename', 'Filename']

    csv_filename = None
    for field in csv_filename_fields:
        if field in csv_row and csv_row[field]:
            csv_filename = csv_row[field]
            break

    if csv_filename:
        if csv_filename != doc_path.name:
            issues.append(
                f"Filename mismatch: "
                f"Actual={doc_path.name}, CSV={csv_filename}"
            )

    consistent = len(issues) == 0

    return {
        'consistent': consistent,
        'issues': issues,
        'warnings': warnings,
        'key': key
    }


def check_csv_consistency(repo_root: Path) -> Dict[str, Any]:
    """
    Check consistency across all documents and CSV trackers.

    Returns:
        {
            'passed': bool,
            'documents_checked': int,
            'documents_passed': int,
            'documents_failed': int,
            'issues': List[str],
            'warnings': List[str],
            'details': Dict
        }
    """
    all_issues = []
    all_warnings = []
    details = {}

    # Load CSV trackers
    state_tracker_path = repo_root / 'state-research-tracker.csv'
    audit_tracker_path = repo_root / 'audit-2026-01-03' / '67-board-audit-tracker-MD-DO.csv'

    state_tracker = load_csv_tracker(state_tracker_path)
    audit_tracker = load_csv_tracker(audit_tracker_path)

    if not state_tracker and not audit_tracker:
        all_issues.append("No CSV trackers found")
        return {
            'passed': False,
            'documents_checked': 0,
            'documents_passed': 0,
            'documents_failed': 0,
            'issues': all_issues,
            'warnings': all_warnings,
            'details': {}
        }

    # Find all document files
    documents = find_document_files(repo_root)

    documents_checked = 0
    documents_passed = 0
    documents_failed = 0

    for doc_path in documents:
        documents_checked += 1

        # Check against primary tracker
        tracker = state_tracker if state_tracker else audit_tracker
        result = check_document_csv_consistency(doc_path, tracker)

        doc_name = doc_path.name
        details[doc_name] = result

        if result['consistent']:
            documents_passed += 1
        else:
            documents_failed += 1
            all_issues.append(f"{doc_name}: {', '.join(result['issues'])}")

        if result['warnings']:
            all_warnings.extend([f"{doc_name}: {w}" for w in result['warnings']])

    # Cross-tracker consistency check (if both exist)
    if state_tracker and audit_tracker:
        cross_issues = check_cross_tracker_consistency(state_tracker, audit_tracker)
        all_issues.extend(cross_issues)

    passed = len(all_issues) == 0

    return {
        'passed': passed,
        'documents_checked': documents_checked,
        'documents_passed': documents_passed,
        'documents_failed': documents_failed,
        'issues': all_issues,
        'warnings': all_warnings,
        'details': details
    }


def check_cross_tracker_consistency(
    tracker1: Dict[str, Dict[str, str]],
    tracker2: Dict[str, Dict[str, str]]
) -> List[str]:
    """
    Check consistency between two CSV trackers.

    Returns:
        List of issue strings
    """
    issues = []

    # Check for entries in tracker1 not in tracker2
    for key in tracker1.keys():
        if key not in tracker2:
            issues.append(f"State {key} in state tracker but not in audit tracker")

    # Check for entries in tracker2 not in tracker1
    for key in tracker2.keys():
        if key not in tracker1:
            issues.append(f"State {key} in audit tracker but not in state tracker")

    return issues


def main():
    """CLI entry point"""
    if len(sys.argv) < 2:
        # Default to current directory's parent
        repo_root = Path.cwd()
    else:
        repo_root = Path(sys.argv[1])

    if not repo_root.exists():
        print(f"Error: Directory not found: {repo_root}")
        sys.exit(1)

    result = check_csv_consistency(repo_root)

    # Print results
    print(f"CSV Consistency Check")
    print(f"{'='*60}")
    print(f"Documents Checked: {result['documents_checked']}")
    print(f"Documents Passed: {result['documents_passed']}")
    print(f"Documents Failed: {result['documents_failed']}")
    print(f"Overall: {'PASS' if result['passed'] else 'FAIL'}")
    print()

    if result['issues']:
        print(f"Issues ({len(result['issues'])}):")
        for issue in result['issues'][:20]:  # Show first 20
            print(f"  - {issue}")
        if len(result['issues']) > 20:
            print(f"  ... and {len(result['issues']) - 20} more")
        print()

    if result['warnings']:
        print(f"Warnings ({len(result['warnings'])}):")
        for warning in result['warnings'][:10]:  # Show first 10
            print(f"  - {warning}")
        if len(result['warnings']) > 10:
            print(f"  ... and {len(result['warnings']) - 10} more")
        print()

    # Exit with error if failed
    sys.exit(0 if result['passed'] else 1)


if __name__ == '__main__':
    main()
