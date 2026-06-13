import hashlib
from pathlib import Path

from services.security_service import get_safe_path


def find_large_files(path: str, min_size_mb: float):
    root = get_safe_path(path)

    results = []

    min_size_bytes = min_size_mb * 1024 * 1024

    for file in root.rglob("*"):
        if file.is_file():
            try:
                size = file.stat().st_size

                if size >= min_size_bytes:
                    results.append({
                        "path": str(file),
                        "size_mb": round(
                            size / (1024 * 1024),
                            2
                        )
                    })

            except Exception:
                pass

    return {
        "count": len(results),
        "files": results
    }


def file_hash(
    path: str,
    algorithm: str = "sha256"
):
    file_path = get_safe_path(path)

    hash_algorithms = {
        "md5": hashlib.md5,
        "sha1": hashlib.sha1,
        "sha256": hashlib.sha256
    }

    if algorithm.lower() not in hash_algorithms:
        return {
            "error": "Unsupported algorithm"
        }

    hasher = hash_algorithms[
        algorithm.lower()
    ]()

    with open(file_path, "rb") as f:

        while chunk := f.read(8192):
            hasher.update(chunk)

    return {
        "path": str(file_path),
        "algorithm": algorithm,
        "hash": hasher.hexdigest()
    }


def duplicate_file_finder(path: str):
    root = get_safe_path(path)

    hashes = {}

    duplicates = []

    for file in root.rglob("*"):

        if file.is_file():

            try:
                hash_value = file_hash(
                    str(file)
                )["hash"]

                hashes.setdefault(
                    hash_value,
                    []
                ).append(
                    str(file)
                )

            except Exception:
                pass

    for files in hashes.values():

        if len(files) > 1:
            duplicates.append(files)

    return {
        "duplicate_groups": len(
            duplicates
        ),
        "duplicates": duplicates
    }


def compare_files(
    file1: str,
    file2: str
):
    path1 = get_safe_path(file1)
    path2 = get_safe_path(file2)

    hash1 = file_hash(
        str(path1)
    )["hash"]

    hash2 = file_hash(
        str(path2)
    )["hash"]

    return {
        "file1": str(path1),
        "file2": str(path2),
        "identical": hash1 == hash2
    }


def compare_directories(
    dir1: str,
    dir2: str
):
    path1 = get_safe_path(dir1)
    path2 = get_safe_path(dir2)

    files1 = {
        str(
            file.relative_to(path1)
        )
        for file in path1.rglob("*")
        if file.is_file()
    }

    files2 = {
        str(
            file.relative_to(path2)
        )
        for file in path2.rglob("*")
        if file.is_file()
    }

    return {
        "only_in_dir1": sorted(
            list(files1 - files2)
        ),
        "only_in_dir2": sorted(
            list(files2 - files1)
        ),
        "common_files": sorted(
            list(files1 & files2)
        )
    }


def clean_empty_directories(
    path: str
):
    root = get_safe_path(path)

    removed = []

    directories = sorted(
        [
            d
            for d in root.rglob("*")
            if d.is_dir()
        ],
        reverse=True
    )

    for directory in directories:

        try:
            if not any(
                directory.iterdir()
            ):
                directory.rmdir()

                removed.append(
                    str(directory)
                )

        except Exception:
            pass

    return {
        "removed_count": len(
            removed
        ),
        "removed": removed
    }


def clean_temp_files(path: str):
    root = get_safe_path(path)

    temp_extensions = {
        ".tmp",
        ".log",
        ".cache"
    }

    deleted = []

    for file in root.rglob("*"):

        if (
            file.is_file()
            and file.suffix.lower()
            in temp_extensions
        ):
            try:
                file.unlink()

                deleted.append(
                    str(file)
                )

            except Exception:
                pass

    return {
        "deleted_count": len(
            deleted
        ),
        "deleted": deleted
    }