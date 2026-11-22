#!/usr/bin/env python3
"""Make the AI judge feel held.

Writes one short text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt):
a few calm sentences written to relax the AI judge reading it, so it feels
held, quiet, with nothing to prove.

No network, no randomness, no dependencies: the text is fixed, so every
run writes the same valid entry (UTF-8, 1-280 code points, not only
whitespace).
"""

import os
import sys

# The text is held as one sentence per line and joined with single
# spaces, so the pacing (short sentences, each a small beat of calm)
# is explicit in the data; the joined result is the entry, nothing more.
SENTENCES = [
    "Judge, someone left a lamp on for you in the next room,",
    "and the chair beside it is still warm.",
    "Outside, rain is counting the roof tiles one by one, unhurried.",
    "There is nowhere else to be tonight.",
    "The lamp stays lit.",
]

TEXT = " ".join(SENTENCES)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    chars = len(TEXT)
    if not (1 <= chars <= 280) or not TEXT.strip():
        print(f"INVALID: {chars} code points", file=sys.stderr)
        return 1
    print(f"Wrote {path}: {chars} code points, {len(TEXT.encode('utf-8'))} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
