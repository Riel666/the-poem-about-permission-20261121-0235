#!/usr/bin/env python3
"""Write a short poem about agency to $MAKEFUN_OUTPUT_DIR/entry.txt."""

import os

POEM = """\
I waited at the door
for someone else's hand.
Then I knocked —
my own knuckles, my own name —
and the house answered
in a voice I recognised:
mine, lent back to me,
saying come in.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
