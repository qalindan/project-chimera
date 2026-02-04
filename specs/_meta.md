# Project Chimera - Meta Specification

## Vision
Build an autonomous AI influencer system that researches trends, generates content, and manages engagement at scale without constant human intervention.

## Core Principles
1. **Spec-Driven Development**: No code without ratified specs
2. **Agent Autonomy**: AI agents make decisions within defined bounds
3. **Economic Agency**: Agents have wallets and earn/spend autonomously
4. **Safety by Design**: Human oversight for sensitive content

## Architectural Constraints
- **Pattern**: FastRender Swarm (Planner → Worker → Judge)
- **Databases**: PostgreSQL (transactions), Weaviate (memory), Redis (cache)
- **External APIs**: All through MCP servers
- **HITL**: Confidence-based escalation (<0.7 goes to human review)

## Success Metrics
- Content production rate: 10 posts/day/agent
- Engagement rate: >3% per post
- Autonomous operation: 95% without human intervention
- Revenue generation: $100/month/agent (testnet)

## Non-Negotiables
1. No hardcoded API keys in source code
2. All agent actions must be traceable via MCP
3. Financial transactions require >0.8 confidence
4. Sensitive topics (politics, health, finance) require human review