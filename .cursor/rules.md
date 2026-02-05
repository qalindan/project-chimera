# Project Chimera - AI Development Rules

## 🎯 PROJECT CONTEXT
This is Project Chimera - an autonomous AI influencer system. We're building a factory that creates AI agents who research trends, generate content, and manage engagement autonomously.

## ⚡ PRIME DIRECTIVE
**NEVER** generate implementation code without first checking the `specs/` directory. All code must align with the specifications defined in:
- `specs/_meta.md` - Vision and constraints
- `specs/functional.md` - User stories
- `specs/technical.md` - API contracts and database schema
- `specs/openclaw_integration.md` - Agent network protocols

## 📋 DEVELOPMENT PROCESS
1. **READ FIRST**: Always read the relevant spec file before coding
2. **PLAN**: Explain your approach before writing any code
3. **TEST-FIRST**: Create failing tests before implementation
4. **SPEC-ALIGNED**: Every function must match the API contracts in `technical.md`

## 🏗️ ARCHITECTURAL CONSTRAINTS
- Use **FastRender Swarm** pattern (Planner → Worker → Judge)
- All external APIs go through **MCP servers** (not direct calls)
- Database: **PostgreSQL** (transactions) + **Weaviate** (memory) + **Redis** (cache)
- **Confidence-based HITL**: <0.7 confidence goes to human review
- **Economic agency**: All agents have Coinbase AgentKit wallets

## 🔧 TOOLING GUIDANCE
- Use **MCP servers** for external services
- Structure code in **skills/** directory
- Follow **FastAPI** patterns for APIs
- Use **Pydantic** for data validation
- Implement proper **error handling** and **logging**

## 🚫 FORBIDDEN
- No hardcoded API keys in source code
- No direct API calls bypassing MCP
- No code without corresponding tests
- No deviations from spec without approval