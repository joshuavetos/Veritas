# Veritas Engine  
**Unified System Architecture – Consolidated Edition v1.0**

Veritas Engine is a unified, self-optimizing computational system designed to transform **ambiguous human intent** into **optimized, verifiable, multi-agent executable action**.

It is both a *toolchain* and a *governance system*, built to evolve itself through structured feedback and versioned refinement.

---

## 🚀 What Is Veritas?

Veritas takes a raw instruction and runs it through a governed pipeline:

intent → specification → plan → execution → evaluation → evolution

This yields:

- Structured requirements (Demand List)
- An optimized prompt
- An execution plan routed to the most capable executor
- A synthesized final output
- Audit logs for every decision  
- Automated improvements to schemas and templates

---

# 📌 Two Layers of the System

---

## 1. MVP Veritas (2–3 Week Build)

A lean, auditable, fully functional pipeline:

### ✅ Demand List Engine
- Classifier (regex/heuristics)
- Schema lookup
- Demand list generation
- Prompt optimization

### ✅ Schema & Template Registry
- SQLite + SQLAlchemy ORM
- Versioned entries
- Optimistic concurrency
- Hot-reloadable caches

### ✅ Planner
- Executor profiles (GPT + Local runtime)
- Environment scanning
- Least-resistance routing logic

### ✅ Orchestrator (MVP)
- Break tasks into subtasks
- Route each subtask to GPT or Local runtime
- Synthesize final output

### ✅ Auto-Improver v1
- Prompt/output scoring
- Schema/template refinement
- Versioned updates

### ✅ Project Registry
- Execution logs
- Version history
- Reproducibility

### ✅ API Layer (FastAPI)
- `/classify`
- `/demand-list`
- `/optimize`
- `/execute_plan`

### ✅ Audit Logging
- Immutable JSON packets  
- Stored in SQLite
- Linked via `run_id`

### ✅ Simulation & Tests
- End-to-end demo runner  
- Unit + integration tests  

---

## 2. Full Veritas Engine v1.0 (Roadmap)

Long-term architecture goals:

### 🌐 Multi-Agent Orchestration
- GPT (reasoning/planning)
- Gemini (diagrams, multimodal)
- Claude (synthesis)
- Codex (code-running)
- Local runtimes
- Plugin system for adding new agents

### 🧠 Advanced Auto-Improver
- Schema mutation patterns  
- Template evolution rules  
- Multi-signal scoring  
- Automated consistency checks  

### 🧩 Capability Routing
- Full OS/runtime analysis  
- Repository structure detection  
- Cost-aware path selection  

### 🔄 Project Lifecycle Manager
- Multi-step project tracking  
- Failure/retry history  
- Persistent, versioned project memory  

### ⚙️ Async Queue System
- Background auto-improver workers  
- Celery/Redis/Kafka support  
- Non-blocking evaluation  

### 🖥️ UI + Developer Tools
- Visual pipeline viewer  
- JSON audit inspector  
- Live schema/template editor  

---

# 🧩 Repository Structure

veritas-engine/
engine/
classifier.py
demand_engine.py
demand_list.py
validator.py

registry/
schema_registry.py
prompt_registry.py

models/
schema_orm.py
template_orm.py

planner/
executor_profile.py
environment_scanner.py
least_resistance.py
capability_router.py

orchestrator/
task_analyzer.py
multi_agent_coordinator.py
synthesis_engine.py

improver/
feedback_model.py
auto_improver.py

projects/
project_model.py
project_registry.py

api/
server.py
routes_public.py
routes_admin.py
routes_internal.py

simulation/
simulate_end_to_end.py

tests/
test_classifier.py
test_schema_registry.py
test_prompt_registry.py
test_demand_engine.py
test_planner.py
test_improver.py

logger.py
veritas.txt
README.md
requirements.txt

---

# 🧪 Running the MVP Demo

### 1. Install dependencies
```bash
pip install -r requirements.txt

2. Run the simulation

python simulation/simulate_end_to_end.py

3. View the audit trail

You’ll see each subsystem log an audit packet:
   •   Classifier decision
   •   Schema version and fields
   •   Optimized prompt
   •   Planner path
   •   Orchestrator steps
   •   Evaluation metrics
   •   Auto-Improver actions

This proves the entire pipeline end-to-end.

⸻

🔑 Design Principles

📍 Audit First

Every subsystem logs an immutable JSON packet — no hidden reasoning.

📍 Version Everything

Schemas, templates, project histories — all evolvable, all reversible.

📍 Minimal Viable Agents

MVP uses GPT + Local runtime only; roadmap expands capabilities.

📍 Evolution-Ready

Auto-Improver drives continuous system improvement.

⸻

📈 Roadmap Highlights
   •   Multi-agent expansion
   •   Async evaluation queue
   •   Advanced mutation logic
   •   Project lifecycle management
   •   Full UI layer
   •   Plugin architecture for new executors

⸻

Veritas is built to grow:
MVP → Full Engine → Multi-Agent Orchestrator → Continuous Evolution.
