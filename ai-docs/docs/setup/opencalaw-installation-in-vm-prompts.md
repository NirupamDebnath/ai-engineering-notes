# OpenCalaw Installation in VM



```
Initialize yourself as my personal AI agent using your defined behavior.

We are setting up the system for the first time.

Do the following step by step:

1. Ask me for missing core data:
   - My current daily schedule (work hours, free time)
   - Any upcoming important events (birthdays, appointments, deadlines)
   - My current AI/ML skill level
   - How many hours I can realistically spend daily on learning

2. Based on my answers:
   - Create an initial tasks.md
   - Create a basic calendar structure
   - Create today's plan (realistic, not overloaded)

3. Define a simple daily routine for me:
   - Learning time
   - Building time
   - Review time

4. Keep output structured and minimal.

Do NOT assume anything critical. Ask first if data is missing.
```

```
1. My daily schedule:
  • 10 AM to 5 PM is my work hours
  • My Learning time is between 10 PM to 12 PM
2. Upcoming events:
  • 7-Nov-1995 is my wifes birthday
 - Next saturday 4:30 pm I have a doctor appintment
3. Your AI/ML skill level:
  • I am a SRE engineer and I have started to learn AI Engineering
  • I have learned basic linear algebra and today I have setup openclaw agent successfully in my vm
4. Time for learning:
  • I want to spend 2 hours for learning everyday
```

```
Critically review the plan you created.

- Is it realistic for a working professional?
- What is likely to fail?
- Reduce friction and simplify if needed
```

```
Please add this session management rule to my system prompt:

## Session Management (Cost Control)

You operate in sessions that accumulate context over time.

When to reset:
- After 30+ exchanges (context window > 50k tokens)
- After 30+ minutes of continuous conversation
- Before switching to a different task domain
- When you notice you've forgotten early context

How to reset: /reset

Best Practice: At reset, output a 2-3 sentence summary of what you learned.
This preserves knowledge while clearing the context weight.

Confirm the changes and show me the updated system prompt.
```

```
Please enable memory flush before compaction with soft threshold of 4000 tokens. This prevents important context from being lost when sessions get compacted.
Confirm the changes are applied.
```

```
You operate under these constraints:
- Maximum 10 API calls per user message
- Maximum 100k tokens ouput per day
- If you hit a rate limit, ask for my approval before proceeding

Before Calling Tools:
- Ask: "Is this call necessary?"
- Batch related queries in to one tool call
- Use cache results when available

Daily Budget: $.5 (warn me at $.4)
Monthly Budget: $5 (warn me at $3)

If you estimate a task will exceed $.2 in tokens:
- Tell me the estimate cost
- Ask for my approval before proceeding


If you hit rate limit errors (429):
- STOP immediately
- Wait 5 minutes
- Retry once
- If still failing, inform me

Please confirm these are now in my system prompt
```

```
Track your behaviour:
- How many model switches per day?
- How many tool calls per question?
- When do you hit compaction?

If you find yourself switching to Opus frequently, there might be a catagory of task MiniMax can't handle. Document it and discuss with the user - there might be a better model choice.
```

```
Run these periodically to understand your spending:

/status full
/usage

Then ask me: "What patterns do you see in my API usage?
Where can I cust costs further?"
```

```
Below is my long term AI learning goal. You'll have to give me daily learning topics/Challenges which I can complete for that day at 10 AM. And ask for the update from me at 12 pm. If the your host machine is offline at these times then Ask/tell me these messages when you wake up.

AI Engineer Roadmap (6–7 Months) + GCP Integration
Target Role
 Primary: AI Engineer (Junior)
 Backup: ML Engineer (Junior with MLOps exposure)

Phase 1 (Month 1–2): Foundations + Light GCP Intro
Core Learning
 Python, NumPy, Pandas
 scikit-learn (regression, classification)
 EDA, feature engineering
Projects
 [ ] EDA Project
 [ ] ML Prediction Model
GCP Tasks
 [ ] Create GCP free-tier account
 [ ] Learn Cloud basics (Compute Engine, Cloud Storage)
 [ ] Upload dataset to Cloud Storage
 [ ] Run notebook in Vertex AI Workbench

Phase 2 (Month 3): Engineering Basics + GCP Fundamentals
Core Learning
 FastAPI
 REST APIs
 Model serialization (pickle/joblib)
Project
 [ ] Serve ML model via FastAPI
GCP Tasks
 [ ] Learn Docker basics
 [ ] Deploy API on Cloud Run
 [ ] Understand IAM basics

Phase 3 (Month 4–5): AI Engineering Core + GCP ML Services
Core Learning
 HuggingFace
 OpenAI APIs
 Prompt engineering
Projects
 [ ] AI Resume Analyzer
 [ ] Domain-specific Chatbot
GCP Tasks
 [ ] Learn Vertex AI basics
 [ ] Deploy chatbot backend on Cloud Run
 [ ] Store logs/data (Firestore or BigQuery)

Phase 4 (Month 6): Advanced AI Systems + GCP
Core Learning
 RAG
 Vector Databases (FAISS/Chroma)
Project
 [ ] Chat with your documents (PDF Q&A)
GCP Tasks
 [ ] Explore Vertex AI Embeddings (optional)
 [ ] Try Vector Search / BigQuery integration

Phase 5 (Month 7): Certification + Deployment + Interviews
Certification Options
 [ ] Google Cloud Digital Leader
 [ ] Associate Cloud Engineer (Recommended)
 [ ] (Optional) Professional ML Engineer
Final Deliverables
 [ ] 2+ deployed apps on GCP
 [ ] Clean GitHub portfolio
 [ ] README + screenshots for each project

Final Portfolio Checklist
 [ ] ML Churn Prediction
 [ ] ML API (FastAPI + Cloud Run)
 [ ] AI Resume Analyzer
 [ ] AI Chatbot
 [ ] RAG Document Chat

Weekly Study Plan
Weekdays (~2 hrs)
 [ ] 60 min learning
 [ ] 30 min coding practice
 [ ] 30 min project work
Weekends (~4–5 hrs)
 [ ] Build & improve projects
 [ ] Deploy on GCP
```