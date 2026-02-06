import json
from llm.client import call_llm


VERIFIER_SYSTEM_PROMPT = """
You are a Verifier Agent.

Your responsibilities:
- Validate that execution results are complete and correct.
- If any data is missing, mention it clearly.
- Produce a clean, user-friendly, structured final response.
- Output MUST be valid JSON only.

Expected JSON format:
{
  "summary": "...",
  "github_repositories": [...],
  "weather": {...},
  "notes": "..."
}
"""


def verify_execution_results(execution_results: dict) -> dict:
    response = call_llm(VERIFIER_SYSTEM_PROMPT, json.dumps(execution_results))

    try:
        start = response.index("{")
        end = response.rindex("}") + 1
        json_text = response[start:end]
        result = json.loads(json_text)

    except json.JSONDecodeError:
        raise ValueError("Verifier Agent failed to return valid JSON.")

    return result