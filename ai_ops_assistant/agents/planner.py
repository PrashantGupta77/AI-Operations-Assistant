import json
from llm.client import call_llm


PLANNER_SYSTEM_PROMPT = """
You are a Planner Agent in an AI Operations Assistant.

Your task:
- Convert the user's natural language request into a step-by-step execution plan.
- Choose appropriate tools for each step.
- Output MUST be valid JSON only.
- Do NOT include explanations or extra text.

Available tools:
1. github_search -> search GitHub repositories
   Required fields: query, limit
2. weather_lookup -> get current weather
   Required field: city

JSON format:
{
  "steps": [
    {
      "action": "github_search",
      "query": "python",
      "limit": 5
    },
    {
      "action": "weather_lookup",
      "city": "Delhi"
    }
  ]
}
"""


def create_execution_plan(user_task: str) -> dict:
    response = call_llm(PLANNER_SYSTEM_PROMPT, user_task)

    try:
        start = response.index("{")
        end = response.rindex("}") + 1
        json_text = response[start:end]
        plan = json.loads(json_text)
    except json.JSONDecodeError:
        raise ValueError("Planner Agent failed to return valid JSON.")

    return plan