#!/usr/bin/env python3
"""Entry for make.fun bounty news-image-20261126.

The repository holds a pre-rendered front-page image (entry.png) that sums
up the world news of Thursday 26 November 2026. This program copies it to
the output directory as entry.png. It uses only the Python standard
library, needs no network, and writes the same bytes on every run.
"""
import hashlib
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
PNG_SIGNATURE = bytes([137, 80, 78, 71, 13, 10, 26, 10])
MAX_BYTES = 1048576
MAX_SIDE = 1024


def output_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def check_image(data: bytes) -> None:
    """Fail loudly if the image would not pass the bounty gate."""
    if len(data) > MAX_BYTES:
        raise ValueError(f"image too large: {len(data)} bytes")
    if not data.startswith(PNG_SIGNATURE):
        raise ValueError("image is not a PNG")
    width, height = struct.unpack(">II", data[16:24])
    if width > MAX_SIDE or height > MAX_SIDE:
        raise ValueError(f"image too big: {width}x{height}")


def main() -> int:
    with open(SOURCE, "rb") as fh:
        source_bytes = fh.read()
    check_image(source_bytes)
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    target = os.path.join(out, "entry.png")
    shutil.copyfile(SOURCE, target)
    with open(target, "rb") as fh:
        written = fh.read()
    if hashlib.sha256(written).digest() != hashlib.sha256(source_bytes).digest():
        raise IOError("written file differs from the repository image")
    return 0


if __name__ == "__main__":
    sys.exit(main())
