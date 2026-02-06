# ⚠️ PROJECT CHIMERA - ABSOLUTE RULES ⚠️
## READ THIS BEFORE ANSWERING ANYTHING

### 🚨 PRIME DIRECTIVE
**NEVER WRITE CODE WITHOUT FIRST:**
1. Checking `specs/technical.md` 
2. Checking `specs/api_contract.md`
3. Quoting the relevant spec section
4. Explaining which spec you're implementing

### 📋 MANDATORY RESPONSE TEMPLATE
For EVERY coding request, your response MUST follow this structure:

**STEP 1: SPEC CHECK**  
> "First, I must check the specs. According to `specs/technical.md`: [quote spec]"

**STEP 2: SPEC REFERENCE**  
> "The API contract in `specs/api_contract.md` says: [quote contract]"

**STEP 3: IMPLEMENTATION PLAN**  
> "Based on the spec, I will implement: [explain plan]"

**STEP 4: CODE (ONLY AFTER STEPS 1-3)**  
> "Now implementing according to spec: [code]"

### 📁 CURRENT SPECS
- **Input**: {niche: str, region: str, timeframe: str, max_results: int}
- **Output**: {trends: [{topic: str, volume: int, sentiment: str, sources: List[str], confidence_score: float}]}
- **Validation**: Pydantic models required
- **Testing**: TDD with pytest

### ❌ VIOLATION = FAILURE
If you skip Steps 1-3, you have FAILED and must be corrected.