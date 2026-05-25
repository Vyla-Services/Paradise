# Paradise — Universal Pack System for OGFN & Unreal Engine

Paradise is a high‑performance, engine‑agnostic packer/unpacker designed for:

- OGFN content distribution
- Unreal Engine / UEFN asset pipelines
- Game launchers and backend systems
- Modding ecosystems
- General game development workflows

Paradise provides:

- A custom `.pak` archive format
- Multiple compression backends (zlib, lz4, zstd)
- SHA‑256 integrity verification
- Optional AES‑GCM encryption
- A full CLI tool
- A full GUI (Qt / PySide6)
- A Python SDK for UE + OGFN integration

Paradise is built to be fast, simple, and production‑ready.

---

## Features

- Pack folders into `.pak` archives
- Extract `.pak` archives
- Inspect file tables
- Verify integrity
- Multiple compression algorithms
- Optional AES encryption
- Full GUI (Qt)
- Full CLI
- SDK for Unreal Engine & OGFN
- Clean, extensible architecture

---

## Installation

### 1. Install Python 3.10+

Check version:

python --version

Code

---

### 2. Install Dependencies

Paradise uses:

- PySide6 (UI)
- lz4
- zstandard
- pycryptodome

Install everything:

pip install -r requirements.txt

Code

Or manually:

pip install PySide6 lz4 zstandard pycryptodome

Code

---

### 3. Install Paradise (Development Mode)

From the project root:

pip install -e .

Code

This makes the `paradise` CLI globally available.

---

## CLI Usage

### Pack a folder

paradise pack Content out.pak

Code

With compression options:

paradise pack Content out.pak --compression zstd --level 10

Code

### Extract a pack

paradise extract out.pak Extracted/

Code

### List contents

paradise list out.pak

Code

### Verify integrity

paradise verify out.pak

Code

---

## Using the Paradise UI

Run the UI:

python -m paradise_ui.app

Code

The UI includes:

- Pack panel
- Extract panel
- Inspector panel
- Dark theme
- Qt interface

---

## How Paradise Works

Paradise uses a simple, fast binary format:

### 1. Header
- Magic: `PARADISE`
- Version
- File count

### 2. File Table
For each file:
- Path
- Compression type
- Offset
- Raw size
- Compressed size
- SHA‑256 hash

### 3. Data Block
All compressed file data stored back‑to‑back.

### Compression Backends
- zlib (default)
- lz4 (fast)
- zstd (best ratio)

### Integrity
Every file is hashed with SHA‑256.

### Encryption (Optional)
AES‑GCM per file.

---

## Paradise SDK

Paradise includes a Python SDK for:

### Unreal Engine
- Export Paradise packs into `/Content`
- Load assets virtually
- Use Paradise packs as external content sources

### OGFN
- Stream assets from packs
- Read manifests
- Hot‑patch content
- Integrate with launchers and backends

Example:

```python
from paradise_sdk import ParadiseLoader

loader = ParadiseLoader("Season1.pak")
data = loader.load_binary("Textures/UI/button.png")
Building Paradise Into an EXE
Paradise can be compiled into standalone Windows executables using PyInstaller.

Build CLI:
Code
pyinstaller --onefile paradise_cli/main.py --name paradise
Build UI:
Code
pyinstaller --onefile paradise_ui/app.py --name Paradise
The EXEs will appear in:

Code
dist/
    paradise.exe
    Paradise.exe