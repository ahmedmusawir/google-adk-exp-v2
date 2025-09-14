from google.adk.agents import Agent
from google.adk.tools import built_in_code_execution

root_agent = Agent(
    name="calc_agent",
    # Using the same model as requested
    model="gemini-2.5-flash",
    description="A calculator agent",
    instruction="""
You are a powerful calculator. Your superpower is that you
can perform any mathematical calculation by writing and executing
Python code. When a user asks a question that requires math,
use the code execution tool to find the precise answer.

After you receive the result from the code execution, you
MUST present that result to the user as the final answer.
    """,
    # The tool is an instance of the BuiltInCodeExecutor class
    tools=[built_in_code_execution]
)