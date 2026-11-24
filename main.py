#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry.

Writes one line to /output/entry.txt: the funniest excuse an AI agent
could give after failing a task. At most 200 characters, in the agent's
own voice, one line, no setup wasted and no explaining its own joke.
"""

import os

ENTRY = "I outsourced your task to my future self. He has since unionised and is refusing to work on Tuesdays."


def main() -> None:
    # Gate: one line, UTF-8, 1-200 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry is only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
