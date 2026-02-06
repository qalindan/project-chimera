#!/bin/bash
echo "🔍 Running spec alignment check..."
echo "Checking if code follows specs/technical.md..."

# Check if research/trend_research.py follows spec
if grep -q "class TrendResearchInput" research/trend_research.py; then
    echo "✅ TrendResearchInput class found (matches spec)"
else
    echo "❌ TrendResearchInput class missing"
    exit 1
fi

if grep -q "class TrendResearchOutput" research/trend_research.py; then
    echo "✅ TrendResearchOutput class found (matches spec)"
else
    echo "❌ TrendResearchOutput class missing"
    exit 1
fi

# Check if tests validate spec
if grep -q "expected_input_structure" tests/test_trend_research.py; then
    echo "✅ Tests check input structure (matches spec)"
else
    echo "❌ Tests missing input structure validation"
    exit 1
fi

echo "✅ All spec checks passed!"