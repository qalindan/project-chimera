# Skill: Social Posting

## 📱 Description
Posts content to social media platforms and engages with audience.

## 📥 Input Contract
```json
{
  "content_package": {
    "script": "string",
    "title": "string",
    "description": "string",
    "hashtags": ["string"]
  },
  "platforms": ["string ('youtube', 'tiktok', 'twitter')"],
  "schedule_time": "string (ISO timestamp, optional)",
  "engagement_settings": {
    "auto_reply": "boolean",
    "reply_tone": "string",
    "monitor_comments": "boolean"
  }
}
```
### 🔧 Implementation Notes
- Use platform-specific MCP servers

- Handle rate limiting and retries

- Schedule posts via queue system

- Track posting success/failure
