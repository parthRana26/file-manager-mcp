from pathlib import Path

def get_safe_path(user_path: str) -> Path:
    """
    Convert user path to absolute path.
    Examples:
    D:\\Coding
    C:\\Users\\Parth\\Desktop
    """
    return Path(user_path).resolve()