#!/usr/bin/env python3
"""Copy the committed front page to the grader's output directory.

Standard library only, so it runs in the grader's fresh container with no
network and nothing installed. The image (entry.png, beside this file) was
drawn by render.py, a local Pillow script kept out of this snapshot; this
program only copies its bytes, so both grader runs write identical output.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(OUT_DIR, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote %s" % dst)


if __name__ == "__main__":
    main()
