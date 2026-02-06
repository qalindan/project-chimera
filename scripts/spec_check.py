#!/usr/bin/env python3
"""Check if code aligns with specifications."""

import os
import sys

def check_spec_alignment():
    """Verify code follows specs."""
    checks = []
    
    # Check 1: specs directory exists
    checks.append(("Specs directory", os.path.exists("specs/")))
    
    # Check 2: technical.md exists
    checks.append(("Technical spec", os.path.exists("specs/technical.md")))
    
    # Check 3: trend_research.py follows patterns
    if os.path.exists("research/trend_research.py"):
        with open("research/trend_research.py", "r") as f:
            content = f.read()
            checks.append(("Pydantic models", "class TrendResearchInput" in content))
            checks.append(("API contract", "def research_trends" in content))
    
    # Check 4: tests exist
    checks.append(("Test suite", os.path.exists("tests/test_trend_research.py")))
    
    # Print results
    print("🔍 Spec Alignment Check")
    print("=" * 40)
    
    all_passed = True
    for name, passed in checks:
        status = "✅" if passed else "❌"
        print(f"{status} {name}")
        if not passed:
            all_passed = False
    
    print("=" * 40)
    return all_passed

if __name__ == "__main__":
    if check_spec_alignment():
        print("✅ All spec checks passed!")
        sys.exit(0)
    else:
        print("❌ Some spec checks failed")
        sys.exit(1)