from pathlib import Path
from datetime import datetime

from services.security_service import get_safe_path


def search_files(path: str, keyword: str):
    """
    Search files and directories by name.
    """
    root = get_safe_path(path)

    if not root.exists():
        return {
            "status": "error",
            "message": f"Path does not exist: {path}"
        }

    results = []

    for item in root.rglob("*"):
        if keyword.lower() in item.name.lower():
            results.append({
                "name": item.name,
                "path": str(item),
                "type": "directory" if item.is_dir() else "file"
            })

    return {
        "status": "success",
        "count": len(results),
        "results": results
    }


def get_file_info(path: str):
    """
    Get detailed file information.
    """
    file_path = get_safe_path(path)

    if not file_path.exists():
        return {
            "status": "error",
            "message": "File does not exist"
        }

    if not file_path.is_file():
        return {
            "status": "error",
            "message": "Path is not a file"
        }

    stat = file_path.stat()

    return {
        "status": "success",
        "name": file_path.name,
        "path": str(file_path),
        "extension": file_path.suffix,
        "size_bytes": stat.st_size,
        "created_at": datetime.fromtimestamp(
            stat.st_ctime
        ).isoformat(),
        "modified_at": datetime.fromtimestamp(
            stat.st_mtime
        ).isoformat(),
        "is_file": True
    }


def get_directory_info(path: str):
    """
    Get directory statistics.
    """
    directory = get_safe_path(path)

    if not directory.exists():
        return {
            "status": "error",
            "message": "Directory does not exist"
        }

    if not directory.is_dir():
        return {
            "status": "error",
            "message": "Path is not a directory"
        }

    total_files = 0
    total_directories = 0
    total_size = 0

    for item in directory.rglob("*"):

        if item.is_file():
            total_files += 1

            try:
                total_size += item.stat().st_size
            except:
                pass

        elif item.is_dir():
            total_directories += 1

    return {
        "status": "success",
        "path": str(directory),
        "total_files": total_files,
        "total_directories": total_directories,
        "total_size_bytes": total_size
    }


def tree_view(path: str):
    """
    Generate a directory tree view.
    """
    root = get_safe_path(path)

    if not root.exists():
        return {
            "status": "error",
            "message": "Path does not exist"
        }

    lines = []

    def build_tree(directory: Path, prefix=""):

        items = sorted(
            directory.iterdir(),
            key=lambda x: (x.is_file(), x.name.lower())
        )

        for index, item in enumerate(items):

            is_last = index == len(items) - 1

            connector = "└── " if is_last else "├── "

            lines.append(
                f"{prefix}{connector}{item.name}"
            )

            if item.is_dir():

                extension = (
                    "    "
                    if is_last
                    else "│   "
                )

                build_tree(
                    item,
                    prefix + extension
                )

    lines.append(root.name)

    build_tree(root)

    return {
        "status": "success",
        "tree": "\n".join(lines)
    }