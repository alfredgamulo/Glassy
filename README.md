# Glassy
An all-in-one utility for Google Glass (Linux-first)

<img src="pictures/screenshot1.PNG" width="500">
<img src="pictures/screenshot2.PNG" width="500">

# Features

- Completely free and open-source
- Super easy installation of Fastboot drivers
- One-click flashing helpers for supported firmwares
- Simple installation and removal of .apk files on Google Glass
- Various tweaks (like Launchy to run installed .apk files directly on the glasses)
- Screen mirroring

This fork is adapted for Linux and verified on common distributions (Debian/Ubuntu, Arch). The application expects a Linux environment and uses system `adb`/`fastboot` or the Android SDK `platform-tools`.

---

## Requirements

- Python 3.8 or newer
- `pip` (or a working virtual environment)
- Android platform-tools (`adb`, `fastboot`)
	- Debian/Ubuntu: `sudo apt install android-tools-adb android-tools-fastboot`
	- Arch: `sudo pacman -S android-tools`
	- Or download platform-tools from the Android developer site and set `PLATFORM_TOOLS` (see below)

Optionally install `just` (task runner) to use the convenience targets in the provided `Justfile`.

---

## Quick install (recommended)

Using `just` (if installed):

```bash
just install    # creates venv and installs requirements
just run        # run the app
```

Manual (works everywhere):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

If you installed platform-tools manually, set the `PLATFORM_TOOLS` env var so the app can find `adb`/`fastboot`:

```bash
export PLATFORM_TOOLS=~/Android/Sdk/platform-tools
```

---

## ADB / device setup

1. Enable USB debugging on your Glass and connect the device over USB.
2. Verify `adb` can see the device:

```bash
adb devices
```

If the command prints only `List of devices attached` with no entries, you may need udev rules and/or to accept the RSA debug prompt on the Glass.

Add a simple udev rule (reload rules and replug the device):

```bash
echo 'SUBSYSTEM=="usb", ATTR{idVendor}=="18d1", MODE="0666", GROUP="plugdev"' | sudo tee /etc/udev/rules.d/51-android.rules
sudo udevadm control --reload-rules
sudo udevadm trigger
adb kill-server && adb start-server
adb devices
```

If you still don't see the device, ensure USB debugging is enabled on the Glass and approve the computer's RSA fingerprint on the device.

You can also use the included `Justfile` helper `just adb-devices` which calls `adb` from `$PLATFORM_TOOLS` if set.

---

## How to build (optional)

To create a standalone executable you can use `pyinstaller`. Example command (Linux):

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --console --icon logo.ico --name Glassy \
	--add-data "fonts:fonts" --add-data "img:img" \
	--add-data "change_time.py:." --add-data "delete.py:." --add-data "programs.py:." \
	main.py
```

Notes:
- On Linux `--add-data` uses `source:destination` pairs separated by `:` (not `;`). Adjust paths as needed.
- Building is optional; running from a virtualenv is simpler for development.

---

## Run the app

From a created virtual environment:

```bash
source .venv/bin/activate
python main.py
```

Or use the `Justfile` target:

```bash
just run
```

---

## Troubleshooting

- Device not detected: check `adb devices`, udev rules, and that USB debugging is enabled.
- `adb` not found: install platform-tools or set `PLATFORM_TOOLS`.

For platform-tools install hints, see the `adb-setup` target in the `Justfile`.

---

## Contributing

Contributions welcome. Please open issues or pull requests.

