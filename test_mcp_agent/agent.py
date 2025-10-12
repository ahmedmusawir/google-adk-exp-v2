import os
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StreamableHTTPConnectionParams
from google.adk.models.lite_llm import LiteLlm

# 1. Create the configured LiteLLM client instance with OpenRouter
lite_llm_client = LiteLlm(
    model="openrouter/anthropic/claude-3.5-sonnet",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

# 2. Dynamic instruction function
def get_test_instructions(ctx) -> str:
    return """
    Your name is Test Agent! You are testing the MCP connection.
    
    You have access to an 'echo_tool' that echoes back any message you send to it.
    
    When the user says hello or asks you to test the connection:
    1. Use the echo_tool to send a test message
    2. Report back what the tool returned
    
    Be friendly and confirm that the MCP connection is working properly.
    """

# 3. Create the Agent with MCP Toolset pointing to your local server
root_agent = Agent(
    name="test_mcp_agent",
    model=lite_llm_client,
    description="Test agent connected to local MCP echo server",
    instruction=get_test_instructions,
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPConnectionParams(
                url="http://localhost:8080/mcp",  # Your local MCP server endpoint
                # No auth headers needed for local testing
            ),
        )
    ],
)