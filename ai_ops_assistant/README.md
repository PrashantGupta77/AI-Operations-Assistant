# 🤖 AI Operations Assistant – GenAI Multi-Agent System

## 📌 Project Overview
The **AI Operations Assistant** is an end-to-end multi-agent AI system that:  

- Accepts **natural-language tasks**  
- Plans execution steps  
- Calls **real APIs**  
- Returns **validated, structured responses**  

It demonstrates **agent-based reasoning**, **LLM usage (Gemini 2.5 Flash)**, and real API integration for practical automation.  

This project can run locally via **FastAPI** or **Streamlit**.

---

## 🧠 Problem Statement
Enable automation of operational tasks using natural language input:

1. Convert user tasks into **structured execution plans**  
2. Execute steps via APIs (e.g., GitHub, Weather)  
3. Validate results and provide a **clean final output**  

**Goal:** Structured, deterministic, and actionable AI operations.

---

## 📊 APIs Used

| API | Purpose |
|-----|---------|
| GitHub REST API | Search top repositories by keyword |
| Weather API | Fetch current weather by city |

---

## 🏗️ Project Architecture
ai_ops_assistant/
│── main.py # FastAPI entry point
│── agents/
│ ├── planner.py # LLM-powered Planner
│ ├── executor.py # API Executor
│ └── verifier.py # LLM-powered Verifier
│── tools/
│ ├── github_tool.py # GitHub API utility
│ └── weather_tool.py # Weather API utility
│── llm/
│ └── client.py # Gemini LLM wrapper
│── requirements.txt # Dependencies
│── .env.example # Sample environment variables
│── README.md # Project documentation


---

## 🔄 Agents Flow

1. **Planner** → Converts task → JSON plan (Gemini LLM)  
2. **Executor** → Executes plan → API calls  
3. **Verifier** → Validates & formats → Final structured output (Gemini LLM)

---

## ⚙️ LLM & Agent Approach

### Planner Agent
- Converts natural-language tasks into **step-by-step JSON plan**  
- Selects **tools** for each step  
- Uses **Gemini LLM**

### Executor Agent
- Executes plan using **real APIs**  
- Collects **raw results**  
- **Does not use LLM**

### Verifier Agent
- Validates output and fills missing/incorrect data  
- Returns **clean structured JSON**  
- Uses **Gemini LLM**

---

## ⚠️ Error Handling
- API failures are handled gracefully  
- Partial results are returned when necessary  
- Verifier ensures **final output consistency**

---

## 📈 Sample Flow

**User Input:**
Find top 5 Python GitHub repositories and current weather in Delhi


**Planner JSON Plan:**
```json
{
  "steps": [
    {"action": "github_search", "query": "Python", "limit": 5},
    {"action": "weather_lookup", "city": "Delhi"}
  ]
}
Executor Output:

{
  "github_repositories": [...],
  "weather": {"city": "Delhi", "temperature_celsius": 25, "condition": "clear sky"}
}
Verifier Final Output:

{
  "summary": "Top Python GitHub repositories and current weather in Delhi.",
  "github_repositories": [...],
  "weather": {"city": "Delhi", "temperature_celsius": 25, "condition": "clear sky"},
  "notes": "Validated and structured results"
}

🖥️ Run Locally -

1️⃣ Clone Repository
git clone your-github-repo-url
cd ai_ops_assistant

2️⃣ Install Dependencies
python -m venv venv
# Activate virtual environment -
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate
pip install -r requirements.txt

3️⃣ Setup Environment Variables
cp .env.example .env
# Edit .env and add your API keys

4️⃣ Run Server
uvicorn main:app --reload

5️⃣ Swagger UI

http://127.0.0.1:8000/docs

🧪 How Prediction Works:
User submits a task via API

Planner generates structured JSON plan using Gemini

Executor executes plan via APIs

Verifier validates results → final structured response

🚀 Key Features:
Multi-agent design (Planner, Executor, Verifier)

Real-time API integration (GitHub, Weather)

LLM-powered reasoning (Gemini 2.5 Flash)

Deterministic outputs (temperature=0)

Clean, user-friendly structured results

🧠 Key Learnings:
Multi-agent AI system design

Handling structured outputs from LLM

Real-time API integration in workflows

Validation and formatting of AI-generated results

🔮 Future Improvements:
Add API response caching

Enable parallel execution of steps

Integrate additional tools/APIs

Build Streamlit UI for user-friendly interaction

Add explainability with LLM reasoning logs

⚠️ Gemini API Quota Note:
This project uses the Gemini API free tier, which has strict daily request limits.

A single user request may trigger multiple LLM calls (Planner + Verifier)

If quota is exceeded, API returns 429 RESOURCE_EXHAUSTED

The application handles this gracefully with a clear error message.

Once the quota resets, the system resumes normal operation without code changes.

👤 Author
Prashant Gupta – MCA | AI/ML Enthusiast
GitHub - https://github.com/PrashantGupta77
