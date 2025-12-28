# fs_mcp_client.py
import asyncio, os
from langchain_mcp_adapters.client import MultiServerMCPClient
from openai import OpenAI
from mcp.types import Tool
from fastmcp import Client

openai_api_key = "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"

ai_client = OpenAI(
    # This is the default and can be omitted
    api_key=openai_api_key,
)




FS_CONFIG = {
    "mcpServers": {
        "filesystem": {
            "transport": "stdio",
            "command": "npx",
            "args": [
                "-y",
                "@modelcontextprotocol/server-filesystem",
                "/Users/akhalsa/Documents/job_smarts",
            ],
            # Optional:
            # "env": {},
            # "cwd": "/Users/akhalsa/Documents/job_smarts",
        }
    }
}


def mcp_tool_to_openai_tool(mcp_tool: Tool) :
    """
    Convert a FastMCP Tool (from client.list_tools()) into
    an OpenAI function tool definition.
    """
    # MCP spec: tools always expose an inputSchema JSON Schema object
    params = mcp_tool.inputSchema or {
        "type": "object",
        "properties": {},
        "required": [],
        "additionalProperties": False,
    }
    params.setdefault("additionalProperties", False)

    return {
        "type": "function",
        "name": mcp_tool.name,
        "description": mcp_tool.description or "",
        "parameters": params,
    }


async def demo():
    mcp_client = Client(FS_CONFIG)

    async with mcp_client:
        print("Connected:", mcp_client.is_connected())

        # List tools exposed by the filesystem server
        tools = await mcp_client.list_tools()
        print("Tools:", [t.name for t in tools])
        oa_tools = [mcp_tool_to_openai_tool(t) for t in tools]
        print(oa_tools)
        response = ai_client.responses.create(
            model="gpt-5.2",
            input="Save a file called hello.txt with the text 'this is a message from openai' ",
            tools=oa_tools

        )
        print("\nDONE\n")

        print(response)



if __name__ == "__main__":
    asyncio.run(demo())

