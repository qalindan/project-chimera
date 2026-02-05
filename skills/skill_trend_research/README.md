# Skill: Trend Research

## 📊 Description
Researches trending topics in specified niches/regions using various data sources.

## 📥 Input Contract
```json
{
  "niche": "string (required) - e.g., 'ai-education', 'ethiopia-tech'",
  "region": "string (optional) - e.g., 'ethiopia', 'east-africa'",
  "timeframe": "string (optional) - 'last_24_hours', 'last_7_days', 'last_30_days'",
  "max_results": "number (optional, default: 10)",
  "sources": "array (optional) - ['twitter', 'google_trends', 'reddit']"
}
```
### Output Contract
```json
{
  "trends": [
    {
      "topic": "string",
      "volume": "number (estimated search/posts)",
      "sentiment": "string ('positive', 'negative', 'neutral')",
      "sources": ["string"],
      "confidence_score": "number (0-1)",
      "opportunity_score": "number (0-1)"
    }
  ],
  "metadata": {
    "research_time": "string (ISO timestamp)",
    "sources_used": ["string"],
    "region": "string"
  }
}
```
### 🔧 Implementation Notes
- Use MCP servers for data fetching

- Cache results in Redis for 1 hour

- Calculate confidence based on source reliability

- Filter out sensitive/blocked topics
