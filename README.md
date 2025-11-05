# Zotero MCP Connector

A Model Control Protocol (MCP) connector for integrating your local Zotero with Claude.  
This enables direct read access to your local Zotero library through Claude's Desktop interface.
It depends on the ability to access a local web-api in Zotero 7.

This was inspired by a repository using Node.js and the web api: [mcp-zotero](https://github.com/kaliaboi/mcp-zotero).  
This builds on the shoulders of the fantastic [pyzotero](https://github.com/urschrei/pyzotero) library.

## Installation

### Run from local code (Recommended)
Information about Claude Desktop interacting with MCPs can be found [here](https://modelcontextprotocol.io/quickstart/user).

1. Use `uv`. Installation instructions can be found [here](https://docs.astral.sh/uv/getting-started/installation/).

2. Checkout the git project to local space and activate the virtual environment inside:
```bash
git clone https://github.com/dr1np/mcp-pyzotero.git
cd mcp-pyzotero
uv sync
```

3. Enable the local API in Zotero 7:
   ![Zotero Local API Settings](assets/LocalAPISettings.png)

4. Add the server to your local Claude installation:
```bash
uv run mcp install zotero.py
```

### Run encapsulated with uvx (Should work)
Edit the configuration for your Claude Desktop softare in the file.

    - macOS: ~/Library/Application Support/Claude/claude_desktop_config.json
    - Windows: %APPDATA%\Claude\claude_desktop_config.json

and add the Zotero entry
```json
{
    "mcpServers": {
        "Zotero": {
            "command": "uvx",
            "args": ["--from", "git+https://github.com/dr1np/mcp-pyzotero.git", 
                     "--with", "mcp[cli]",
                     "--with", "pyzotero",
                     "mcp", "run", "zotero.py"
                    ],
        }
    }
}
```

## Configuration

The connector is configured to work with local Zotero installations and currently only `user` libraries are supported. 
By default it uses the userid `0`, but you can also set the environment variable `ZOTERO_USER_ID` if needed:

```bash
uv run mcp install zotero.py -v ZOTERO_USER_ID=0
```

## Available Functions

### Available tools
- `get_zotero_information()`: Returns library information including summary, collections, recent items, or tags
- `get_collection_items(collection_key)`: Get all items in a specific collection
- `get_items_metadata(item_key)`: Get detailed information about specific paper(s), including abstract and BibTeX keys
- `search_library(query, mode)`: Search your Zotero library with configurable modes

### Tool Details

#### get_zotero_information
Returns information about your Zotero library. By default returns a summary, but can be configured to return:
- `summary`: Library overview and group information
- `recent`: Recently added items (default limit: 10)
- `tags`: All tags used in the library
- `collections`: Available collections

**Example usage:**
```
get_zotero_information(properties="summary,recent", limit=5)
```

#### get_collection_items
Retrieves all items from a specific collection.

**Parameters:**
- `collection_key`: The collection identifier
- `limit`: Optional limit on number of items returned

#### get_items_metadata
Gets detailed metadata for specific items.

**Parameters:**
- `item_key`: Item key(s), comma-separated for multiple items
- `include_abstract`: Include abstract (default: true)
- `include_bibtex`: Include BibTeX citation key (default: true)

#### search_library
Searches the Zotero library with flexible query options.

**Parameters:**
- `query`: Search term
- `qmode`: Search mode - "titleCreatorYear" (default) or "everything"
- `itemType`: Item type filter (default: "-attachment" to exclude attachments)
- `tag`: Tag filter
- `include_abstract`: Include abstracts in results
- `limit`: Result limit

## Testing

The repository includes test scripts to verify functionality:

```bash
# Basic functionality test
python simple_test.py

# Advanced functionality test
python advanced_test.py
```

### Test Results Summary

Based on testing with a library containing 619 items:

✅ **Library Information**: Successfully retrieves library stats, collections, and tags  
✅ **Search Functionality**: Finds items by keywords (e.g., "machine learning")  
✅ **Collection Access**: Retrieves items from specific collections  
✅ **Item Metadata**: Gets detailed information including abstracts and authors  
✅ **Item Types**: Supports journal articles, conference papers, books, etc.  
✅ **Attachments**: Detects PDF attachments and other file types  
✅ **Better BibTeX Integration**: Citation key support (when Better BibTeX plugin is installed)

**Sample Output:**
- Library contains 619 items across multiple collections
- Collections include "代码评审" (Code Review), "多分类" (Multiclass), etc.
- Search results include full metadata with DOI, URLs, and tags
- Supports both Chinese and English content

## Requirements

- Python 3.10+
  - pyzotero
  - mcp[cli]
- Local Zotero installation

## Contributing

Contributions are welcome! Please visit the [GitHub repository](https://github.com/dr1np/mcp-pyzotero) to:
- Report issues
- Submit pull requests
- Suggest improvements

## License

MIT