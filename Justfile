set shell := ["bash", "-cu"]


install:
    uv venv .venv
    uv pip install -r requirements.txt --python .venv

run:
    export PLATFORM_TOOLS=${PLATFORM_TOOLS:-$HOME/Android/Sdk/platform-tools};\
    .venv/bin/python main.py

adb *ARGS:
    export PLATFORM_TOOLS=${PLATFORM_TOOLS:-$HOME/Android/Sdk/platform-tools};\
    "$PLATFORM_TOOLS/adb" {{ARGS}}

adb-devices:
    export PLATFORM_TOOLS=${PLATFORM_TOOLS:-$HOME/Android/Sdk/platform-tools};\
    "$PLATFORM_TOOLS/adb" devices

adb-install APP:
    export PLATFORM_TOOLS=${PLATFORM_TOOLS:-$HOME/Android/Sdk/platform-tools};\
    "$PLATFORM_TOOLS/adb" install {{APP}}

adb-setup:
    echo "Install platform-tools for your distro:"
    echo "  Debian/Ubuntu: sudo apt install android-tools-adb android-tools-fastboot"
    echo "  Arch: sudo pacman -S android-tools"
    echo "Or download from: https://developer.android.com/studio/releases/platform-tools"
    echo "Then set PLATFORM_TOOLS env var to the folder, e.g.:"
    echo "  export PLATFORM_TOOLS=~/Android/Sdk/platform-tools"
    echo "Test with: just adb-devices"
