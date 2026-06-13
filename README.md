# file-manager-mcp

A production-ready Model Context Protocol (MCP) server built with FastMCP for managing files, directories, archives, and filesystem utilities.

## Features

### File Operations

* List files and directories
* Create files
* Read files
* Update files
* Append content to files
* Delete files
* Rename files
* Move files
* Copy files

### Directory Operations

* Create directories
* Delete directories

### Search Operations

* Search files by name
* Get file information
* Get directory information
* Generate directory tree view

### Batch Operations

* Batch create files
* Batch delete files
* Batch move files
* Batch copy files
* Batch rename files
* Batch create directories
* Batch delete directories

### ZIP Operations

* Create ZIP archives
* Extract ZIP archives
* List ZIP contents

### Utility Operations

* Find large files
* Generate file hashes
* Find duplicate files
* Compare files
* Compare directories
* Clean empty directories
* Clean temporary files

### Server Utilities

* Health check endpoint
* Server information endpoint
* Tool discovery endpoint
* Logging support

---

## Tech Stack

* Python 3.11+
* FastMCP
* Uvicorn
* MCP Protocol
* Streamable HTTP Transport

---

## Project Structure

```text
file-system-manager/
│
├── main.py
├── requirements.txt
├── README.md
├── server.py
├── auth.py
├── config.py
│
├── services/
│   ├── file_service.py
│   ├── search_service.py
│   ├── batch_service.py
│   ├── zip_service.py
│   ├── utility_service.py
│   └── security_service.py
│
└── server.log
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/ParthRana26/file-manager-mcp.git
cd file-manager-mcp
```

### Create Virtual Environment

```bash
uv venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
uv pip install -r requirements.txt
```

---

## Running Locally

```bash
uv run python main.py
```

Server starts on:

```text
http://localhost:8000/mcp
```

---

## Testing with MCP Inspector

Start the server:

```bash
uv run python main.py
```

Open MCP Inspector:

```bash
npx @modelcontextprotocol/inspector
```

Connect using:

```text
Transport: Streamable HTTP
URL: http://localhost:8000/mcp
```

---

## Deployment

This server can be deployed on:

* Prefect Horizon
* Railway
* Render
* VPS
* Docker

### Prefect Horizon

1. Push repository to GitHub.
2. Open Prefect Horizon.
3. Create Hosted MCP Server.
4. Select repository.
5. Set entrypoint:

```text
main.py
```

6. Deploy.

---

## Available MCP Tools

### File Tools

* list_files_tool
* create_file_tool
* read_file_tool
* update_file_tool
* append_file_tool
* delete_file_tool
* create_directory_tool
* delete_directory_tool
* rename_file_tool
* move_file_tool
* copy_file_tool

### Search Tools

* search_files_tool
* get_file_info_tool
* get_directory_info_tool
* tree_view_tool

### Batch Tools

* batch_create_files_tool
* batch_delete_files_tool
* batch_move_files_tool
* batch_copy_files_tool
* batch_rename_files_tool
* batch_create_directories_tool
* batch_delete_directories_tool

### ZIP Tools

* create_zip_tool
* extract_zip_tool
* list_zip_contents_tool

### Utility Tools

* find_large_files_tool
* file_hash_tool
* duplicate_file_finder_tool
* compare_files_tool
* compare_directories_tool
* clean_empty_directories_tool
* clean_temp_files_tool

### Meta Tools

* health_check_tool
* server_info_tool
* available_tools_tool

---

## Security

* Path validation
* Safe filesystem access
* Error handling
* Logging support
* Controlled file operations

---

## Version

```text
Version: 1.0.0
Phase: 7
Status: Production Ready
Tools: 34
```

---

## Author

Parth Rana

GitHub:
https://github.com/ParthRana26

---

## License

MIT License
