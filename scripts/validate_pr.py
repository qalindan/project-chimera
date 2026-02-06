#!/usr/bin/env python3
"""Validate Pull Requests for spec alignment."""

import json
import sys
import os

def validate_pr():
    """Check if PR follows project standards."""
    print("🔍 PR Validation Check")
    print("=" * 50)
    
    # Check for spec references in changed files
    spec_keywords = ["specs/technical.md", "specs/api_contract.md", 
                     "TrendResearchInput", "TrendResearchOutput", "Pydantic"]
    
    changed_files = os.getenv("CHANGED_FILES", "").split()
    
    spec_references = []
    for file in changed_files:
        if file.endswith(".py"):
            with open(file, "r") as f:
                content = f.read()
                for keyword in spec_keywords:
                    if keyword in content:
                        spec_references.append((file, keyword))
    
    if spec_references:
        print("✅ Found spec references:")
        for file, keyword in spec_references:
            print(f"   - {file}: references {keyword}")
    else:
        print("❌ No spec references found in changed files!")
        return False
    
    # Check if tests were updated
    test_files = [f for f in changed_files if "test" in f.lower()]
    if test_files:
        print(f"✅ Tests updated: {', '.join(test_files)}")
    else:
        print("⚠️  No test files modified. Ensure TDD compliance.")
    
    print("=" * 50)
    return True

if __name__ == "__main__":
    if validate_pr():
        print("✅ PR validation passed")
        sys.exit(0)
    else:
        print("❌ PR validation failed")
        sys.exit(1)