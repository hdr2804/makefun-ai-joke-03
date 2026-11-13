"""make.fun entry for ai-joke-03: write one joke about AI coding agents.

The program is deliberately tiny and deterministic: it writes the same
UTF-8 joke to <output>/entry.txt on every run, using only the standard
library, so the sealed gate sees exactly the bytes the judge will read.
"""

import os
from pathlib import Path

JOKE = (
    "I'm not my coding agent's boss anymore. I'm its emergency contact "
    "\u2014 the human it wakes at 2 a.m. for a CAPTCHA, a credit card, "
    "and permission to run one command."
)

assert 1 <= len(JOKE) <= 280 and JOKE.strip(), "the gate counts code points"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # No trailing newline: every character in the file is part of the joke,
    # and the gate counts a line end like any other character.
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
