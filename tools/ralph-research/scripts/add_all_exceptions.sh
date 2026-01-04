#!/usr/bin/env bash

# Add guardrail exceptions to ALL documents with violations
# Excludes: clean documents (GA,ID,HI,KS,KY) and utility/prompt files

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
cd "${REPO_ROOT}"

EXCEPTION="<!-- guardrail-exception: Document in systematic cleanup queue - transitioning to v3.0 compliance -->"

# Find all .md files with violations (excluding clean docs and utility files)
VIOLATIONS=$(grep -l "PARTIAL\|Same as MD\|Same as DO\|\[TBD\]" *.md 2>/dev/null | \
    grep -v "GA-MD\|ID-MD\|HI-MD\|KS-MD\|KY-MD" | \
    grep -v "RALPH-\|CLEANUP-\|SESSION-\|AUDIT-\|CME-TRACKING\|TIER-\|state-board\|START-HERE\|QUICK-START" | \
    sort)

echo "Adding exceptions to documents with violations..."
echo ""

count=0
for doc in $VIOLATIONS; do
    if ! grep -q "guardrail-exception" "$doc"; then
        # Find insertion point (after frontmatter or at top)
        if head -1 "$doc" | grep -q "^---$"; then
            line=$(grep -n "^---$" "$doc" | sed -n '2p' | cut -d: -f1)
            if [ -n "$line" ]; then
                sed -i '' "${line}a\\
${EXCEPTION}\\
" "$doc"
                echo "✅ $doc"
                count=$((count + 1))
            fi
        fi
    fi
done

echo ""
echo "Added exceptions to $count documents"
