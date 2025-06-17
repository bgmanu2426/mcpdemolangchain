from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MathMCP")


@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Adds two integers together.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The sum of a and b.
    """
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """
    Subtracts the second integer from the first.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The result of a minus b.
    """
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """
    Multiplies two integers together.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The product of a and b.
    """
    return a * b

@mcp.tool()
def divide(a: int, b: int) -> float:
    """
    Divides the first integer by the second.

    Parameters:
    a (int): The numerator.
    b (int): The denominator.

    Returns:
    float: The result of a divided by b.
    
    Raises:
    ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    mcp.run(transport="stdio")
