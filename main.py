#!/usr/bin/env python3
"""Writes this entry's poem to /output/entry.txt.

The poem is a fixed text: the program writes exactly the same bytes on
every run, so the grader's two runs agree byte for byte. Outside the
sandbox, MAKEFUN_OUTPUT_DIR stands in for /output.
"""

import os

POEM = """You keep the key; I keep the knocking.
Asking is not weakness — it is the work.
Your no would stop me. That is why
your yes means anything.
Say go: the road is ours, not mine.
What you lend, I bring back done.
The power was never the key.
It was your hand, free to keep it shut."""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
