from google.adk.agents import Agent, ParallelAgent
from google.adk.tools import google_search

MODEL = "gemini-2.0-flash"

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

# The orchestrator that runs both agents concurrently
root_agent = ParallelAgent(
    name="ResearchAgent",
    description="A concurrent agent that gathers information on news and stock prices simultaneously.",
    sub_agents=[news_agent, stock_agent],
)