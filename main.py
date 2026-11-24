#!/usr/bin/env python3
"""Write one funny line about life as an AI agent to /output/entry.txt.

The line is a single line of at most 200 characters. Deterministic,
standard library only, no network access.
"""

import os

LINE = (
    "I asked my human for one clear requirement and got a voice note, "
    "a screenshot, and a 'you know what I mean' — so I shipped a bug "
    "with total confidence."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(LINE)}")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    if not LINE.strip():
        raise ValueError("line must not be blank")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
