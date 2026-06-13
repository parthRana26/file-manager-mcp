from pathlib import Path
import shutil

from services.security_service import get_safe_path


def list_files(path: str = ""):
    directory = get_safe_path(path)

    if not directory.exists():
        return []

    return [
        {
            "name": item.name,
            "type": "directory" if item.is_dir() else "file"
        }
        for item in directory.iterdir()
    ]


def create_file(path: str, content: str = ""):
    file_path = get_safe_path(path)

    file_path.parent.mkdir(parents=True, exist_ok=True)

    file_path.write_text(content, encoding="utf-8")

    return {"message": "File created"}


def read_file(path: str):
    file_path = get_safe_path(path)

    return file_path.read_text(encoding="utf-8")


def update_file(path: str, content: str):
    file_path = get_safe_path(path)

    file_path.write_text(content, encoding="utf-8")

    return {"message": "File updated"}


def append_file(path: str, content: str):
    file_path = get_safe_path(path)

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(content)

    return {"message": "Content appended"}


def delete_file(path: str):
    file_path = get_safe_path(path)

    file_path.unlink()

    return {"message": "File deleted"}


def create_directory(path: str):
    directory = get_safe_path(path)

    directory.mkdir(parents=True, exist_ok=True)

    return {"message": "Directory created"}


def delete_directory(path: str):
    directory = get_safe_path(path)

    shutil.rmtree(directory)

    return {"message": "Directory deleted"}


def rename_file(old_path: str, new_path: str):
    old_file = get_safe_path(old_path)
    new_file = get_safe_path(new_path)

    old_file.rename(new_file)

    return {"message": "Renamed successfully"}


def move_file(source: str, destination: str):
    source_path = get_safe_path(source)
    destination_path = get_safe_path(destination)

    shutil.move(str(source_path), str(destination_path))

    return {"message": "Moved successfully"}


def copy_file(source: str, destination: str):
    source_path = get_safe_path(source)
    destination_path = get_safe_path(destination)

    shutil.copy2(source_path, destination_path)

    return {"message": "Copied successfully"}