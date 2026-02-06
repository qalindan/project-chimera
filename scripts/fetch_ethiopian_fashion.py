"""Runner to fetch Ethiopian fashion trends using the TrendResearchAPI."""
import json
import sys
import os

# Ensure project root is on path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from research.trend_research import TrendResearchAPI


def main():
    api = TrendResearchAPI()
    result = api.fetch_ethiopian_fashion(region="Africa", timeframe="7d", max_results=10)

    print(json.dumps({"trends": [t.dict() for t in result.trends]}, indent=2))


if __name__ == "__main__":
    main()
