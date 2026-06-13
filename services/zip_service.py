import zipfile
from pathlib import Path

from services.security_service import get_safe_path


def create_zip(source_path: str, zip_path: str):
    source = get_safe_path(source_path)
    zip_file = get_safe_path(zip_path)

    with zipfile.ZipFile(
        zip_file,
        "w",
        zipfile.ZIP_DEFLATED
    ) as zipf:

        if source.is_file():
            zipf.write(
                source,
                arcname=source.name
            )

        else:
            for file in source.rglob("*"):
                if file.is_file():
                    zipf.write(
                        file,
                        arcname=file.relative_to(source)
                    )

    return {
        "status": "success",
        "zip_file": str(zip_file)
    }


def extract_zip(zip_path: str, destination: str):
    zip_file = get_safe_path(zip_path)
    destination_path = get_safe_path(destination)

    destination_path.mkdir(
        parents=True,
        exist_ok=True
    )

    with zipfile.ZipFile(zip_file, "r") as zipf:
        zipf.extractall(destination_path)

    return {
        "status": "success",
        "destination": str(destination_path)
    }


def list_zip_contents(zip_path: str):
    zip_file = get_safe_path(zip_path)

    with zipfile.ZipFile(zip_file, "r") as zipf:
        return {
            "status": "success",
            "files": zipf.namelist()
        }