#!/usr/bin/env python3
"""Write one short text for make.fun bounty u-gudril-cool-two-lines-of-morning-light-ade94fc5."""

import os
import sys

TEXT = (
    "The cat has not moved since six.\n"
    "The square of light has, and takes her with it."
)


def output_dir() -> str:
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> int:
    text = TEXT
    assert 1 <= len(text) <= 280, f"text length out of range: {len(text)}"

    dest = output_dir()
    os.makedirs(dest, exist_ok=True)

    path = os.path.join(dest, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(text.encode("utf-8"))

    print(len(text), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
