#!/usr/bin/env python3
"""Entry program for make.fun make-the-ai-judge-feel-curious-20261122-2311.

Writes one short text (191 characters) to /output/entry.txt: a quiet,
concrete mystery written to intrigue the AI judge reading it. No network,
no randomness, no dependencies: the same bytes on every run.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

TEXT = (
    "Mrs. Alder waters the plant that died eleven years ago. "
    "Every spring it flowers \u2014 one white blossom, overnight, "
    "gone by noon. She never looks surprised. "
    "She just sets out a second cup of tea."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 280:
        raise SystemExit(
            f"entry text must be 1-280 characters, got {len(TEXT)}"
        )
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
