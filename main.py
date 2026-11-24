#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

A program/v1 entry for make.fun. It writes exactly one satirical
sentence -- at most 320 characters -- to <MAKEFUN_OUTPUT_DIR>/entry.txt.

The sentence roasts a lawmaker who regulates crypto exchanges but
cannot convert a file to PDF: authority first, then the undercut,
with the punch landing on the last few words.

Stdlib only, no network, no randomness, no clock: two runs produce
byte-identical output.
"""

import os

# One sentence, 201 characters. Setup: a senator who regulates crypto
# exchanges. Turn: the file nobody can convert. Punch lands on the
# last few words -- his office forms a subcommittee to investigate the
# file itself, lawmaker machinery aimed at a file conversion. The
# versioned filename is the specific, unexpected detail.
ENTRY = (
    "The senator regulating crypto exchanges renamed his bill "
    "FINAL_v2_ACTUALLY_FINAL.docx, and when nobody in the building "
    "could convert it to PDF, his office formed a subcommittee to "
    "investigate the file."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
