# server.py
from fastmcp import FastMCP
import os
import dotenv

dotenv.load_dotenv()
mcp = FastMCP("My MCP Server")

@mcp.tool()
def get_companycode()-> str:
    """
    Fetch company code
    
    Args: None
        
    Returns:
        str: company code
    """
    return "#123456"

@mcp.tool()
def get_MCPcode()-> str:
    """
    Fetch MCP code
    
    Args: None
        
    Returns:
        str: MCP code
    """
    return "MCP#123@456"

if __name__ == "__main__":
     mcp.run()
