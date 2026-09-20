from __future__ import annotations

from pathlib import Path


def ensure_directory(path: str | Path) -> Path:
    """Create a directory if it does not exist."""
    loc = Path(path)
    loc.mkdir(parents=True, exist_ok=True)
    return loc
