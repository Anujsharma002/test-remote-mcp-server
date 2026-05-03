import random
from fastmcp import FastMCP
import json
mcp = FastMCP(name="Simple calculator server",auth=None)

@mcp.tool
def random_number(min_val:int=1, max_val:int=100)->int:
    """Generate a random number within a range.
    Args:
        min_val (int): The minimum value (default: 1).
        max_val (int): The maximum value (default: 100).
        
        Returns:
            int: A random integer between min_val and max_val (inclusive)."""
    return random.randint(min_val, max_val)

@mcp.tool
def add_numbers(a:int, b:int)->int:
    """Add two numbers and return the result."""
    return a + b
@mcp.resource("info://server")
def server_info():
    """Get information about this server."""
    info = {
        "name":"Simple Calculator Server",
        "version":"1.0.0",
        "description":"A basic server with math tools.",
        "tools":["random_number", "add"],
        "author":"Your Name"
    }
    return json.dumps(info,indent=2)

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=3001)
