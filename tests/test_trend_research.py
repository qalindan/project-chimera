"""Test suite for Trend Research functionality."""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from research.trend_research import TrendResearchAPI, TrendResearchInput, TrendResearchOutput

def test_trend_research_api_contract():
    """Test that trend research API matches spec contract."""
    api = TrendResearchAPI()
    
    # Test input that should work
    valid_input = {
        "niche": "ai-education",
        "region": "global",
        "timeframe": "7d",
        "max_results": 5
    }
    
    # Test the actual API
    result = api.research_trends(valid_input)
    
    # Verify output structure
    assert hasattr(result, 'trends'), "Output missing 'trends' field"
    assert isinstance(result.trends, list), "'trends' should be a list"
    
    # Verify each trend item has required fields
    if result.trends:
        trend = result.trends[0]
        assert hasattr(trend, 'topic'), "Trend missing 'topic'"
        assert hasattr(trend, 'volume'), "Trend missing 'volume'"
        assert hasattr(trend, 'sentiment'), "Trend missing 'sentiment'"
        assert hasattr(trend, 'sources'), "Trend missing 'sources'"
        assert hasattr(trend, 'confidence_score'), "Trend missing 'confidence_score'"
    
    print("✅ API contract test passed!")

def test_trend_research_validation():
    """Test that invalid inputs are properly rejected."""
    api = TrendResearchAPI()
    
    test_cases = [
        ({"niche": "ai-education"}, "Missing region", True),
        ({"niche": 123, "region": "US"}, "Wrong type for niche", False),
        ({}, "Empty input", False),
        ({"niche": "test", "region": "US", "max_results": 0}, "max_results too small", False),
        ({"niche": "test", "region": "US", "max_results": 101}, "max_results too large", False),
        ({"niche": "test", "region": "US", "timeframe": "30d", "max_results": 10}, "Valid input", True),
    ]
    
    for input_data, description, should_validate in test_cases:
        is_valid = api.validate_input(input_data)
        
        if should_validate:
            assert is_valid, f"Should validate: {description}"
        else:
            assert not is_valid, f"Should not validate: {description}"
    
    print("✅ Validation test passed!")

def test_trend_research_functionality():
    """Test actual trend research functionality."""
    api = TrendResearchAPI()
    
    # Test with known niche
    input_data = {
        "niche": "ai-education",
        "region": "global",
        "timeframe": "7d",
        "max_results": 1
    }
    
    result = api.research_trends(input_data)
    
    # Should get at least one trend for ai-education
    assert len(result.trends) > 0, "Should return trends for ai-education niche"
    
    # Test max_results limit
    input_data["max_results"] = 1
    result = api.research_trends(input_data)
    assert len(result.trends) <= 1, "Should respect max_results limit"
    
    # Test with unknown niche
    input_data["niche"] = "unknown-niche"
    result = api.research_trends(input_data)
    assert len(result.trends) == 0, "Should return empty for unknown niche"
    
    print("✅ Functionality test passed!")

if __name__ == "__main__":
    print("\n=== Running Trend Research Tests ===\n")
    
    try:
        test_trend_research_api_contract()
    except Exception as e:
        print(f"❌ API contract test failed: {e}")
    
    try:
        test_trend_research_validation()
    except Exception as e:
        print(f"❌ Validation test failed: {e}")
    
    try:
        test_trend_research_functionality()
    except Exception as e:
        print(f"❌ Functionality test failed: {e}")
    
    print("\n=== Tests Complete ===\n")