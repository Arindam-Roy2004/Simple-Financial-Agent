import streamlit as st
from dotenv import load_dotenv
import os

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

# Load API key
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")  # type: ignore

# Define agents
web_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are an assistant and search the web for the information.",
    tools=[DuckDuckGoTools()],
    instructions="Always include the source of the information you provide.",
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Finance Expert",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True)],
    instructions="Always include the source of the information you provide.",
    show_tool_calls=True,
    markdown=True,
)

# Team agent
agent_team = Agent(team=[web_agent, finance_agent], model=OpenAIChat(id="gpt-4o"))

# Streamlit UI
st.set_page_config(page_title="Agno Agent Assistant", layout="centered")
st.title("🤖 Multi-Agent Assistant (Web + Finance)")

query = st.text_input("Ask me anything:", placeholder="e.g., What is the stock price of AAPL or latest AI trends?")

if query:
    with st.spinner("🔎 Thinking..."):
        # .run() returns a RunResponse object
        response = agent_team.run(query)
        
        # --- CORRECTED LINE ---
        # Access the .content attribute to get the final answer string
        st.markdown(response.content)