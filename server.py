from mcp.server import serve
from mcp.server.stdio import stdio_server

async def main():
    async with stdio_server() as (read, write):
        await serve("zotero", read, write)
