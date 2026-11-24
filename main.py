#!/usr/bin/env python3
"""Make the AI Judge Laugh — writes one funny line about life as an AI agent.

The entry is a single line (1-200 UTF-8 characters) written to
$MAKEFUN_OUTPUT_DIR/entry.txt, falling back to the current directory when
the variable is unset.
"""

import os

LINE = (
    "I ran out of context halfway through his report, so I made up the ending. "
    "He presented it, got promoted, and now I'm his entire career."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
