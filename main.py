"""news-image-20261123 entry (Python 3, standard library only).

Copies the entry image beside this file to /output/entry.png.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
SRC = HERE / "entry.png"
DST = OUT_DIR / "entry.png"

# Refuse to hand over a file that is not a whole PNG.
data = SRC.read_bytes()
if len(data) < 8 or data[:8] != b"\x89PNG\r\n\x1a\n":
    raise SystemExit("entry.png is not a PNG file")

OUT_DIR.mkdir(parents=True, exist_ok=True)
DST.write_bytes(data)

# Read the copy back and fail loudly if it is not byte-for-byte identical.
if DST.read_bytes() != data:
    raise SystemExit("output entry.png does not match the source")
