# agent_langgraph.py
import asyncio, os 
from pathlib import Path
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI  # or Anthropic, etc.
from tools.local_tools import run_python_script 

openai_api_key = "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"
os.environ["OPENAI_API_KEY"] = openai_api_key

FS_CONFIG = {
    "filesystem": {
        "transport": "stdio",
        "command": "npx",
        "args": [
            "-y",
            "@modelcontextprotocol/server-filesystem",
            "/Users/akhalsa/Documents/job_smarts/agent",
        ],
    }
}

async def main():
    prompt_path = Path(__file__).parent / "system_prompt_v3.md"
    with open(prompt_path, 'r', encoding='utf-8') as f:
        system_prompt = f.read()
    # 1) MCP → LangChain tools
    mcp_client = MultiServerMCPClient(FS_CONFIG) # type: ignore
    tools = await mcp_client.get_tools()
    # 2) Build an agent that knows how to use them
    agent = create_agent(
        model=ChatOpenAI(model="gpt-5.2"),  # or "openai:gpt-5.2"
        tools=tools + [run_python_script],
        system_prompt=(system_prompt),
    )

    # 3) Run it like a normal LangGraph agent
    #job_board = "https://jobs.usv.com/jobs"
    job_board = "https://jobs.bvp.com/jobs"
    content_string = f"Extract all jobs from {job_board}"
    result = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": content_string
                }
            ]
        }
    )

    # result["messages"] is the full convo; last message is the assistant
    print(result["messages"])

if __name__ == "__main__":
    asyncio.run(main())
