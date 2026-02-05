# Project Chimera - Technical Specifications

## API Contracts

### Trend Research API
**Endpoint:** `POST /api/trends/research`
```json
{
  "input": {
    "niche": "string (e.g., 'ai-education')",
    "region": "string (e.g., 'ethiopia')",
    "timeframe": "string (e.g., 'last_7_days')",
    "max_results": "number (default: 10)"
  },
  "output": {
    "trends": [
      {
        "topic": "string",
        "volume": "number",
        "sentiment": "string (positive/negative/neutral)",
        "sources": ["string"],
        "confidence_score": "number (0-1)"
      }
    ]
  }
}
```
### Content Generation API
**Endpoint:** `POST /api/content/ generate`
```json
{
  "input": {
    "trend_topic": "string",
    "content_type": "string (video/shorts/post)",
    "target_platform": "string (youtube/tiktok/twitter)",
    "tone": "string (professional/casual/entertaining)",
    "target_duration": "string (optional, e.g., '60s', '3min')"
  },
  "output": {
    "content": {
      "script": "string",
      "title": "string",
      "description": "string",
      "hashtags": ["string"],
      "thumbnail_prompt": "string"
    },
    "confidence_score": "number (0-1)",
    "content_id": "string (UUID)"
  }
}
```
### Social Posting API
**Endpoint:** `POST /api/content/publish`
```json
{
  "input": {
    "content_id": "string",
    "platforms": ["string"],
    "schedule_time": "string (ISO timestamp, optional)",
    "engagement_settings": {
      "auto_reply": "boolean",
      "reply_tone": "string"
    }
  },
  "output": {
    "results": [
      {
        "platform": "string",
        "post_url": "string",
        "success": "boolean",
        "posted_at": "string"
      }
    ]
  }
}
```
### Database Schema API
**Tables:** 
**1.Agents**
```sql
CREATE TABLE agents (
    id UUID PRIMARY KEY,
    name VARCHAR(100),
    niche VARCHAR(100),
    wallet_address VARCHAR(255),
    created_at TIMESTAMP,
    status VARCHAR(50)  -- 'active', 'paused', 'training'
);
```
**2.content_posts**
```sql
CREATE TABLE content_posts (
    id UUID PRIMARY KEY,
    agent_id UUID REFERENCES agents(id),
    platform VARCHAR(50),  -- 'youtube', 'tiktok', 'twitter'
    content_url VARCHAR(500),
    posted_at TIMESTAMP,
    engagement_metrics JSONB,  -- {likes: 100, comments: 20, shares: 5}
    revenue DECIMAL(10,2)
);
```
**3.financial_transactions**
```sql
CREATE TABLE financial_transactions (
    id UUID PRIMARY KEY,
    agent_id UUID REFERENCES agents(id),
    amount DECIMAL(10,2),
    transaction_type VARCHAR(50),  -- 'earning', 'expense', 'transfer'
    description TEXT,
    timestamp TIMESTAMP,
    on_chain_tx_hash VARCHAR(255)
);
```
### MCP Servers Required
1.**`twitter-mcp`** - Post to Twitter/X

2.**`youtube-mcp`** - Upload to YouTube

3.**`tiktok-mcp`** - Post to TikTok

4.**`trends-mcp`**- Fetch trending topics

5.**`coinbase-mcp`** - Handle wallet transactions

6.**`weaviate-mcp`** - Semantic memory storage
