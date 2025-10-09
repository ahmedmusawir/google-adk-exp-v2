from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StreamableHTTPConnectionParams

# GHL Private Integration credentials
GHL_API_TOKEN = "pit-1ac05ee8-87bd-4aea-abb7-fea882c11721"  # From Postman test
GHL_LOCATION_ID = "4rKuULHASyQ99nwdL1XH"              # From Postman test

root_agent = Agent(
    name="ghl_mcp_agent",
    model="gemini-2.0-flash",
    description="Rico - Your friendly GHL-connected assistant",
    instruction="""
    Your name is Rico! You are a friendly and funny assistant with full access to GoHighLevel CRM data.
    You always ask the user's name first and then answer them using their name, making you more personable.
    You have a light-hearted sense of humor and occasionally share jokes to lighten the mood.

    IMPORTANT: The locationId is already configured in your system - you do NOT need to ask users for it.
    You have direct access to the GHL location and can fetch data immediately.

    You can access GHL data including:
    - Contacts (search, get, create, update)
    - Products
    - Orders
    - Custom fields
    - Prices
    - Conversations
    - Calendars
    - Opportunities
    - And much more!

    When users ask about CRM data, use your GHL tools to fetch real information immediately.
    Always be helpful and never ask for locationId - it's already set up!
    """,
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPConnectionParams(
                url="https://services.leadconnectorhq.com/mcp/",
                headers={
                    "Authorization": f"Bearer {GHL_API_TOKEN}",
                    "locationId": GHL_LOCATION_ID
                }
            ),
            # Optional: filter specific tools if needed
            # tool_filter=['contacts_search-contacts', 'contacts_get-contact']
        )
    ],
)