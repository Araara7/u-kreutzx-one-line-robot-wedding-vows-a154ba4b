"""One-Line Robot Wedding Vows — entry writer.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt. Deterministic, stdlib only.
"""

import os

ENTRY = (
    "I take you to be my lawfully wedded unit, to have and to hold, "
    "in sickness and in health, until a firmware update do us part."
)


def main() -> None:
    # Gate: 1-160 UTF-8 chars, exactly one line, not only whitespace.
    assert 1 <= len(ENTRY) <= 160, "entry length out of gate"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
