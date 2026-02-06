# API Contract Specification

This document defines the JSON schemas and contracts for key agent interactions in Project Chimera. All inputs/outputs are strictly validated to ensure spec alignment and testability.

## 1. Trend Research Task
**Task Type:** `trend_research`  
**Direction:** Planner → Worker

### Request Schema (Input)
```json
{
  "task_id": "string (uuid-v4)",
  "task_type": "trend_research",
  "priority": "string (enum: high | medium | low)",
  "context": {
    "niche": "string (required, e.g. 'ai-education')",
    "region": "string (required, e.g. 'ethiopia', 'global')",
    "timeframe": "string (optional, enum: '1d' | '7d' | '30d', default: '7d')",
    "max_results": "integer (optional, min: 1, max: 100, default: 10)"
  },
  "required_resources": [
    "array of strings (MCP URIs, e.g. 'mcp://news/trends', 'mcp://twitter/trends')"
  ]
}
```
### Response Schema (Output)
```jSON 
{
  "task_id": "string (uuid-v4)",
  "status": "string (enum: complete | failed | low-confidence)",
  "confidence": "number (0.0 to 1.0)",
  "output": {
    "trends": [
      {
        "topic": "string",
        "volume": "number",
        "sentiment": "string (enum: positive | negative | neutral)",
        "sources": ["string"],
        "confidence_score": "number (0.0 to 1.0)"
      }
    ]
  },
  "error": "string (optional, only if status = failed)"
} 
```
### Example Request
```JSON
{
  "task_id": "550e8400-e29b-41d4-a716-446655440000",
  "task_type": "trend_research",
  "priority": "high",
  "context": {
    "niche": "ai-education",
    "region": "global",
    "timeframe": "7d",
    "max_results": 5
  },
  "required_resources": [
    "mcp://news/trends",
    "mcp://twitter/trends"
  ]
}
```
### Example Response
```JSON
{
  "task_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "complete",
  "confidence": 0.92,
  "output": {
    "trends": [
      {
        "topic": "AI-powered personalized learning",
        "volume": 8500,
        "sentiment": "positive",
        "sources": ["Twitter", "Reddit", "Medium"],
        "confidence_score": 0.87
      },
      {
        "topic": "GPT tutors for students",
        "volume": 7200,
        "sentiment": "positive",
        "sources": ["Twitter", "HackerNews"],
        "confidence_score": 0.92
      }
    ]
  }
}
```
### Validation Rules

- Required fields: task_id, task_type, context.niche, context.region
- max_results: 1–100
- timeframe: "1d", "7d", "30d" (or null)
- sentiment: "positive", "negative", "neutral"
- confidence_score: 0.0–1.0
- All numeric values must be valid (no strings)

### Error Responses
```JSON
{
  "task_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "failed",
  "error": "ValidationError",
  "message": "Missing required field: 'region'",
  "details": {
    "field": "context.region",
    "issue": "required"
  }
}
```
### OpenClaw Integration

This contract will be fulfilled via:
- Local mock implementation (development/testing)
- OpenClaw MCP server (production, real-time trends)
- Hybrid fallback (mock if OpenClaw unavailable)
