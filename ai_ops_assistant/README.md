# 🤖 AI Operations Assistant – GenAI Multi-Agent System

<p align="center">
  <img src="https://img.shields.io/badge/LLM-Gemini%202.5%20Flash-blueviolet" />
  <img src="https://img.shields.io/badge/Architecture-Multi--Agent-success" />
  <img src="https://img.shields.io/badge/APIs-GitHub%20%7C%20Weather-orange" />
  <img src="https://img.shields.io/badge/Run%20Locally-FastAPI-blue" />
</p>

---

## 📌 Project Overview

The **AI Operations Assistant** is an end-to-end **multi-agent AI system** that:

- Accepts **natural-language tasks**
- Plans execution steps automatically
- Calls **real third-party APIs**
- Returns **validated, structured responses**

It demonstrates **agent-based reasoning**, **LLM usage (Gemini 2.5 Flash)**, and real API integration for practical automation.

✅ Runs locally via **FastAPI** 

---

## 🧠 Problem Statement

Enable automation of operational tasks using natural language input:

1. Convert user tasks into **structured execution plans**
2. Execute steps via APIs (e.g., GitHub, Weather)
3. Validate results and return a **clean final output**

🎯 **Goal:** Structured, deterministic, and actionable AI operations.

---

## 📊 APIs Used

| API | Purpose |
|-----|--------|
| **GitHub REST API** | Search top repositories by keyword |
| **Weather API** | Fetch current weather by city |

---

## 🏗️ Project Architecture

```text
ai_ops_assistant/
│── main.py                  # FastAPI entry point
│
├── agents/
│   ├── planner.py           # LLM-powered Planner
│   ├── executor.py          # API Executor
│   └── verifier.py          # LLM-powered Verifier
│
├── tools/
│   ├── github_tool.py       # GitHub API utility
│   └── weather_tool.py      # Weather API utility
│
├── llm/
│   └── client.py            # Gemini LLM wrapper
│
├── requirements.txt
├── .env.example
└── README.md

🔄 Agents Flow:

User Task
   ↓
Planner Agent (LLM)
   ↓
Structured JSON Plan
   ↓
Executor Agent (APIs)
   ↓
Raw Results
   ↓
Verifier Agent (LLM)
   ↓
Validated Final Output


⚙️ LLM & Agent Responsibilities:
🧠 Planner Agent -
Converts natural-language input into a step-by-step JSON plan

Selects appropriate tools for each step

Uses Gemini 2.5 Flash

⚙️ Executor Agent -
Executes the planner’s steps using real APIs

Collects raw responses

❌ Does not use any LLM (fully deterministic)

✅ Verifier Agent -
Validates completeness and correctness of results

Fixes missing or inconsistent data

Returns clean, structured JSON

Uses Gemini 2.5 Flash

⚠️ Error Handling:
API failures are handled gracefully

Partial results are returned when needed

Verifier ensures final output consistency

No hallucinated or hard-coded responses

📈 Sample Execution Flow:
🔹 User Input
Find top 5 Python GitHub repositories and current weather in Delhi
🔹 Planner JSON Plan
{
  "steps": [
    { "action": "github_search", "query": "Python", "limit": 5 },
    { "action": "weather_lookup", "city": "Delhi" }
  ]
}
🔹 Executor Output
{
  "github_repositories": [...],
  "weather": {
    "city": "Delhi",
    "temperature_celsius": 25,
    "condition": "clear sky"
  }
}
🔹 Verifier Final Output
{
  "summary": "Top Python GitHub repositories and current weather in Delhi",
  "github_repositories": [...],
  "weather": {
    "city": "Delhi",
    "temperature_celsius": 25,
    "condition": "clear sky"
  },
  "notes": "Validated and structured results"
}


🧪 Example Prompts -
Use the following prompts to test all core capabilities:

1- GitHub + Weather

Find the top 5 Python GitHub repositories and the current weather in Delhi.

2- Single API Tool

Show the top 3 trending JavaScript repositories on GitHub.

3- Weather Lookup

What is the current weather in Mumbai?

4- Multi-Step Reasoning

Find popular ML repositories on GitHub and check today’s weather in Bangalore.

5- Edge Case Handling

Get the weather for an unknown city and list top GitHub repositories for AI.


▶️ Run Locally
1️⃣ Clone Repository
git clone https://github.com/PrashantGupta77/AI-Operations-Assistant.git
cd ai_ops_assistant

2️⃣ Install Dependencies
python -m venv venv

source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt

3️⃣ Setup Environment Variables
cp .env.example .env
Add your API keys inside .env.


4️⃣ Run Server
uvicorn main:app --reload

5️⃣ Swagger UI
http://127.0.0.1:8000/docs

🚀 Key Features
✅ Multi-agent design (Planner, Executor, Verifier)

✅ Real-time API integration

✅ LLM-powered structured reasoning

✅ Deterministic execution (temperature = 0)

✅ Clean, validated final responses

⚠️ Gemini API Quota Note
Uses Gemini free tier

One request may trigger multiple LLM calls

On quota exhaustion:

API returns 429 RESOURCE_EXHAUSTED

System fails gracefully with clear messaging

Automatically resumes after quota reset

🔮 Future Improvements:
API response caching

Parallel step execution

Additional tools & integrations

Streamlit UI

Agent reasoning logs for explainability

👤 Author
Prashant Gupta
🎓 MCA | AI / ML Enthusiast
🔗 GitHub: https://github.com/PrashantGupta77

