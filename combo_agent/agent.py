from google.adk.agents import Agent, ParallelAgent, SequentialAgent
from google.adk.tools import google_search, AgentTool

MODEL = "gemini-2.5-flash"

# Agent to find the latest news
news_agent = Agent(
    model=MODEL,
    name="NewsAgent",
    description="Finds the latest news on a specific topic.",
    instruction="Use the google_search tool to find the most recent news headlines for the given topic.",
    tools=[google_search],
    output_key="latest_news",
)

# Agent to find the current stock price
stock_agent = Agent(
    model=MODEL,
    name="StockAgent",
    description="Finds the current stock price of a company.",
    instruction="Use the google_search tool to find the most current stock price for the given company ticker or name.",
    tools=[google_search],
    output_key="current_stock_price",
)

# Parallel execution agent to run both searches concurrently
parallel_agent = ParallelAgent(
    name="ResearchAgent",
    description="A concurrent agent that gathers information on news and stock prices simultaneously.",
    sub_agents=[news_agent, stock_agent],
)

# Agent to synthesize the parallel results into a single response
synthesis_agent = Agent(
    model=MODEL,
    name="SynthesisAgent",
    description="Synthesizes information from multiple sources into a single, cohesive response.",
    instruction="""Synthesize the provided information from a news search and a stock price search.
    News: {latest_news}
    Stock Price: {current_stock_price}
    Combine these into a single, concise response for the user.
    """,
)

# The sequential workflow that is a tool for the root agent
research_workflow = SequentialAgent(
    name="ResearchWorkflow",
    description="A workflow that performs concurrent searches and synthesizes the results.",
    sub_agents=[parallel_agent, synthesis_agent],
)

# THE NEW ROOT AGENT
root_agent = Agent(
    model=MODEL,
    name="Chatbot",
    description="A helpful assistant that can answer questions about news and stock prices.",
    instruction="""You are a friendly and helpful chatbot. Your primary function is to answer user questions.
    If the user asks for news or stock prices, use the `research_tool` to get the information.
    For all other questions, respond conversationally.
    """,
    tools=[AgentTool(agent=research_workflow)],
)

# Note: The `run` or `adk web` command will now use `root_agent`
# from google.adk.agent_manager import AgentManager
# manager = AgentManager(root_agent)
# manager.send_request("What's the latest news on Tesla stock?")
# manager.send_request("Hello, how are you?")