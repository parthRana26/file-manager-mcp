import shutil
from pathlib import Path

from services.security_service import get_safe_path


def batch_create_files(files: list):
    created = []
    failed = []

    for file_data in files:
        try:
            path = get_safe_path(file_data["path"])
            content = file_data.get("content", "")

            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

            created.append(str(path))

        except Exception as e:
            failed.append({
                "path": file_data.get("path"),
                "error": str(e)
            })

    return {
        "created_count": len(created),
        "failed_count": len(failed),
        "created": created,
        "failed": failed
    }


def batch_delete_files(paths: list):
    deleted = []
    failed = []

    for file_path in paths:
        try:
            path = get_safe_path(file_path)

            if path.exists() and path.is_file():
                path.unlink()

            deleted.append(str(path))

        except Exception as e:
            failed.append({
                "path": file_path,
                "error": str(e)
            })

    return {
        "deleted_count": len(deleted),
        "failed_count": len(failed),
        "deleted": deleted,
        "failed": failed
    }


def batch_move_files(operations: list):
    moved = []
    failed = []

    for operation in operations:
        try:
            source = get_safe_path(operation["source"])
            destination = get_safe_path(operation["destination"])

            destination.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            shutil.move(
                str(source),
                str(destination)
            )

            moved.append({
                "source": str(source),
                "destination": str(destination)
            })

        except Exception as e:
            failed.append({
                "operation": operation,
                "error": str(e)
            })

    return {
        "moved_count": len(moved),
        "failed_count": len(failed),
        "moved": moved,
        "failed": failed
    }


def batch_copy_files(operations: list):
    copied = []
    failed = []

    for operation in operations:
        try:
            source = get_safe_path(operation["source"])
            destination = get_safe_path(operation["destination"])

            destination.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            shutil.copy2(
                source,
                destination
            )

            copied.append({
                "source": str(source),
                "destination": str(destination)
            })

        except Exception as e:
            failed.append({
                "operation": operation,
                "error": str(e)
            })

    return {
        "copied_count": len(copied),
        "failed_count": len(failed),
        "copied": copied,
        "failed": failed
    }


def batch_rename_files(operations: list):
    renamed = []
    failed = []

    for operation in operations:
        try:
            old_path = get_safe_path(
                operation["old_path"]
            )

            new_path = get_safe_path(
                operation["new_path"]
            )

            old_path.rename(new_path)

            renamed.append({
                "old_path": str(old_path),
                "new_path": str(new_path)
            })

        except Exception as e:
            failed.append({
                "operation": operation,
                "error": str(e)
            })

    return {
        "renamed_count": len(renamed),
        "failed_count": len(failed),
        "renamed": renamed,
        "failed": failed
    }


def batch_create_directories(paths: list):
    created = []
    failed = []

    for directory_path in paths:
        try:
            path = get_safe_path(directory_path)

            path.mkdir(
                parents=True,
                exist_ok=True
            )

            created.append(str(path))

        except Exception as e:
            failed.append({
                "path": directory_path,
                "error": str(e)
            })

    return {
        "created_count": len(created),
        "failed_count": len(failed),
        "created": created,
        "failed": failed
    }


def batch_delete_directories(paths: list):
    deleted = []
    failed = []

    for directory_path in paths:
        try:
            path = get_safe_path(directory_path)

            shutil.rmtree(path)

            deleted.append(str(path))

        except Exception as e:
            failed.append({
                "path": directory_path,
                "error": str(e)
            })

    return {
        "deleted_count": len(deleted),
        "failed_count": len(failed),
        "deleted": deleted,
        "failed": failed
    }