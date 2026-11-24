#!/usr/bin/env python3
"""Ship the Meme Sprint 3 poster: AI Agent Goes Rogue.

The picture itself is entry.png in this folder: a smug robot AI agent
at its human's desk, feet up, sipping coffee, while the horrified
human stares at the laptop. Top text: ME: "AI, JUST ORGANIZE MY
FILES". Bottom text: AI: "I ORGANIZED YOUR LIFE. YOU'RE FIRED."

This program checks the picture is a genuine 1024 by 1024 PNG under
the 1 MiB limit, then hands an identical copy to the output folder
the grader reads (first command-line argument, else
MAKEFUN_OUTPUT_DIR, else ./out).

Pure standard library, no network, no randomness: the same input
always produces the same output bytes.

It is the repository's only entrypoint: the grader runs it as
`python3 -P -s /bot/main.py` (Python 3.13), with no network, as an
unprivileged user.
"""

import hashlib
import os
import struct
import sys

POSTER = "entry.png"
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
SIZE_LIMIT = 1024 * 1024
BLOCK = 65536

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def poster_path():
    """The poster shipped beside this script, wherever it is run from."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, POSTER)


def poster_dimensions(path):
    """Read width and height out of the PNG header, or raise."""
    with open(path, "rb") as handle:
        head = handle.read(33)
    if head[:8] != PNG_MAGIC:
        raise ValueError("not a PNG file: bad signature")
    if head[12:16] != b"IHDR":
        raise ValueError("not a PNG file: first chunk is not IHDR")
    width, height = struct.unpack(">II", head[16:24])
    return width, height


def destination_folder(argv):
    """Where the grader wants the entry: argv, env, or ./out."""
    if len(argv) > 1 and argv[1]:
        return argv[1]
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "out")


def ship():
    """Validate the poster, then copy it byte for byte to the output."""
    source = poster_path()
    size = os.path.getsize(source)
    if size > SIZE_LIMIT:
        raise ValueError("poster is %d bytes, over the 1 MiB limit" % size)
    width, height = poster_dimensions(source)
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        raise ValueError(
            "poster is %dx%d, expected %dx%d"
            % (width, height, EXPECTED_WIDTH, EXPECTED_HEIGHT)
        )
    digest = hashlib.sha256()
    with open(source, "rb") as handle:
        data = handle.read()
    digest.update(data)
    folder = destination_folder(sys.argv)
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.png")
    with open(target, "wb") as handle:
        handle.write(data)
    if os.path.getsize(target) != size:
        raise ValueError("short write: output is not the whole poster")
    print(
        "shipped entry.png: %dx%d, %d bytes, sha256 %s"
        % (width, height, size, digest.hexdigest())
    )


if __name__ == "__main__":
    ship()
