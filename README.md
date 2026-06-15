# 🗂️ File Manager MCP

**Open-Source MCP Server for Local File Management**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.13%2B-blue.svg)](https://www.python.org/)
[![MCP](https://img.shields.io/badge/MCP-Compatible-brightgreen)](https://modelcontextprotocol.io/)
[![FastMCP](https://img.shields.io/badge/FastMCP-powered-purple.svg)](https://github.com/jlowin/fastmcp)

File Manager MCP allows AI assistants such as **Claude Desktop, ChatGPT, Cursor, VS Code, Windsurf, MCP Inspector, and custom MCP clients** to safely manage files and folders on your computer using natural language.

Everything runs **locally on your machine**. Your files stay under your control.

---

# 🚀 Who Is This For?

File Manager MCP is designed for:

* 👨‍💻 Developers
* 🎓 Students
* 🏢 Professionals
* 🤖 MCP Enthusiasts
* ⚡ Power Users

Whether you're organizing projects, managing documents, comparing files, creating archives, or automating repetitive filesystem tasks, File Manager MCP provides a simple natural-language interface through your favorite AI assistant.

---

# ✨ Features

### 📁 File Operations

* Create files
* Read files
* Update files
* Append content
* Delete files
* Rename files
* Move files
* Copy files

### 📂 Directory Operations

* Create directories
* Delete directories
* Analyze directories
* Generate directory trees

### 🔍 Search Services

* Search files
* Search folders
* Recursive search

### 📦 ZIP Operations

* Create ZIP archives
* Extract ZIP archives
* Inspect ZIP contents

### ⚡ Batch Operations

* Batch create files
* Batch delete files
* Batch move files
* Batch copy files
* Batch rename files
* Batch create directories
* Batch delete directories

### 🧰 Utility Tools

* File hashing
* Duplicate file detection
* File comparison
* Directory comparison
* Large file discovery
* Empty directory cleanup
* Temporary file cleanup

### 🌐 MCP Features

* Streamable HTTP Transport
* FastMCP Powered
* MCP Compatible
* Local First Architecture

---

# 📊 Project Statistics

| Metric          | Value           |
| --------------- | --------------- |
| MCP Tools       | 35              |
| Service Modules | 5               |
| Transport       | Streamable HTTP |
| Language        | Python          |
| License         | MIT             |
| Status          | Active          |

---

# 🔄 How It Works

```text
You
 ↓
AI Assistant
(ChatGPT / Claude / Cursor)
 ↓
File Manager MCP
 ↓
Your Local Filesystem
```

Example:

You ask:

"Create a FastAPI project structure"

Your AI assistant sends a request to File Manager MCP.

File Manager MCP creates the folders and files on your computer and returns the result.

No files are uploaded by File Manager MCP.

---

# 🔌 Supported MCP Clients

File Manager MCP works with:

* Claude Desktop
* ChatGPT
* Cursor
* VS Code
* Windsurf
* MCP Inspector
* Custom MCP Clients

Any MCP-compatible client can connect.

---

# 🚀 Quick Start

## 1. Clone Repository

```bash
git clone https://github.com/parthRana26/file-manager-mcp.git
cd file-manager-mcp
```

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

### Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Start MCP Server

```bash
python main.py
```

Server URL:

```text
http://localhost:8000/mcp
```

---

# 🔧 MCP Client Setup

## Step 1

Start File Manager MCP:

```bash
python main.py
```

## Step 2

Copy the endpoint:

```text
http://localhost:8000/mcp
```

## Step 3

Add it to your MCP Client:

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

## Step 4

Restart your MCP Client.

## Step 5

Ask:

```text
Show available tools from File Manager MCP
```

---

# ✅ Verify Installation

Ask your AI:

```text
Show available tools from File Manager MCP
```

Or:

```text
Run health_check_tool
```

Expected response:

```json
{
  "status": "healthy"
}
```

---

# 💬 Example Prompts

### File Management

```text
Create a README.md file
```

```text
Read requirements.txt
```

```text
Rename all files to snake_case
```

```text
Move PDF files into Documents
```

### Search

```text
Find files containing invoice
```

```text
Search for folders containing MCP
```

### Directory Management

```text
Create a FastAPI project structure
```

```text
Show directory tree of my workspace
```

### ZIP Operations

```text
Create a ZIP archive of my project
```

```text
Extract project.zip
```

```text
Show ZIP contents
```

### Utility Operations

```text
Generate SHA256 hash of a file
```

```text
Find duplicate files
```

```text
Compare two directories
```

```text
Find files larger than 500 MB
```

```text
Remove empty folders
```

---

# 🧩 Example Workflow

### User

> Create a FastAPI project structure

### AI

✅ Creates folders

✅ Creates README.md

✅ Creates requirements.txt

✅ Creates source files

---

### User

> Zip the project

### AI

✅ Creates project.zip

---

### User

> Move the ZIP into backups

### AI

✅ Moves the archive

---

# 🏗️ Architecture

```text
main.py
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

# 📁 Project Structure

```text
file-manager-mcp/
│
├── main.py
├── requirements.txt
├── README.md
├── config.py
├── auth.py
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

# 🎯 Why File Manager MCP?

Most filesystem MCP servers provide only basic file operations.

File Manager MCP combines:

* File Management
* Directory Management
* Search Services
* Batch Operations
* ZIP Utilities
* File Hashing
* Duplicate Detection
* File Comparison
* Directory Comparison
* Cleanup Utilities

all inside a single MCP server.

---

# 👥 Use Cases

### Developers

* Organize projects
* Generate folder structures
* Compare code versions
* Archive releases

### Students

* Manage assignments
* Organize notes
* Archive coursework

### Content Creators

* Organize assets
* Remove duplicate media
* Archive completed work

### Power Users

* Automate filesystem tasks
* Clean directories
* Analyze storage usage

---

# 🔒 Security Notes

File Manager MCP performs real filesystem operations.

It can:

* Create files
* Modify files
* Move files
* Delete files
* Create ZIP archives
* Extract ZIP archives
* Remove directories

Recommended:

✅ Run locally

✅ Use trusted MCP clients

✅ Review destructive operations before approval

✅ Use project-specific folders when possible

---

# 🌍 Open Source

File Manager MCP is open source.

You are free to:

* Use it
* Modify it
* Extend it
* Fork it
* Contribute to it

Community contributions are welcome.

---

# 🛣️ Roadmap

* Workspace restrictions
* Authentication support
* Automated tests
* CI/CD pipeline
* Better ZIP validation
* Configuration via .env
* Additional MCP resources
* More utility tools

---

# 🤝 Contributing

Contributions, issues, and feature requests are welcome.

1. Fork the repository
2. Create a feature branch
3. Make changes
4. Commit your changes
5. Open a Pull Request

---

# 📄 License

Licensed under the MIT License.

See the LICENSE file for details.

---

# ⭐ Support

If you find this project useful:

* ⭐ Star the repository
* 🐛 Report issues
* 💡 Suggest features
* 🔀 Submit pull requests
* 📢 Share with the MCP community

Every contribution helps improve File Manager MCP.

---

<p align="center">
Built with ❤️ using FastMCP and the Model Context Protocol.
</p>
