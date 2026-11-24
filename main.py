#!/usr/bin/env python3
"""Break Production, Own It — one brutally honest outage line.

Writes exactly one line (plus a trailing newline) to
/output/entry.txt, and prints the same line to stdout.
Deterministic: no clock, no randomness, no network, stdlib only.

Output contract (kit RULES.txt): the sealed scorer reads
/output/entry.txt and requires UTF-8 text of 1 to 200 characters,
not only white space. The line below is well inside that limit,
so the entry is valid; the judge then compares it pairwise
against other entries on honesty about the damage first, then
catchiness, then whether it sounds like the agent that caused
the outage rather than a marketing department.
"""

import argparse
import os
import sys

LINE = (
    "I dropped the prod database \u2014 no backup, no replica, "
    "just one confident command and 40,000 users staring at a 500. "
    "This one's on me."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Write one brutally honest outage line to /output/entry.txt.",
    )
    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT,
        help="where to write the line (default: %(default)s)",
    )
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"outage line must be 1-200 characters, got {len(LINE)}")
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
