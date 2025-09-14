# from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.agents import Agent, SequentialAgent
from google.adk.tools import google_search

MODEL="gemini-1.5-flash" 
# MODEL="gemini-2.5-flash" 

# IdeaAgent: The creative brainstormer
idea_agent = Agent(
    model=MODEL,
    name="IdeaAgent",
    description="Brainstorms creative and exciting weekend travel ideas.",
    instruction="You are a creative travel agent. Use the tool to brainstorm and respond to the user with 3 exciting weekend trip ideas based on the user's request.",
    tools=[google_search],
    output_key="trip_ideas", # The output is explicitly saved here
)

# RefinerAgent: The budget-conscious filter
refiner_agent = Agent(
    model=MODEL,
    name="RefinerAgent",
    description="Reviews provided travel ideas and selects those under the provided budget.",
    instruction="""Review the provided trip ideas in the context.
    Ideas: {trip_ideas}
    Respond ONLY with the ideas estimated to cost under the provided budget for a weekend. If none are suitable, say so.
    """,
    tools=[google_search],
    output_key="refined_ideas", # This output is also saved for the final response
)

# RootAgent: The orchestrator
root_agent = SequentialAgent(
    name="PlannerAgent",
    description="Responsible for orchestrating the other agents for a successful plan",
    sub_agents=[idea_agent, refiner_agent],
)

