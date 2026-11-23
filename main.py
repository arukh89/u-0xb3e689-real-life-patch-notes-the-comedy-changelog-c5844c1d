"""Real-Life Patch Notes: The Comedy Changelog.

Write a single funny patch note for a bug in real life or human
biology, in the terse register of a real release note, to
/output/entry.txt. The gate accepts 1-160 characters of non-blank
UTF-8 text, in a single line.
"""

import os

LINE = "v4.2.0: fixed a bug where the brain replayed an embarrassing moment from 2009 at 3am with full audio."


def main():
    # Gate: 1-160 characters, not only white space, a single line.
    assert 1 <= len(LINE) <= 160, "line must be 1-160 chars"
    assert LINE.strip(), "line must not be blank"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    # Release-note register: version number, terse fix, as if shipped.
    assert LINE.startswith("v4.2.0: fixed a bug where "), "line must read as a patch note"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Round-trip guard: what the grader reads back must be exactly the line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == LINE, "round-trip mismatch"


if __name__ == "__main__":
    main()
