from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from agents.planner import create_execution_plan
from agents.executor import ExecutorAgent
from agents.verifier import verify_execution_results


app = FastAPI(
    title="AI Operations Assistant",
    description="An AI assistant that can execute complex tasks by planning, executing, and verifying results",
    version="1.0"
)

class TaskRequest(BaseModel):
    task: str

@app.post("/execute_task")
def execute_task(request: TaskRequest):
    try:
        # Step 1: Create execution plan
        execution_plan = create_execution_plan(request.task)

        # Step 2: Execute the plan
        executor = ExecutorAgent(execution_plan)
        execution_results = executor.execute()

        # Step 3: Verify results
        verification_passed = verify_execution_results(execution_results)

        return {
            "execution_plan": execution_plan,
            "execution_results": execution_results,
            "verification_passed": verification_passed
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@app.get("/health")
def health_check():
    return {"status": "ok"}


