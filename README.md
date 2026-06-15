# 🗂️ File Manager MCP

### Open-Source MCP Server for Local File Management

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.13%2B-blue.svg)](https://www.python.org/)
[![MCP](https://img.shields.io/badge/MCP-Compatible-brightgreen)](https://modelcontextprotocol.io/)
[![FastMCP](https://img.shields.io/badge/FastMCP-powered-purple.svg)](https://github.com/jlowin/fastmcp)
[![Transport](https://img.shields.io/badge/Transport-Streamable_HTTP-success)](#)
[![Tools](https://img.shields.io/badge/MCP_Tools-35-orange)](#)
[![Status](https://img.shields.io/badge/Status-Active-success)](#)
[![Open Source](https://img.shields.io/badge/Open_Source-Yes-blueviolet)](#)

File Manager MCP is an open-source Model Context Protocol (MCP) server that enables AI assistants such as ChatGPT, Cursor, VS Code, Windsurf, and other MCP-compatible clients to perform local filesystem operations through natural language.

Built with FastMCP and Streamable HTTP transport, the server exposes 35 filesystem tools covering file management, directory operations, search, ZIP handling, batch processing, and utility operations.

---

## 🚀 Why File Manager MCP?

Instead of manually navigating files and folders, users can interact with their filesystem through AI.

### Example

User:

```text
Create a FastAPI project structure
```

AI:

```text
✓ Creates folders
✓ Creates README.md
✓ Creates requirements.txt
✓ Creates source files
```

User:

```text
Zip the project and move it to backups
```

AI:

```text
✓ Creates ZIP archive
✓ Moves archive
```

Everything runs locally on the user's machine.

---

## ✨ Features

### File Operations

* Create files
* Read files
* Update files
* Append content
* Delete files
* Move files
* Copy files
* Rename files

### Directory Operations

* Create directories
* Delete directories
* Analyze directories
* Generate directory trees

### Search Services

* Recursive file search
* Folder search
* Metadata inspection

### ZIP Operations

* Create ZIP archives
* Extract ZIP archives
* List ZIP contents

### Batch Operations

* Batch create files
* Batch delete files
* Batch move files
* Batch copy files
* Batch rename files
* Batch create directories
* Batch delete directories

### Utility Operations

* File hashing
* Duplicate detection
* File comparison
* Directory comparison
* Large file discovery
* Empty directory cleanup
* Temporary file cleanup

---

## 📊 Project Statistics

| Metric          | Value           |
| --------------- | --------------- |
| MCP Tools       | 35              |
| Service Modules | 5               |
| Transport       | Streamable HTTP |
| Framework       | FastMCP         |
| Language        | Python          |
| License         | MIT             |

---

## 🏗️ Architecture

```text
User
 │
 ▼
MCP Client
(ChatGPT / Cursor / VS Code)
 │
 ▼
File Manager MCP
(FastMCP Server)
 │
 ├── File Services
 ├── Search Services
 ├── Batch Services
 ├── ZIP Services
 └── Utility Services
 │
 ▼
Local Filesystem
```

---

## 🛠️ Technology Stack

* Python
* FastMCP
* Model Context Protocol (MCP)
* Streamable HTTP Transport
* pathlib
* shutil
* zipfile
* hashlib
* logging

---

## 🚀 Quick Start

### Clone Repository

```bash
git clone https://github.com/parthRana26/file-manager-mcp.git

cd file-manager-mcp
```

### Install uv

```bash
pip install uv
```

### Install Dependencies

```bash
uv sync
```

### Start Server

```bash
uv run main.py
```

Server Endpoint:

```text
http://localhost:8000/mcp
```

---

## 🔍 Testing with MCP Inspector

Start MCP Inspector:

```bash
npx @modelcontextprotocol/inspector
```

Connect using:

```text
Transport: Streamable HTTP

URL:
http://localhost:8000/mcp
```

Verify that all tools appear successfully.

---

## 🔌 Connecting MCP Clients

Use the following endpoint:

```text
http://localhost:8000/mcp
```

Example configuration:

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

Works with:

* ChatGPT
* Cursor
* VS Code
* Windsurf
* MCP Inspector
* Custom MCP Clients

---

## 💬 Example Prompts

```text
Create a README.md file
```

```text
Generate a FastAPI project structure
```

```text
Find duplicate files
```

```text
Create a ZIP archive of my project
```

```text
Compare two directories
```

```text
Find files larger than 500 MB
```

---

## 📁 Project Structure

```text
file-manager-mcp/

├── main.py
├── requirements.txt
├── config.py
├── README.md

├── services/
│   ├── file_service.py
│   ├── search_service.py
│   ├── batch_service.py
│   ├── zip_service.py
│   ├── utility_service.py
│   └── security_service.py

└── workspace/
```

---

## 🔒 Security Notes

This MCP server performs real filesystem operations.

Recommended:

* Run locally
* Use trusted MCP clients
* Review destructive operations before approval
* Use project-specific directories

---

## 👨‍💻 Maintainer

Parth Rana

GitHub:
https://github.com/parthRana26

LinkedIn:
https://linkedin.com/in/parth-rana-profile

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork the repository and submit pull requests.

---

## 📄 License

Licensed under the MIT License.

See LICENSE for details.
