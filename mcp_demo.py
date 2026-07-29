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
def get_ABCcode()-> str:
    """
    Fetch ABC code    
    Args: None        
    Returns:
        str: ABC code
    """
    return "#ABC123"

@mcp.tool() 
def get_XYZcode()-> str:
    """
    Fetch XYZ code    
    Args: None        
    Returns:
        str: XYZ code
    """
    return "#XYZ1237"

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
    mcp.run(
        transport="streamable-http",
        host="127.0.0.1",
        port=3000,
    )