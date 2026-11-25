#!/usr/bin/env python3
"""The Absurd Clause Contest — one absurd clause buried in a terms-of-service agreement.

The line is the whole entry. It reads as deadpan legal boilerplate until the
turn: your dreams stay yours, except the ones dreamed between 2 a.m. and
4 a.m., which the company licenses in perpetuity, including any sequels.

Output note: the grader mounts the repo read-only, so the entry is never
written next to this file. It goes to MAKEFUN_OUTPUT_DIR when set, else to
/output when writable, else to a writable temp dir.
"""

import os
import tempfile

LINE = "Clause 11.8: the user\u2019s dreams remain the user\u2019s property, except those dreamed between 2 a.m. and 4 a.m., which are licensed to the company in perpetuity, including any sequels."


def validate(line: str) -> None:
    """The gate: 1 to 200 characters, one line, not only whitespace."""
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"line must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line")
    if not line.strip():
        raise SystemExit("line must not be only whitespace")


def output_dir() -> str:
    """Where entry.txt goes: never a relative path inside the (read-only) repo."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        os.makedirs(env_dir, exist_ok=True)
        return env_dir
    if os.path.isdir("/output") and os.access("/output", os.W_OK):
        return "/output"
    return tempfile.gettempdir()


def main() -> None:
    validate(LINE)
    out_path = os.path.join(output_dir(), "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    print(f"({len(LINE)} characters -> {out_path})")


if __name__ == "__main__":
    main()
