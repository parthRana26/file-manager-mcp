# File Manager MCP

Production-ready File System Management Server built with FastMCP and the Model Context Protocol (MCP).

Manage files, directories, archives, searches, and filesystem utilities through any MCP-compatible client such as Claude Desktop, Cursor, VS Code, Windsurf, ChatMCP, and custom MCP clients.

---

## Features

### File Management

* Create files
* Read files
* Update files
* Append content
* Delete files
* Rename files
* Move files
* Copy files

### Directory Management

* List directories
* Create directories
* Delete directories
* Directory statistics
* Directory tree view

### Search Services

* Search files by keyword
* File metadata inspection
* Directory metadata inspection
* Recursive tree generation

### Batch Operations

* Batch file creation
* Batch file deletion
* Batch file movement
* Batch file copying
* Batch file renaming
* Batch directory creation
* Batch directory deletion

### Archive Management

* Create ZIP archives
* Extract ZIP archives
* Inspect ZIP contents

### File Utilities

* File hashing
* Duplicate file detection
* File comparison
* Directory comparison
* Large file discovery
* Empty directory cleanup
* Temporary file cleanup

### Monitoring

* Health Check
* Server Information
* Tool Discovery

---

## Architecture

```text
MCP Client
    │
    ▼
FastMCP Server
    │
    ├── File Services
    ├── Search Services
    ├── Batch Services
    ├── ZIP Services
    └── Utility Services
    │
    ▼
Filesystem
```

---

## Project Structure

```text
file-manager-mcp/
│
├── main.py
├── config.py
├── auth.py
├── requirements.txt
├── pyproject.toml
│
├── services/
│   ├── file_service.py
│   ├── search_service.py
│   ├── batch_service.py
│   ├── zip_service.py
│   ├── utility_service.py
│   └── security_service.py
│
└── workspace/
```

---

## Installation

Clone repository:

```bash
git clone https://github.com/parthRana26/file-manager-mcp.git

cd file-manager-mcp
```

Install dependencies:

```bash
pip install -r requirements.txt
```

or

```bash
uv sync
```

---

## Running the Server

```bash
python main.py
```

Default endpoint:

```text
http://localhost:8000/mcp
```

Custom port:

```bash
PORT=9000 python main.py
```

---

## MCP Client Configuration

Example:

```json
{
  "mcpServers": {
    "file-manager-mcp": {
      "type": "http",
      "url": "http://localhost:8000/mcp"
    }
  }
}
```

Supported Clients:

* Claude Desktop
* Cursor
* VS Code
* Windsurf
* ChatMCP
* Custom MCP Clients

---

## Available Tools

| Category         | Tools |
| ---------------- | ----- |
| File Operations  | 11    |
| Search Services  | 4     |
| Batch Operations | 7     |
| ZIP Operations   | 3     |
| Utility Services | 7     |
| Meta Tools       | 2     |
| Total            | 34    |

---

## Example Prompts

* Create a file called notes.txt
* Search for files containing invoice
* Generate a tree view of my project
* Zip the project folder
* Find duplicate files
* Compare two directories
* Find files larger than 100 MB

---

## Security Notes

This server performs real filesystem operations.

Recommended:

* Run on trusted systems.
* Restrict accessible directories.
* Review destructive operations.
* Add authentication before public deployment.

---

## Local Usage and Hosting Limitations

This project is designed to run locally on the same machine as your MCP client. Users should clone the repository, install the dependencies, and start the server on their own system.

The server uses Streamable HTTP transport and is intended for local filesystem access. Running it locally helps keep file operations secure and under the user's control.

Transport:

```python
mcp.run(
    transport="streamable-http",
    host="0.0.0.0",
    port=PORT
)
```

---

## Roadmap

### Completed

* File CRUD Operations
* Directory Management
* Search Services
* Batch Operations
* ZIP Operations
* Utility Services
* Streamable HTTP Support

### Planned

* Authentication
* Role-Based Access Control
* Audit Logging
* File Versioning
* Docker Support
* Web Dashboard

---

## Author

Parth Rana

GitHub:
https://github.com/parthRana26

LinkedIn:
https://linkedin.com/in/parth-rana-profile

---

## License

Distributed under the MIT License. See `LICENSE` for more information.
