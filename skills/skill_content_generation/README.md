# Skill: Content Generation

## 🎬 Description
Generates video scripts, thumbnails, and posting strategies based on trending topics.

## 📥 Input Contract
```json
{
  "trend_data": {
    "topic": "string",
    "volume": "number",
    "sentiment": "string"
  },
  "content_type": "string ('video', 'short', 'post')",
  "target_platform": "string ('youtube', 'tiktok', 'twitter')",
  "target_duration": "string (e.g., '60s', '3min')",
  "tone": "string ('professional', 'casual', 'entertaining')"
}
```
### 📤 Output Contract
```json
{
  "content_package": {
    "script": "string (full video script)",
    "title": "string (catchy title)",
    "description": "string (platform description)",
    "hashtags": ["string (relevant hashtags)"],
    "thumbnail_prompt": "string (DALL-E/Stable Diffusion prompt)",
    "posting_schedule": {
      "best_times": ["string (ISO timestamps)"],
      "platform_specific_notes": "string"
    }
  },
  "confidence_score": "number (0-1)",
  "estimated_engagement": "number (0-1)",
  "content_id": "string (UUID)"
}
```
### 🔧 Implementation Notes
- Use AI models via MCP servers

- Follow platform-specific best practices

- Include call-to-action in scripts

- Generate multiple title options