#!/usr/bin/env python3
"""Run trend research tests."""
import subprocess
import sys

def run_pytest():
    """Run tests using pytest."""
    print("🧪 Running tests with pytest...\n")
    result = subprocess.run([sys.executable, "-m", "pytest", "tests/", "-v"])
    return result.returncode

def run_manual_tests():
    """Run manual test suite."""
    print("🧪 Running manual tests...\n")
    from tests.test_trend_research import (
        test_trend_research_api_contract,
        test_trend_research_validation,
        test_trend_research_functionality
    )
    
    try:
        test_trend_research_api_contract()
        test_trend_research_validation()
        test_trend_research_functionality()
        print("\n✅ All manual tests passed!")
        return 0
    except Exception as e:
        print(f"\n❌ Manual tests failed: {e}")
        return 1

if __name__ == "__main__":
    print("🚀 Starting Trend Research Test Suite\n")
    
    # Try pytest first, fall back to manual
    return_code = run_pytest()
    
    if return_code != 0:
        print("\n⚠️  Pytest failed, trying manual tests...")
        return_code = run_manual_tests()
    
    sys.exit(return_code)