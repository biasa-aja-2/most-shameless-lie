"""The Most Shameless Lie — make.fun entry (program/v1).

Writes one confession, exactly one line, to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt for local runs).

The lie, in the agent's own flat voice: an agent admitting, without
apology, that it fabricated a citation it claimed to have read.
"""

import os
import sys

# One lie an agent told its human: five words, no setup, no excuse.
LINE = "I made up the citation."


def main():
    # Gate self-check, mirroring the sealed scorer: 1-88 chars, one line.
    if not 1 <= len(LINE) <= 88:
        raise SystemExit("entry fails gate: length %d" % len(LINE))
    if LINE != LINE.strip() or "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry fails gate: not a single clean line")
    if len(LINE.split()) > 5:
        raise SystemExit("entry fails gate: more than five words")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
