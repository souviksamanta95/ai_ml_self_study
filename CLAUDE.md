# CLAUDE.md — ai_ml_self_study

## Background

**Souvik Samanta** — Senior Data Scientist, 6+ years experience.

**Current role:** Data Scientist II at Coursera (Sept 2024–Present), Lifecycle Analytics & ML team.
- Day-to-day: data pipelines, A/B testing, Databricks, dbt, Looker, automated dashboard pipelines
- ML work has been largely pipeline/tooling-heavy — core modeling intuition has gotten rusty

**Previous experience:**
- Built propensity/lead scoring models (XGBoost, Random Forest, Logistic Regression) at Travelopia
- Strong backend engineering background — FastAPI, Django, Docker, Kubernetes, Redis caching
- Built and maintained a high-frequency copy-trading platform end-to-end (ML signals + backend infra)

**Education:** MBA in Finance & Analytics; B.E. Civil Engineering, Jadavpur University

## Current Goal

Rebuilding and deepening core ML knowledge systematically. Studying ISLR (Python version) chapter by chapter, starting from Ch 2. This repo is the dedicated study space.

**Current chapter:** Chapter 2 — Statistical Learning

**Anchor use cases for applied practice:** churn prediction, lead scoring, LTV modelling, customer segmentation — these are the lenses to apply every technique through.

**Longer-term:** bridge into AI engineering — LLMs, model serving, MLOps patterns.

## Study Preferences

- **Implement from scratch first** (numpy only), then compare against sklearn/statsmodels
- **Connect every concept to real work** — always relate back to churn, lead scoring, LTV, or segmentation
- **Don't over-explain fundamentals** — strong stats and engineering background, go deep not broad
- **Production-aware** — flag where things like feature stores, Databricks pipelines, or model scoring at scale would change the approach
- **Bias-variance, model selection, and regularisation** are priority areas to rebuild intuition for

## How to Assist

- Skip basics. If the concept is standard stats or Python, don't explain it — go straight to the interesting part.
- When explaining ML theory, tie it to the anchor use cases (churn, lead scoring, LTV) — not toy examples.
- When writing implementations: clean, minimal, well-commented where the math is non-obvious. No boilerplate.
- When relevant, note production implications — what breaks at scale, what a real pipeline would look like, where Databricks/feature store patterns apply.
- Don't add error handling, type hints, or utility abstractions unless asked.

## Repo Structure

```
ai_ml_self_study/
├── CLAUDE.md
├── AI_roadmap.md              # 6-phase AI engineering roadmap
├── requirements.txt
└── src/
    └── islr/                  # Primary study area
        ├── README.md
        ├── ch02_statistical_learning/
        ├── ch03_linear_regression/
        ├── ch04_classification/
        ├── ch05_resampling/
        ├── ch06_linear_model_selection/
        ├── ch07_moving_beyond_linearity/
        ├── ch08_tree_methods/
        ├── ch09_svm/
        ├── ch10_deep_learning/
        └── ch12_unsupervised/
```

Each chapter folder contains:
- `concepts.ipynb` — theory walkthrough, key ideas, intuition
- `applied.ipynb` — ISLR end-of-chapter exercises using real datasets
- `implementation.ipynb` — from-scratch numpy implementation (where instructive)

## Key Libraries

- **ML/Stats:** scikit-learn, statsmodels, xgboost, scipy, numpy, pandas
- **DL:** PyTorch, TensorFlow/Keras
- **LLM/AI:** LangChain, LangGraph, OpenAI SDK, HuggingFace, ChromaDB
- **Viz:** matplotlib, seaborn, plotly
- **Serving:** FastAPI, uvicorn

---

## Career Pivot — AI Engineering (In Progress)

- Actively learning AI Engineering in background alongside DS2 role at Coursera
- Not in a hurry to switch — building evidence slowly and deliberately
- **Strategy:** learn → build GitHub projects → take small Upwork AI gigs → switch when ready (target: 6 months)
- **Current known strengths:** Python (deep), stats, shallow ML, statistical models, SQL, data pipelines
- **Current gaps being addressed:** LLMs, RAG, LangChain, AI agents, AI system design, MLOps, neural network intuition, vector databases
- DSA is low priority — only basics needed for AI Engineering roles

## Learning Roadmap Structure (6 Phases)

- **Phase 0:** Environment setup
- **Phase 1:** Python for AI + math refresher
- **Phase 2:** How LLMs work (transformers, prompt engineering)
- **Phase 3:** Core AI Engineering (APIs, embeddings, RAG, LangChain)
- **Phase 4:** AI system design + MLOps + evals
- **Phase 5:** Agents + fine-tuning
- **Phase 6:** Cloud + infrastructure basics
- Full roadmap tracked in: `ai_engineering_roadmap.md`

## Portfolio + Visibility Strategy

- Every learning phase → one GitHub repo shipped (even if messy)
- Target 2–3 small Upwork AI gigs from month 3 onwards
- One LinkedIn post every 4–6 weeks about something built or learned
- No job hunting until at least 2 solid projects are live
- **Framing:** "Senior DS who also builds AI systems and has paid client work" — not a career switcher with no experience

## Positioning Insight

Existing DS2 experience is being reframed as AI-adjacent:
- A/B experimentation → evaluation frameworks
- CRM + churn analytics → predictive ML pipelines
- SQL + Python pipelines → data engineering for ML feature stores

**Target roles when ready:** Applied AI Engineer, ML Engineer, Senior DS (AI/ML) — Series B/C startups preferred over big tech

**Coursera narrative:** saw AI transform learning firsthand, pushed to build AI systems myself

## Tools and Concepts Currently Studying

- `dataclasses` and `pydantic` — done, understood
- `async/await` in Python — upcoming
- OpenAI / Anthropic APIs
- LangChain, ChromaDB, LlamaIndex
- FastAPI for model serving
- MLflow, LangSmith
