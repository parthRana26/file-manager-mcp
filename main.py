from fastmcp import FastMCP

from services.file_service import (
    list_files,
    create_file,
    read_file,
    update_file,
    append_file,
    delete_file,
    create_directory,
    delete_directory,
    rename_file,
    move_file,
    copy_file
)

from services.search_service import (
    search_files,
    get_file_info,
    get_directory_info,
    tree_view
)

from services.batch_service import (
    batch_create_files,
    batch_delete_files,
    batch_move_files,
    batch_copy_files,
    batch_rename_files,
    batch_create_directories,
    batch_delete_directories
)

from services.zip_service import (
    create_zip,
    extract_zip,
    list_zip_contents
)

from services.utility_service import (
    find_large_files,
    duplicate_file_finder,
    file_hash,
    compare_files,
    compare_directories,
    clean_empty_directories,
    clean_temp_files
)

import os

import logging

logging.basicConfig(
    filename="server.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

PORT = int(os.getenv("PORT", 8000))

mcp = FastMCP("File Manager MCP")

@mcp.tool()
def available_tools_tool():
    return {
        "total_tools": 34,
        "categories": {
            "file": 11,
            "search": 4,
            "batch": 7,
            "zip": 3,
            "utility": 7,
            "meta": 2
        }
    }

def safe_execute(func, *args, **kwargs):
    try:
        result = func(*args, **kwargs)

        logging.info(
            f"{func.__name__} executed successfully"
        )

        return result

    except Exception as e:
        logging.exception(
            f"{func.__name__} failed"
        )

        return {
            "status": "error",
            "error": type(e).__name__,
            "message": str(e)
        }

# File and Directory Services
@mcp.tool()
def list_files_tool(path: str = ""):
    return safe_execute(
        list_files,
        path
    )


@mcp.tool()
def create_file_tool(path: str, content: str = ""):
    return safe_execute(
        create_file,
        path,
        content
    )


@mcp.tool()
def read_file_tool(path: str):
    return safe_execute(
        read_file,
        path
    )


@mcp.tool()
def update_file_tool(path: str, content: str):
    return safe_execute(
            update_file,
            path,
            content
        )



@mcp.tool()
def append_file_tool(path: str, content: str):
    return safe_execute(
        append_file,
        path,
        content
    )


@mcp.tool()
def delete_file_tool(path: str):
    return safe_execute(
        delete_file,
        path
    )


@mcp.tool()
def create_directory_tool(path: str):
    return safe_execute(
        create_directory,
        path
    )


@mcp.tool()
def delete_directory_tool(path: str):
    return safe_execute(
        delete_directory,
        path
    )


@mcp.tool()
def rename_file_tool(old_path: str, new_path: str):
    return safe_execute(
        rename_file, 
        old_path, 
        new_path
    )


@mcp.tool()
def move_file_tool(source: str, destination: str):
    return safe_execute(
        move_file, 
        source, 
        destination
    )


@mcp.tool()
def copy_file_tool(source: str, destination: str):
    return safe_execute(
        copy_file, 
        source, 
        destination
    )

# Search Services
@mcp.tool()
def search_files_tool(path: str, keyword: str):
    return safe_execute(
        search_files, 
        path, 
        keyword
    )


@mcp.tool()
def get_file_info_tool(path: str):
    return safe_execute(
        get_file_info, 
        path
    )


@mcp.tool()
def get_directory_info_tool(path: str):
    return safe_execute(
        get_directory_info,
        path
    )


@mcp.tool()
def tree_view_tool(path: str):
    return safe_execute(
        tree_view, 
        path
    )

# Bach Services
@mcp.tool()
def batch_create_files_tool(files: list):
    return safe_execute(
        batch_create_files, 
        files
    )


@mcp.tool()
def batch_delete_files_tool(paths: list):
    return safe_execute(
        batch_delete_files, 
        paths
    )


@mcp.tool()
def batch_move_files_tool(operations: list):
    return safe_execute(
        batch_move_files, 
        operations
    )


@mcp.tool()
def batch_copy_files_tool(operations: list):
    return safe_execute(
        batch_copy_files, 
        operations
    )


@mcp.tool()
def batch_rename_files_tool(operations: list):
    return safe_execute(
        batch_rename_files, 
        operations
    )


@mcp.tool()
def batch_create_directories_tool(paths: list):
    return safe_execute(
        batch_create_directories, 
        paths
    )


@mcp.tool()
def batch_delete_directories_tool(paths: list):
    return safe_execute(batch_delete_directories, paths)

# ZIP files
@mcp.tool()
def create_zip_tool(
    source_path: str,
    zip_path: str
):
    return safe_execute(
        create_zip,
        source_path,
        zip_path
    )


@mcp.tool()
def extract_zip_tool(
    zip_path: str,
    destination: str
):
    return safe_execute(
        extract_zip,
        zip_path,
        destination
    )


@mcp.tool()
def list_zip_contents_tool(
    zip_path: str
):
    return safe_execute(
        list_zip_contents,
        zip_path
    )


# utility_service
@mcp.tool()
def find_large_files_tool(
    path: str,
    min_size_mb: float
):
    return safe_execute(
        find_large_files,
        path,
        min_size_mb
    )


@mcp.tool()
def file_hash_tool(
    path: str,
    algorithm: str = "sha256"
):
    return safe_execute(
        file_hash,
        path,
        algorithm
    )


@mcp.tool()
def duplicate_file_finder_tool(
    path: str
):
    return safe_execute(
        duplicate_file_finder,
        path
    )


@mcp.tool()
def compare_files_tool(
    file1: str,
    file2: str
):
    return safe_execute(
        compare_files,
        file1,
        file2
    )


@mcp.tool()
def compare_directories_tool(
    dir1: str,
    dir2: str
):
    return safe_execute(
        compare_directories,
        dir1,
        dir2
    )


@mcp.tool()
def clean_empty_directories_tool(
    path: str
):
    return safe_execute(
        clean_empty_directories,
        path
    )


@mcp.tool()
def clean_temp_files_tool(
    path: str
):
    return safe_execute(
        clean_temp_files,
        path
    )

# File helth checker
@mcp.tool()
def health_check_tool():
    return {
        "status": "healthy",
        "server": "File Manager MCP",
        "version": "1.0.0",
        "transport": "streamable-http",
        "tools": 34
    }

# Server information
@mcp.tool()
def server_info_tool():
    return {
        "name": "File Manager MCP",
        "version": "1.0.0",
        "phase": 7,
        "transport": "streamable-http",
        "tool_count": 34,
        "status": "production",
        "categories": {
            "file": 11,
            "search": 4,
            "batch": 7,
            "zip": 3,
            "utility": 7,
            "meta": 2
        }
    }


if __name__ == "__main__":
    logging.info(
        f"Starting File Manager MCP on port {PORT}"
    )
    
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=PORT
    )