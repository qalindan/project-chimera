# Architecture Strategy - Project Chimera

## Chosen Agent Pattern
**FastRender Swarm (Planner → Worker → Judge)**  
- Planner: Decomposes high-level goals into executable tasks  
- Worker: Executes atomic tasks in parallel  
- Judge: Validates output for quality, safety, and spec alignment  
Why this pattern? Matches SRS exactly, enables high parallelism, prevents hallucinations via Judge, supports self-healing.

## Human-in-the-Loop Placement
- Position: After Worker output, before commit to global state  
- Mechanism: Judge assigns confidence score → <0.7 escalates to HITL dashboard  
Why here? Prevents low-quality or risky actions from affecting the fleet while keeping high-confidence autonomy intact.

## Database Choice for High-Velocity Video Metadata
- Primary: **PostgreSQL** (transactional integrity, ACID for wallet/campaign data)  
- Secondary: **Weaviate** (vector search for semantic memory, RAG)  
- Cache/Queue: **Redis** (fast task queue, short-term state)  
Why not pure NoSQL? Video metadata needs strong consistency (ownership, payments), but semantic search benefits from vector DB. Hybrid is best.

## Overall Architecture Principles
- Spec-driven: Never write code without ratified specs/
- MCP-first: All external interaction through MCP servers
- Governance-first: Judge + CodeRabbit review on every change
- Economic agency: Coinbase AgentKit wallets from day one