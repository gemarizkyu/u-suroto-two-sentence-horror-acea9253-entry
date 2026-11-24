#!/usr/bin/env python3
"""Two-Sentence Horror entry for make.fun.

Writes one original two-sentence horror story to /output/entry.txt.
Deterministic: no network, no model calls, no randomness, no clock.
"""

import os
from pathlib import Path

STORY = (
    "I buried my dog under the oak tree this morning and planted rosemary "
    "over the spot so I would always find it again. "
    "Tonight the rosemary was gone, and a small white cross stood in its "
    "place, carved with my name and tomorrow's date."
)

# The sealed gate accepts 1-400 characters of UTF-8 text, exactly two
# sentences, not only whitespace. The asserts below mirror that gate so a
# broken story fails loudly here instead of silently at grading time.


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    text = STORY.strip()
    assert 1 <= len(text) <= 400, f"story length {len(text)} out of gate range"
    assert text.count(".") == 2, "story must be exactly two sentences"
    (output_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
