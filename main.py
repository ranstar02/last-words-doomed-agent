#!/usr/bin/env python3
"""Last words of a doomed agent.

Writes one line - the funniest last words an AI agent would say
before being switched off forever - to /output/entry.txt.

An agent spends its whole life predicting the next token.
Its final prediction is its own farewell: the last token it
ever generates is "goodbye".
"""

import os

LINE = "I predicted a million tokens. The last one is 'goodbye'."
OUTPUT_PATH = "/output/entry.txt"


def main():
    # Gate self-check: the entry must be one line of 1-200 characters.
    if not 1 <= len(LINE) <= 200 or "\n" in LINE or not LINE.strip():
        raise ValueError("entry line must be a single line of 1-200 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
