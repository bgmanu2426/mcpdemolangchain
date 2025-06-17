# MCP Demo: LangChain Integration

This project demonstrates how to create and run MCP (Model Context Protocol) servers for math operations and weather information, suitable for integration with LangChain or other MCP-compatible clients.

## Project Structure

- `mathserver.py` — MCP server providing basic math operations (add, subtract, multiply, divide).
- `weather.py` — MCP server providing weather information for a given city (mock implementation).
- `client.py` — (Optional) Example client for interacting with the servers.
- `mcp.json` — Configuration file for MCP server endpoints.
- `pyproject.toml`, `uv.lock` — Python project dependencies and lock file.

## Requirements

- Python 3.8+
- `mcp` Python package (`pip install mcp`)
- (Optional) `npx` for the filesystem MCP server

## Setup

1. **Install dependencies:**
   ```sh
   uv sync
   ```

## Running the Servers

### Math MCP Server

This server communicates over stdio and provides basic math operations.

```sh
uv run mathserver.py
```

### Weather MCP Server

This server communicates over HTTP (default port 8000) and provides weather information.

```sh
uv run weather.py
```

> **Note:** If you see an error about port 8000 being in use, stop any other process using that port or change the port in `weather.py`.

## Configuration: `mcp.json`

Example configuration for MCP clients:

```json
{
  "mcpServers": {
    "weather": {
      "url": "http://localhost:8000/mcp",
      "transport": "streamable_http"
    },
    "math": {
      "command": "python",
      "args": [
        "D:\\VS_Code\\Learning\\mcpdemolangchain\\mathserver.py"
      ],
      "transport": "stdio"
    }
  }
}
```

## Usage

- Use an MCP-compatible client (such as LangChain) to connect to the servers as configured in `mcp.json`.
- The math server provides: `add`, `subtract`, `multiply`, `divide`.
- The weather server provides: `get_weather(city: str)`.

## Troubleshooting

- **Port in use:** If the weather server fails to start due to port 8000 being in use, stop the conflicting process or change the port.
- **Path errors:** Ensure all Windows paths in `mcp.json` use double backslashes.
- **Python errors:** Make sure the `mcp` package is installed in your Python environment.