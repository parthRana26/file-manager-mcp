# File Manager MCP

[![Python](https://img.shields.io/badge/Python-3.11+-3776ab?logo=python&logoColor=white)](https://www.python.org/)
[![FastMCP](https://img.shields.io/badge/FastMCP-Production%20Ready-4CAF50?logo=fastapi&logoColor=white)](https://github.com/jreichel/fastmcp)
[![MCP](https://img.shields.io/badge/MCP-Model%20Context%20Protocol-0066CC?logoColor=white)](https://modelcontextprotocol.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)](https://github.com/parthRana26/file-manager-mcp)

---

## 🎯 Overview

**File Manager MCP** is a production-grade Model Context Protocol (MCP) server that provides comprehensive file system management capabilities for local execution. It enables AI agents and LLM applications like Claude, Cursor, VS Code, and Windsurf to perform sophisticated filesystem operations with a standardized, secure interface.

This MCP server is designed to run locally on your machine, providing AI assistants with trusted access to your filesystem through 34 specialized tools organized by category. Whether you're automating file operations, performing batch tasks, or enabling AI-assisted development workflows, File Manager MCP delivers a robust foundation.

### Why File Manager MCP?

- **Local Execution**: Runs entirely on your machine with no cloud dependencies or external services
- **Standardized Protocol**: Implements Model Context Protocol for seamless AI integration
- **Comprehensive Tooling**: 34 production-tested tools covering all major filesystem operations
- **AI-First Design**: Purpose-built for LLM interactions and autonomous agent workflows
- **Security-First**: Path validation, permission checks, and configurable access controls
- **Multi-Client Support**: Works with Claude Desktop, Cursor, VS Code, and Windsurf

---

## ✨ Features

### Core File Operations
- **CRUD Operations**: List, create, read, update, delete files
- **Advanced Operations**: Append, rename, move, copy files with full path validation
- **Directory Management**: Create, delete, and analyze directory structures
- **Batch Operations**: Efficient bulk operations for files and directories (create, delete, move, copy, rename)

### Search & Discovery
- **File Search**: Find files by name patterns across directory trees
- **File Metadata**: Retrieve detailed file and directory information
- **Tree Generation**: Generate visual directory tree representations
- **Large File Discovery**: Identify files exceeding specified size thresholds

### Archive & Compression
- **ZIP Operations**: Create, extract, and list ZIP archive contents
- **Batch Archive**: Process multiple files and directories into archives

### Advanced Utilities
- **File Hashing**: Generate MD5, SHA-1, and SHA-256 hashes for integrity verification
- **Duplicate Detection**: Find duplicate files across directories using content hashing
- **File Comparison**: Compare files at byte level for differences
- **Directory Comparison**: Analyze structural differences between directories
- **Cleanup Operations**: Identify and remove temporary files and empty directories

### System & Health
- **Health Checks**: Monitor server status and availability
- **Tool Discovery**: Enumerate all available tools and their specifications
- **Server Information**: Access server configuration and metadata
- **Logging**: Comprehensive request/response logging for debugging and auditing

---

## 📋 Prerequisites

- **Python**: 3.11 or higher
- **UV**: Package manager (recommended) or pip
- **Git**: For cloning the repository

### System Requirements
- **OS**: Linux, macOS, or Windows
- **RAM**: Minimum 512MB (1GB+ recommended)
- **Disk**: 50MB free space for installation

---

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/parthRana26/file-manager-mcp.git
cd file-manager-mcp
```

### Step 2: Create Virtual Environment

```bash
# Using UV (recommended)
uv venv

# Or using Python venv
python3.11 -m venv .venv
```

### Step 3: Activate Environment

```bash
# On Linux/macOS:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
# Using UV
uv pip install -r requirements.txt

# Or using pip
pip install -r requirements.txt
```

### Dependencies

Key dependencies included in `requirements.txt`:

- **fastmcp** (>=0.1.0): FastMCP framework for MCP server implementation
- **python-dotenv** (>=1.0.0): Environment variable management

---

## 💻 Quick Start

### Starting the Server

```bash
# Option 1: Using UV
uv run python main.py

# Option 2: Direct Python execution
python main.py
```

Expected output:
```
INFO:uvicorn.server:Uvicorn running on http://0.0.0.0:8000
INFO:main:Starting File Manager MCP on port 8000
```

The server will be available at: **`http://localhost:8000/mcp`**

### Verify Server is Running

```bash
# In another terminal
curl http://localhost:8000/mcp
```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root to configure the server:

```bash
# Server Settings
MCP_HOST=0.0.0.0              # Bind address (0.0.0.0 for all interfaces)
MCP_PORT=8000                 # Server port
LOG_LEVEL=INFO                # DEBUG, INFO, WARNING, ERROR, CRITICAL

# Security Settings
ENABLE_PATH_VALIDATION=true   # Validate paths to prevent traversal attacks
ENABLE_REQUEST_LOGGING=true   # Log all requests/responses

# Optional: Restrict operations to specific directories
# ALLOWED_BASE_DIRS=/home/user/projects:/tmp/workspace
```

### Default Configuration

If no `.env` file is provided:
- **Host**: `0.0.0.0`
- **Port**: `8000`
- **Log Level**: `INFO`
- **Path Validation**: Enabled by default
- **Request Logging**: Enabled by default

---

## 🔌 MCP Client Configuration

### Claude Desktop

1. **Locate Configuration File**
   - **macOS/Linux**: `~/.config/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

2. **Edit Configuration**

Add the File Manager MCP server to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "file-manager": {
      "command": "python",
      "args": [
        "-m",
        "uvicorn",
        "main:mcp",
        "--host",
        "127.0.0.1",
        "--port",
        "8000"
      ],
      "cwd": "/path/to/file-manager-mcp"
    }
  }
}
```

3. **Restart Claude Desktop** for changes to take effect

### Cursor

1. **Open Settings** (`Cmd+,` or `Ctrl+,`)

2. **Navigate to**: Features → MCP

3. **Add New Server**:
   - **Name**: `file-manager`
   - **Type**: `stdio` or `HTTP`
   - **Command**: `python main.py`
   - **Working Directory**: `/path/to/file-manager-mcp`

4. **Save and Restart** Cursor

### VS Code

1. **Install MCP Extension** (if not already installed)
   - Search for "MCP" in the Extensions marketplace

2. **Configure MCP Extension**

Add to VS Code `settings.json`:

```json
"mcp.servers": {
  "file-manager": {
    "command": "python",
    "args": ["main.py"],
    "cwd": "/path/to/file-manager-mcp",
    "env": {
      "PYTHONUNBUFFERED": "1"
    }
  }
}
```

3. **Restart VS Code**

### Windsurf

1. **Open Settings** (`Cmd+,` or `Ctrl+,`)

2. **Search for "MCP"** in settings

3. **Add Server Configuration**:

```json
{
  "mcp": {
    "servers": {
      "file-manager": {
        "command": "python",
        "args": ["main.py"],
        "cwd": "/path/to/file-manager-mcp"
      }
    }
  }
}
```

4. **Reload Windsurf**

---

## 📁 Complete Tools Reference

### File Management Tools (11 tools)

| Tool | Parameters | Purpose |
|------|-----------|---------|
| `list_files_tool` | `path: str` | List all files and directories in a path |
| `create_file_tool` | `path: str`, `content: str` | Create a new file with content |
| `read_file_tool` | `path: str` | Read complete file contents |
| `update_file_tool` | `path: str`, `content: str` | Replace entire file content |
| `append_file_tool` | `path: str`, `content: str` | Append content to existing file |
| `delete_file_tool` | `path: str` | Delete a file permanently |
| `rename_file_tool` | `old_path: str`, `new_path: str` | Rename file or directory |
| `move_file_tool` | `source: str`, `destination: str` | Move file to new location |
| `copy_file_tool` | `source: str`, `destination: str` | Copy file to destination |
| `create_directory_tool` | `path: str` | Create new directory |
| `delete_directory_tool` | `path: str` | Delete directory (recursive) |

### Search & Discovery Tools (4 tools)

| Tool | Parameters | Purpose |
|------|-----------|---------|
| `search_files_tool` | `path: str`, `keyword: str` | Find files by name pattern |
| `get_file_info_tool` | `path: str` | Get detailed file metadata (size, permissions, dates) |
| `get_directory_info_tool` | `path: str` | Get directory statistics (file count, total size) |
| `tree_view_tool` | `path: str` | Generate visual directory tree structure |

### Batch Operations Tools (7 tools)

| Tool | Parameters | Purpose |
|------|-----------|---------|
| `batch_create_files_tool` | `files: list` | Create multiple files in single operation |
| `batch_delete_files_tool` | `paths: list` | Delete multiple files efficiently |
| `batch_move_files_tool` | `operations: list` | Move multiple files with path pairs |
| `batch_copy_files_tool` | `operations: list` | Copy multiple files with path pairs |
| `batch_rename_files_tool` | `operations: list` | Rename multiple files in batch |
| `batch_create_directories_tool` | `paths: list` | Create multiple directories |
| `batch_delete_directories_tool` | `paths: list` | Delete multiple directories |

### Archive Operations Tools (3 tools)

| Tool | Parameters | Purpose |
|------|-----------|---------|
| `create_zip_tool` | `source_path: str`, `zip_path: str` | Create ZIP archive from directory/file |
| `extract_zip_tool` | `zip_path: str`, `destination: str` | Extract ZIP archive to destination |
| `list_zip_contents_tool` | `zip_path: str` | List all files within ZIP archive |

### Utility & Analysis Tools (7 tools)

| Tool | Parameters | Purpose |
|------|-----------|---------|
| `file_hash_tool` | `path: str`, `algorithm: str` | Generate file hash (MD5, SHA-1, SHA-256) |
| `duplicate_file_finder_tool` | `path: str` | Find duplicate files by content hash |
| `compare_files_tool` | `file1: str`, `file2: str` | Compare two files byte-by-byte |
| `compare_directories_tool` | `dir1: str`, `dir2: str` | Compare directory structures and contents |
| `find_large_files_tool` | `path: str`, `min_size_mb: float` | Find files exceeding size threshold |
| `clean_empty_directories_tool` | `path: str` | Remove all empty directories recursively |
| `clean_temp_files_tool` | `path: str` | Remove temporary files (*.tmp, *.bak, etc.) |

### System & Metadata Tools (2 tools)

| Tool | Parameters | Purpose |
|------|-----------|---------|
| `health_check_tool` | None | Verify server is running and healthy |
| `server_info_tool` | None | Get server version, status, and tool count |
| `available_tools_tool` | None | List all available tools and categories |

**Total**: 34 tools across 6 categories

---

## 📚 Usage Examples

### Basic File Operations

```python
# Example: Create and read a file
from mcp import Client

client = Client("http://localhost:8000/mcp")

# Create a new file
result = await client.call_tool("create_file_tool", {
    "path": "/tmp/notes.txt",
    "content": "Important notes go here"
})

# Read the file back
result = await client.call_tool("read_file_tool", {
    "path": "/tmp/notes.txt"
})
print(result)  # Returns: {"content": "Important notes go here"}

# Update the file
await client.call_tool("update_file_tool", {
    "path": "/tmp/notes.txt",
    "content": "Updated content"
})

# Delete the file
await client.call_tool("delete_file_tool", {
    "path": "/tmp/notes.txt"
})
```

### Search and Discovery

```python
# Find all Python files in a directory
result = await client.call_tool("search_files_tool", {
    "path": "/home/user/projects",
    "keyword": "*.py"
})

# Get detailed file information
result = await client.call_tool("get_file_info_tool", {
    "path": "/home/user/projects/main.py"
})

# Generate directory tree
result = await client.call_tool("tree_view_tool", {
    "path": "/home/user/projects"
})
```

### Batch Operations

```python
# Create multiple files at once
result = await client.call_tool("batch_create_files_tool", {
    "files": [
        {"path": "/tmp/file1.txt", "content": "Content 1"},
        {"path": "/tmp/file2.txt", "content": "Content 2"},
        {"path": "/tmp/file3.txt", "content": "Content 3"}
    ]
})

# Move multiple files
result = await client.call_tool("batch_move_files_tool", {
    "operations": [
        {"source": "/tmp/old1.txt", "destination": "/home/user/new1.txt"},
        {"source": "/tmp/old2.txt", "destination": "/home/user/new2.txt"}
    ]
})
```

### Archive Operations

```python
# Create a backup ZIP
result = await client.call_tool("create_zip_tool", {
    "source_path": "/home/user/documents",
    "zip_path": "/home/user/backup.zip"
})

# List ZIP contents
result = await client.call_tool("list_zip_contents_tool", {
    "zip_path": "/home/user/backup.zip"
})

# Extract archive
result = await client.call_tool("extract_zip_tool", {
    "zip_path": "/home/user/backup.zip",
    "destination": "/home/user/restored"
})
```

### File Analysis & Cleanup

```python
# Find large files (>100MB)
result = await client.call_tool("find_large_files_tool", {
    "path": "/home/user",
    "min_size_mb": 100
})

# Find duplicate files
result = await client.call_tool("duplicate_file_finder_tool", {
    "path": "/home/user/documents"
})

# Compare two files
result = await client.call_tool("compare_files_tool", {
    "file1": "/home/user/version1.txt",
    "file2": "/home/user/version2.txt"
})

# Generate file hash
result = await client.call_tool("file_hash_tool", {
    "path": "/home/user/important.zip",
    "algorithm": "sha256"
})

# Clean up temporary files
result = await client.call_tool("clean_temp_files_tool", {
    "path": "/home/user"
})
```

---

## 🔄 Real-World Workflow Example

### Automated Backup and Cleanup

```python
import asyncio
from mcp import Client

async def backup_workflow():
    """
    Complete workflow:
    1. Find large files
    2. Create backup archive
    3. Detect duplicates
    4. Remove temporary files
    5. Verify backup integrity
    """
    
    client = Client("http://localhost:8000/mcp")
    
    # Step 1: Analyze large files
    print("📊 Analyzing large files...")
    large_files = await client.call_tool("find_large_files_tool", {
        "path": "/home/user/documents",
        "min_size_mb": 50
    })
    print(f"Found {len(large_files['files'])} files > 50MB")
    
    # Step 2: Create backup
    print("📦 Creating backup...")
    backup = await client.call_tool("create_zip_tool", {
        "source_path": "/home/user/documents",
        "zip_path": "/backups/documents.zip"
    })
    
    # Step 3: Find duplicates
    print("🔍 Detecting duplicates...")
    duplicates = await client.call_tool("duplicate_file_finder_tool", {
        "path": "/home/user/documents"
    })
    
    # Step 4: Clean up
    print("🧹 Cleaning temporary files...")
    await client.call_tool("clean_temp_files_tool", {
        "path": "/home/user"
    })
    
    # Step 5: Verify backup
    print("🔐 Verifying backup...")
    hash_result = await client.call_tool("file_hash_tool", {
        "path": "/backups/documents.zip",
        "algorithm": "sha256"
    })
    print(f"Backup verified: {hash_result['hash']}")
    
    print("✅ Workflow complete!")

asyncio.run(backup_workflow())
```

---

## 🏗️ Project Structure

```
file-manager-mcp/
├── main.py                      # Entry point, MCP server initialization
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── .env                         # Configuration (create locally)
├── .gitignore                   # Git ignore rules
│
├── services/                    # Core business logic
│   ├── file_service.py         # File CRUD operations
│   ├── search_service.py       # Search and discovery
│   ├── batch_service.py        # Bulk operations
│   ├── zip_service.py          # Archive operations
│   ├── utility_service.py      # Hashing, cleanup, comparison
│   └── security_service.py     # Path validation and security
│
└── server.log                   # Server logs (generated)
```

### Service Architecture

- **File Service**: Core file I/O operations with complete path handling
- **Search Service**: Pattern matching, file discovery, and tree generation
- **Batch Service**: Optimized bulk operations with atomic transactions
- **ZIP Service**: Archive creation, extraction, and inspection
- **Utility Service**: Hashing, deduplication, analysis, and cleanup
- **Security Service**: Path traversal prevention and access validation

---

## 🧪 Testing the Server

### Using MCP Inspector

The MCP Inspector is an interactive testing tool for MCP servers:

```bash
# Terminal 1: Start the File Manager MCP server
python main.py

# Terminal 2: Open MCP Inspector
npx @modelcontextprotocol/inspector @modelcontextprotocol/inspector
```

Then connect to `http://localhost:8000/mcp`

### Testing Workflow

1. **Health Check**: Call `health_check_tool` → verify server is running
2. **Tool Discovery**: Call `available_tools_tool` → list all 34 tools
3. **List Files**: Call `list_files_tool` with `path: "."` → verify file listing
4. **Tree View**: Call `tree_view_tool` → generate directory tree
5. **Create File**: Call `create_file_tool` → create test file
6. **Clean Up**: Call `delete_file_tool` → remove test file

### Using curl for Basic Testing

```bash
# Check health
curl http://localhost:8000/health

# Verify MCP endpoint
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -d '{"method":"tools/list"}'
```

---

## 🔒 Security Considerations

### Local Execution Security

Since File Manager MCP runs **locally on your machine**, security is paramount:

#### Path Validation
- All paths are validated to prevent `../` directory traversal attacks
- Symbolic links are resolved and validated
- Only absolute paths are accepted internally

#### Access Control
- **Optional Base Directory Restriction**: Configure `ALLOWED_BASE_DIRS` to limit operations to specific directories
- **Permission Checks**: Respects system filesystem permissions
- **Request Validation**: All parameters are validated before execution

#### Best Practices

```python
# ✅ DO: Use absolute paths
await client.call_tool("create_file_tool", {
    "path": "/home/user/documents/file.txt",
    "content": "safe"
})

# ✅ DO: Restrict base directories in .env
# ALLOWED_BASE_DIRS=/home/user:/tmp

# ✅ DO: Enable path validation
# ENABLE_PATH_VALIDATION=true

# ❌ DON'T: Use user-provided paths directly
user_input = request.args.get('path')
await client.call_tool("read_file_tool", {"path": user_input})

# ❌ DON'T: Trust relative paths
await client.call_tool("delete_file_tool", {"path": "../../../etc/passwd"})
```

### Deployment Security Checklist

When using this server:

- [ ] Run on localhost only (`MCP_HOST=127.0.0.1`)
- [ ] Enable path validation (`ENABLE_PATH_VALIDATION=true`)
- [ ] Configure allowed directories (`ALLOWED_BASE_DIRS`)
- [ ] Enable request logging (`ENABLE_REQUEST_LOGGING=true`)
- [ ] Review logs regularly for suspicious activity
- [ ] Keep Python and dependencies updated
- [ ] Restrict file permissions on `.env` file (600)

---

## 💡 Why Filesystem MCP Servers Run Locally

Filesystem MCP servers like File Manager MCP are designed to run locally for several important reasons:

### Security & Privacy
- **Direct Access**: AI assistants need direct access to your local filesystem
- **No Transmission**: Files never leave your machine or transit through external servers
- **Data Control**: Complete control over what files are accessed and when
- **Encryption**: Your data remains encrypted at rest on your machine

### Performance
- **Zero Network Latency**: Local execution eliminates network delays
- **Bandwidth Efficiency**: No need to transmit file contents over network
- **Instant Operations**: Direct filesystem access is orders of magnitude faster
- **Scalability**: Handle large files and directories without network constraints

### Reliability
- **Offline Capable**: Works without internet connection
- **No Server Dependency**: No external service can go down and break functionality
- **Guaranteed Availability**: Always available when your machine is running
- **Atomic Operations**: Direct filesystem access ensures data consistency

### Architecture
```
┌─────────────────────────────────┐
│  Your Machine (Local Execution) │
│  ┌─────────────────────────────┐│
│  │  Claude/Cursor/VS Code      ││
│  │         ↕ (IPC)             ││
│  │  File Manager MCP Server    ││
│  │         ↕ (Direct I/O)      ││
│  │    Your Local Filesystem    ││
│  └─────────────────────────────┘│
└─────────────────────────────────┘
```

This local-first architecture ensures:
- ✅ Maximum security and privacy
- ✅ Optimal performance
- ✅ Complete reliability
- ✅ Full data control

---

## 🛠️ Development & Contributing

### Local Development Setup

```bash
# Clone and setup
git clone https://github.com/parthRana26/file-manager-mcp.git
cd file-manager-mcp

# Create virtual environment
uv venv
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt

# Run with debug logging
LOG_LEVEL=DEBUG python main.py
```

### Development Guidelines

- **Code Style**: Follow PEP 8 standards
- **Error Handling**: Provide meaningful error messages
- **Logging**: Add appropriate log statements for debugging
- **Testing**: Write tests for new functionality
- **Documentation**: Update docstrings and README as needed

### Contributing

We welcome contributions! To contribute:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature`
3. **Make your changes** with clear, descriptive commits
4. **Push to your fork**: `git push origin feature/your-feature`
5. **Open a Pull Request** with detailed description

### Reporting Issues

Found a bug? Please report it with:
- Detailed description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Environment details (Python version, OS)
- Relevant error messages or logs

---

## 📖 Project Structure Documentation

### File Organization

```
├── main.py
│   └─ FastMCP server initialization
│   └─ Tool registration (34 tools)
│   └─ Error handling with safe_execute wrapper
│   └─ Server startup on port 8000
│
├── services/file_service.py
│   └─ list_files() → Directory listing
│   └─ create_file() → File creation
│   └─ read_file() → File reading
│   └─ update_file() → File overwrite
│   └─ append_file() → File append
│   └─ delete_file() → File deletion
│   └─ [rename, move, copy] → File operations
│   └─ [create, delete]_directory() → Directory ops
│
├── services/search_service.py
│   └─ search_files() → Pattern matching
│   └─ get_file_info() → File metadata
│   └─ get_directory_info() → Directory stats
│   └─ tree_view() → Directory tree
│
├── services/batch_service.py
│   └─ batch_create_files() → Multiple file creation
│   └─ batch_delete_files() → Multiple file deletion
│   └─ batch_move_files() → Multiple file moves
│   └─ [copy, rename]_files() → Batch operations
│   └─ [create, delete]_directories() → Batch dirs
│
├── services/zip_service.py
│   └─ create_zip() → Archive creation
│   └─ extract_zip() → Archive extraction
│   └─ list_zip_contents() → Archive listing
│
├── services/utility_service.py
│   └─ find_large_files() → Size analysis
│   └─ file_hash() → Hash generation
│   └─ duplicate_file_finder() → Duplicate detection
│   └─ compare_files() → File comparison
│   └─ compare_directories() → Directory comparison
│   └─ clean_empty_directories() → Cleanup
│   └─ clean_temp_files() → Temp file removal
│
└── services/security_service.py
    └─ validate_path() → Path traversal prevention
    └─ check_permissions() → Permission validation
    └─ resolve_symlinks() → Symlink handling
```

---

## 📄 License

File Manager MCP is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for complete details.

### Quick Summary

The MIT License permits you to:
- ✅ Use, modify, and distribute this software
- ✅ Use it for commercial and private purposes
- ✅ Include it in proprietary applications

With the conditions:
- 📋 Include a copy of the license and copyright notice
- 📋 State significant changes made to the software

---

## 🎯 Quick Reference

### Starting the Server
```bash
python main.py
```

### Testing Health
```bash
curl http://localhost:8000/health
```

### MCP Endpoint
```
http://localhost:8000/mcp
```

### Environment Setup
Create `.env` with:
```
MCP_PORT=8000
LOG_LEVEL=INFO
ENABLE_PATH_VALIDATION=true
```

### Adding to Claude Desktop
Edit `~/.config/Claude/claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "file-manager": {
      "command": "python",
      "args": ["-m", "uvicorn", "main:mcp"],
      "cwd": "/path/to/file-manager-mcp"
    }
  }
}
```

---

## 📞 Support & Resources

- **GitHub Issues**: [Report bugs or request features](https://github.com/parthRana26/file-manager-mcp/issues)
- **MCP Documentation**: [modelcontextprotocol.io](https://modelcontextprotocol.io/)
- **FastMCP Guide**: [FastMCP on GitHub](https://github.com/jreichel/fastmcp)
- **Python Docs**: [Python asyncio](https://docs.python.org/3/library/asyncio.html)

---

## 👨‍💻 Author

**Parth Rana**

- **GitHub**: [github.com/parthRana26](https://github.com/parthRana26)
- **Repository**: [file-manager-mcp](https://github.com/parthRana26/file-manager-mcp)

A software engineer passionate about building robust tools for AI applications and local-first systems.

---

**Made with ❤️ for the AI and MCP community**
