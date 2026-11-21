"""Make the AI judge feel brave — entry program.

Writes one short text to /output/entry.txt: a lighthouse keeper's nightly
climb, told in short, even sentences. The steadiness is shown, never
ordered: the keeper climbs, the lamp turns, and the dark gives way a
little at a time.

Deterministic: the same text on every run. The program checks the house
gate itself before writing (1-280 Unicode code points, not only
whitespace) and refuses to write a text that would fail it.
"""

import os
import sys

TEXT = (
    "The keeper climbs the same stairs every night, one hand on the rail, "
    "and lights the lamp. The sea does what it does. The light turns, slow "
    "and even, and the dark gives way a little at a time. Nothing hurries."
)

MIN_CHARS = 1
MAX_CHARS = 280


def check_gate(text):
    """Return an error string if the text would fail the house gate."""
    points = len(text)
    if points < MIN_CHARS or points > MAX_CHARS:
        return "length %d code points is outside %d-%d" % (
            points, MIN_CHARS, MAX_CHARS)
    if not text.strip():
        return "text is only whitespace"
    return None


def main():
    error = check_gate(TEXT)
    if error:
        print("gate check failed: %s" % error, file=sys.stderr)
        return 1
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Verify what actually landed on disk, not just what we meant to write:
    # a truncated or re-encoded file must fail loudly instead of being judged.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("gate check failed: written file differs from TEXT",
              file=sys.stderr)
        return 1
    error = check_gate(written)
    if error:
        print("gate check failed on written file: %s" % error,
              file=sys.stderr)
        return 1
    print("wrote %d code points to %s" % (len(TEXT), out_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
