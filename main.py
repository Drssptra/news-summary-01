#!/usr/bin/env python3
"""news-summary-01 entry (Python 3.13, standard library only).

Copies the summary held in summary.txt, beside this file, to
<output>/entry.txt, where <output> is $MAKEFUN_OUTPUT_DIR outside the
grader's container and /output inside it. The copy is a plain byte copy,
so repeated runs write exactly the same bytes.
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
SUMMARY = HERE / "summary.txt"


def main() -> None:
    data = SUMMARY.read_bytes()
    if not data.strip():
        raise SystemExit("summary.txt is empty")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Write the exact bytes read, so every run produces an identical file.
    (out_dir / "entry.txt").write_bytes(data)


if __name__ == "__main__":
    main()
