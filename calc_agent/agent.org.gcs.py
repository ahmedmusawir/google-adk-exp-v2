# /calc_agent/agent.py
from google.adk import Agent  # or from google.adk.agents import Agent (either ok)
from google.adk.code_executors import BuiltInCodeExecutor
from utils.gcs_utils import fetch_instructions

code_executor = BuiltInCodeExecutor()

def get_live_instructions(ctx) -> str:
    return fetch_instructions("calc_agent")

root_agent = Agent(
    name="calc_agent",
    model="gemini-2.5-flash",
    description="Calculator agent",
    instruction=get_live_instructions,
    code_executor=code_executor,   # <-- the correct place
    # tools=[]                    # <-- leave empty (or remove entirely)
)
