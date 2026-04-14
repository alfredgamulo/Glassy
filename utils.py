import os
import sys
import shutil

BASE_DIR = os.path.dirname(__file__)


def resource_path(*parts):
    """Return an absolute path relative to the project base directory.

    Works when running normally and when packaged with PyInstaller (uses
    sys._MEIPASS when available).
    """
    base = getattr(sys, '_MEIPASS', None) or BASE_DIR
    if len(parts) == 0:
        return base
    return os.path.join(base, *parts)


def get_executable(name: str) -> str:
    """Return an executable path for `name` on Linux.

    Lookup order:
    1. System `PATH` (shutil.which)
    2. `$PLATFORM_TOOLS/<name>` if `PLATFORM_TOOLS` env var is set
    3. `~/Android/Sdk/platform-tools/<name>` (default requested path)
    4. Packaged `platform_tools/<name>` next to the project
    5. Fallback to `name` (let caller handle failures)
    """
    # 1. system PATH
    exe = shutil.which(name)
    if exe:
        return exe

    # 2. environment override
    platform_tools_env = os.environ.get("PLATFORM_TOOLS")
    if platform_tools_env:
        candidate = os.path.join(os.path.expanduser(platform_tools_env), name)
        if os.path.exists(candidate) and os.access(candidate, os.X_OK):
            return candidate

    # 3. default Android SDK platform-tools path (per user request)
    default_sdk = os.path.expanduser("~/Android/Sdk/platform-tools")
    candidate = os.path.join(default_sdk, name)
    if os.path.exists(candidate) and os.access(candidate, os.X_OK):
        return candidate

    # 4. packaged copy next to the project
    candidate = os.path.join(BASE_DIR, 'platform_tools', name)
    if os.path.exists(candidate) and os.access(candidate, os.X_OK):
        return candidate

    # 5. final fallback
    return name
