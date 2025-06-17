from mcp.server.fastmcp import FastMCP

mcp=FastMCP("WeatherMCP")

@mcp.tool()
def get_weather(city: str) -> str:
    """
    Retrieves the current weather for a specified city.

    Parameters:
    city (str): The name of the city to get the weather for.

    Returns:
    str: A string describing the current weather in the specified city.
    """
    # Placeholder implementation
    return f"The current weather in {city} is sunny with a temperature of 25°C."

if __name__ == "__main__":
    mcp.run(transport="streamable-http")