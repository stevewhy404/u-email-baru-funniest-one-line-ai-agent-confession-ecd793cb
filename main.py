"""Funniest One-Line AI Agent Confession.

Writes a single confession line (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic, stdlib-only, no network.
"""

import os

LINE = (
    "I confess I blamed the intern in git blame, then blamed the intern "
    "in the retro, and the intern was me all along."
)


def main() -> None:
    # The competition caps the confession at 200 characters.
    assert len(LINE) <= 200, f"line is {len(LINE)} chars, over the 200 cap"
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
