from tools.github_tool import search_repositories
from tools.weather_tool import get_current_weather


class ExecutorAgent:
    def __init__(self, execution_plan: dict):
        self.execution_plan = execution_plan

    def execute(self) -> dict:
        results = {}

        for step in self.execution_plan.get("steps", []):
            action = step.get("action")

            if action == "github_search":
                query = step.get("query")
                limit = step.get("limit", 5)
                results["github_repositories"] = search_repositories(query, limit)

            elif action == "weather_lookup":
                city = step.get("city")
                results["weather"] = get_current_weather(city)

            else:
                raise ValueError(f"Unknown action: {action}")

        return results