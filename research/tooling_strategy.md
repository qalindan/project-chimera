# Tooling Strategy - Developer vs Runtime Tools

## 🛠️ Developer Tools (MCP Servers for Development)

### 1. Git MCP Server
- **Purpose**: Version control operations
- **Use**: Commit, push, create branches via AI
- **Configuration**: Already available in Cursor/Claude

### 2. Filesystem MCP Server
- **Purpose**: File operations and editing
- **Use**: Create, read, update files via AI
- **Configuration**: Built into most AI IDEs

### 3. Database MCP Server
- **Purpose**: Direct database operations during development
- **Use**: Test queries, inspect schemas
- **Setup**: PostgreSQL MCP connector

### 4. Testing MCP Server
- **Purpose**: Run and monitor tests
- **Use**: Execute pytest, view results
- **Setup**: Custom MCP server for test orchestration

## ⚡ Runtime Tools (Agent Skills - What Chimera Agents Use)

### Category 1: Data Collection Skills
- `skill_trend_research` - Fetch trends
- `skill_audience_analysis` - Analyze followers
- `skill_competitor_monitoring` - Track competitors

### Category 2: Content Creation Skills
- `skill_content_generation` - Create scripts
- `skill_thumbnail_design` - Design thumbnails
- `skill_video_editing` - Edit videos (via API)

### Category 3: Publishing Skills
- `skill_social_posting` - Post to platforms
- `skill_engagement` - Reply to comments
- `skill_scheduling` - Schedule content

### Category 4: Economic Skills
- `skill_wallet_management` - Handle transactions
- `skill_revenue_tracking` - Track earnings
- `skill_expense_management` - Manage costs

## 🔗 MCP Server Strategy
Each external service gets its own MCP server:
- `twitter-mcp`, `youtube-mcp`, `tiktok-mcp`
- `trends-mcp` (aggregates Google Trends, Twitter trends)
- `coinbase-mcp` (wallet operations)
- `weaviate-mcp` (vector memory operations)

This separation ensures:
1. **Decoupling**: Change Twitter API? Only update `twitter-mcp`
2. **Reusability**: Multiple agents can use same MCP server
3. **Maintainability**: Isolated error handling
4. **Security**: API keys isolated in MCP servers