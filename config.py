from pathlib import Path

WORKSPACE_DIR = Path("workspace").resolve()

ALLOWED_EXTENSIONS = {
    ".txt",
    ".md",
    ".json",
    ".csv",
    ".py",
    ".js",
    ".html",
    ".css"
}

MAX_FILE_SIZE_MB = 5