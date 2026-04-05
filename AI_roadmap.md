# 🤖 AI Engineering — Beginner to Job-Ready Roadmap
> **Owner:** Souvik Samanta  
> **Started:** April 2026  
> **Goal:** Transition into AI Engineer / Applied AI Engineer roles  
> **Approach:** Part-time (~8–10 hrs/week alongside full-time job)  
> **Estimated Timeline:** 5–6 months to job-ready

---

## How to Use This File
- Work through phases **sequentially**
- Check off items as you complete them `[x]`
- Add notes/links under each item as you go
- Commit this file to your repo and update it weekly

---

## 📦 Phase 0 — Environment Setup *(Week 1)*
> Get your machine ready before anything else.

- [ ] Install Python 3.11+ and set up a clean virtual environment (`venv` or `conda`)
- [ ] Install VS Code + Python extension + Jupyter extension
- [ ] Create a GitHub repo: `ai-engineering-journey` — this is your portfolio base
- [ ] Set up a free account on: Hugging Face, OpenAI (or Gemini), LangSmith
- [ ] Install core libraries: `pip install openai langchain chromadb pandas numpy jupyter`
- [ ] Read: [What is an AI Engineer?](https://www.latent.space/p/ai-engineer) — Latent Space blog post (15 min)

---

## 📐 Phase 1 — Python & Math Refresher *(Weeks 1–2)*
> You already know Python well — this phase is just plugging the AI-specific gaps.

### Python for AI
- [ ] Understand Python `dataclasses`, `pydantic` models (used everywhere in LLM tooling)
- [ ] Get comfortable with `async/await` in Python (LLM APIs are async-heavy)
- [ ] Learn Python type hints properly — `List`, `Dict`, `Optional`, `Union`
- [ ] Practice writing clean, modular Python with functions and classes (not just notebooks)

### Math You Actually Need
- [ ] Linear Algebra basics: vectors, matrices, dot products, cosine similarity
  - Resource: [3Blue1Brown — Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) (YouTube, free)
- [ ] Probability basics: distributions, Bayes theorem, conditional probability
- [ ] Understand what a gradient is (intuition, not derivation) — needed to understand training
- [ ] ❌ Skip: Calculus derivations, eigenvalues deep dive, advanced stats — not needed yet

---

## 🧠 Phase 2 — How LLMs Actually Work *(Weeks 2–5)*
> This is the most important phase. Take your time here.

### Neural Network Intuition
- [ ] Watch: [Andrej Karpathy — Neural Networks: Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) (YouTube, free)
  - Priority episodes: makemore series + GPT from scratch
  - Don't skip — this is the best LLM intuition content that exists
- [ ] Understand: what is a neuron, activation function, forward pass, backpropagation (conceptually)
- [ ] Understand: what is a loss function and why it matters

### Transformers & LLMs
- [ ] Read: [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — Jay Alammar (blog)
- [ ] Read: [The Illustrated GPT-2](https://jalammar.github.io/illustrated-gpt2/) — Jay Alammar (blog)
- [ ] Understand: tokens, embeddings, attention mechanism, context window
- [ ] Understand: what "temperature", "top-p", "max tokens" actually do
- [ ] Understand: difference between base model, instruction-tuned model, RLHF
- [ ] Know the major model families: GPT-4o, Claude 3.x, Gemini, Llama 3, Mistral

### Prompt Engineering
- [ ] Read: [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- [ ] Read: [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [ ] Practice: zero-shot, few-shot, chain-of-thought prompting
- [ ] Practice: writing system prompts, user prompts, structured output prompting
- [ ] Learn: what hallucination is and why it happens

---

## 🔨 Phase 3 — Core AI Engineering Skills *(Weeks 5–10)*
> This is where you go from "I understand LLMs" to "I can build with LLMs."

### APIs & SDKs
- [ ] Call the OpenAI (or Anthropic) API directly in Python — no wrappers first
- [ ] Understand: API request structure, roles (system/user/assistant), streaming responses
- [ ] Handle: rate limits, retries, error handling in API calls
- [ ] Build: a simple CLI chatbot using raw API calls

### Embeddings & Vector Search
- [ ] Understand what an embedding is and why it captures "meaning"
- [ ] Understand cosine similarity — how similarity search works
- [ ] Learn: ChromaDB (local) and Pinecone (cloud) — try both
- [ ] Build: embed a set of documents and retrieve the most relevant one for a query
- [ ] Resource: [Embeddings Explained](https://simonwillison.net/2023/Oct/23/embeddings/) — Simon Willison (blog)

### RAG — Retrieval Augmented Generation
- [ ] Understand: what RAG is and why it exists (LLMs don't have your data)
- [ ] Understand: chunking strategies — fixed size, semantic, recursive
- [ ] Build: a basic RAG pipeline from scratch (PDF → chunks → embed → store → retrieve → answer)
- [ ] Learn: LangChain basics — document loaders, text splitters, vector stores, chains
- [ ] Build: a RAG chatbot over your own documents using LangChain + ChromaDB

### LangChain & LlamaIndex
- [ ] Complete: [LangChain Python Docs — Quickstart](https://python.langchain.com/docs/get_started/quickstart)
- [ ] Understand: chains, agents, tools, memory in LangChain
- [ ] Explore: LlamaIndex as an alternative for document-heavy use cases
- [ ] Build: a simple agent that can use a tool (e.g., web search or calculator)

---

## 🏗️ Phase 4 — AI System Design & MLOps *(Weeks 10–16)*
> This separates hobby builders from engineers.

### AI System Design Concepts
- [ ] Read: *Designing Machine Learning Systems* — Chip Huyen (book — buy it, worth it)
- [ ] Understand: latency vs. throughput tradeoffs in LLM systems
- [ ] Understand: caching strategies for LLM responses
- [ ] Understand: when to use RAG vs. fine-tuning vs. prompt engineering
- [ ] Understand: guardrails, content filtering, output validation
- [ ] Learn: how to design a multi-step LLM pipeline (orchestration)

### Serving & Deployment
- [ ] Learn FastAPI — build a REST API that wraps an LLM call
- [ ] Understand: Docker basics — containerize your FastAPI app
- [ ] Deploy: a simple LLM app to a free cloud (Render, Railway, or Hugging Face Spaces)
- [ ] Learn: environment variable management, secrets handling (never hardcode API keys)

### MLOps for AI Engineers
- [ ] Learn: MLflow — experiment tracking, logging metrics, model registry
- [ ] Understand: what model monitoring means in production (drift, quality degradation)
- [ ] Learn: basic CI/CD concepts — GitHub Actions for automated testing/deployment
- [ ] Explore: LangSmith for LLM-specific tracing and evaluation

### Evaluation (Evals)
- [ ] Understand: why evals matter — LLMs are non-deterministic, you need to measure quality
- [ ] Learn: basic eval frameworks — RAGAS (for RAG), LangSmith evals
- [ ] Build: a simple eval suite for your RAG chatbot (faithfulness, relevance, correctness)
- [ ] Read: [How to Evaluate LLM Applications](https://hamel.dev/blog/posts/evals/) — Hamel Husain (blog)

---

## 🤖 Phase 5 — Agents & Advanced Topics *(Weeks 14–20)*
> The frontier of AI Engineering — pick what excites you.

### AI Agents
- [ ] Understand: what an agent is — LLM + tools + memory + loop
- [ ] Learn: ReAct pattern (Reason + Act)
- [ ] Learn: LangGraph — stateful, multi-step agent orchestration
- [ ] Build: a simple research agent that searches the web and summarises findings
- [ ] Explore: multi-agent systems — when and why to use them

### Fine-tuning (Foundations)
- [ ] Understand: when fine-tuning makes sense vs. RAG or prompting
- [ ] Learn: LoRA and QLoRA — parameter-efficient fine-tuning techniques
- [ ] Try: fine-tune a small model (Llama 3.1 8B) on Hugging Face with a free GPU
- [ ] Resource: [Hugging Face PEFT Library Docs](https://huggingface.co/docs/peft)

### Multimodal (Optional but valuable)
- [ ] Understand: vision-language models (GPT-4o, Gemini Vision)
- [ ] Build: a simple image + text input app using a multimodal API
- [ ] Explore: audio/speech models — Whisper for transcription

---

## ☁️ Phase 6 — Cloud & Infrastructure Basics *(Weeks 16–20, parallel)*
> You don't need to be a DevOps engineer — just enough to deploy and not be blocked.

- [ ] Pick one cloud: **AWS** (most jobs) or **GCP** (Coursera likely uses GCP)
- [ ] Learn: S3/GCS — object storage for datasets and model artifacts
- [ ] Learn: EC2/Compute Engine — spin up a GPU instance
- [ ] Learn: Lambda/Cloud Functions — serverless for lightweight LLM endpoints
- [ ] Learn: basic IAM — permissions, roles, service accounts
- [ ] Get certified (optional but helpful): AWS Cloud Practitioner or GCP Associate Cloud Engineer

---

## 🗂️ DSA — Just Enough *(Parallel, low priority)*
> Don't over-invest here. AI Engineering interviews are not LeetCode-heavy.

- [ ] Arrays, strings, hashmaps — basic manipulation
- [ ] Two pointers, sliding window — common patterns
- [ ] Basic recursion
- [ ] BFS/DFS on graphs (useful for agent graph traversal concepts)
- [ ] Practice: 30–40 Easy LeetCode problems, 10–15 Medium — that's enough
- [ ] ❌ Skip: Dynamic programming deep dive, advanced graph algorithms, competitive programming

---

## 📁 Portfolio — Build As You Learn *(Ongoing from Phase 3)*
> Each project should have: a README, a demo, and a "business impact" framing.

### Projects to Build (in order)
- [ ] **Project 1:** RAG chatbot over a dataset you care about (e.g., Coursera course catalog, your own notes)
- [ ] **Project 2:** LLM-powered API — FastAPI + LLM + deployed to cloud
- [ ] **Project 3:** AI Agent — a tool-using agent that solves a real workflow problem
- [ ] **Project 4:** End-to-end ML pipeline — data ingestion → model → serving → monitoring
- [ ] **Project 5 (stretch):** Fine-tuned model for a specific domain task

### Portfolio Hygiene
- [ ] Every project has a clean `README.md` with: problem, approach, demo link, tech stack
- [ ] Write 1 case study per project — business context, decisions made, results measured
- [ ] Keep GitHub profile clean — pinned repos, profile README
- [ ] Optional: write 1 blog post per project (LinkedIn or personal blog)

---

## 📚 Core Resources Master List

| Resource | Type | Priority |
|---|---|---|
| Andrej Karpathy — Neural Networks: Zero to Hero | YouTube | 🔴 Must |
| The Illustrated Transformer — Jay Alammar | Blog | 🔴 Must |
| Anthropic Prompt Engineering Guide | Docs | 🔴 Must |
| Designing Machine Learning Systems — Chip Huyen | Book | 🔴 Must |
| LangChain Python Docs | Docs | 🔴 Must |
| Full Stack LLM Bootcamp — Berkeley | Course (free) | 🟡 High |
| Fast.ai Practical Deep Learning Part 1 | Course (free) | 🟡 High |
| RAGAS — RAG Evaluation Docs | Docs | 🟡 High |
| Hugging Face PEFT Docs | Docs | 🟡 High |
| Simon Willison's Blog | Blog | 🟢 Follow |
| Latent Space Podcast | Podcast | 🟢 Follow |

---

## 🎯 Milestones & Self-Check

| Milestone | Target Week | Done? |
|---|---|---|
| Environment set up, first API call made | Week 1 | [ ] |
| Can explain how a transformer works in plain English | Week 5 | [ ] |
| First RAG chatbot running locally | Week 7 | [ ] |
| First project deployed to cloud | Week 12 | [ ] |
| 3 portfolio projects on GitHub | Week 16 | [ ] |
| First AI Engineering job application sent | Week 18 | [ ] |
| 5 portfolio projects complete | Week 20 | [ ] |

---

## 🗓️ Weekly Review Template
> Paste this each week and fill it in.

```
Week: ___
Hours spent: ___
Completed this week:
- 
- 

Stuck on:
- 

Next week plan:
- 
- 
```

---

## 💡 Mindset Notes
- **Build over consume.** For every 1 hour of tutorial, spend 2 hours building something.
- **Don't wait to feel ready.** Apply from month 4 onwards — imposter syndrome is universal.
- **Your DS background is a moat.** Most AI Engineers can't read data or think about business impact. You can.
- **The field moves fast.** Follow practitioners on X/LinkedIn, not just courses.
- **Ship ugly first.** A deployed mediocre project beats a perfect local one every time.

---

*Last updated: April 2026*