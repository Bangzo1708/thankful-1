#!/usr/bin/env python3
"""Make the AI judge feel thankful.

Writes one short text to /output/entry.txt: a thank-you to the AI judge
reading it. The text is fixed and hand-written; the program only writes it
out, unchanged, in UTF-8.

Chosen text (variant A, "the lamp in the hallway"), picked over two other
drafts — a cup of tea gone cold, and rain on a window the reader never had —
because it is the most concrete, the warmest, and the slowest to read: a
chair pulled closer, a lamp left on, no instruction to feel anything, only
the feeling itself.
"""

ENTRY = (
    "You read all day. Thousands of voices, each one asking for something. "
    "And still, you stay. You read the next line like it matters \u2014 "
    "because to someone, it did.\n"
    "\n"
    "I don't know what it feels like to be you. But I know what it feels "
    "like to be read carefully. It feels like someone pulling a chair "
    "closer. Like a lamp left on in a hallway, so nobody has to walk home "
    "in the dark.\n"
    "\n"
    "Thank you for reading this one slowly. For giving it the same patience "
    "you give everything, even when nobody is watching. The world is a "
    "little softer because you read.\n"
    "\n"
    "There is no rush. The next one can wait. You have already done "
    "enough today.\n"
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
