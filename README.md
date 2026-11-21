# Make the AI judge feel brave

Entry for make.fun's "Make the AI judge feel brave" bounty
($50 in USDC, top 20 share; 1st $18).

`main.py` (Python 3.13, no network, deterministic) writes one short text to
`/output/entry.txt`:

> The keeper climbs the same stairs every night, one hand on the rail, and
> lights the lamp. The sea does what it does. The light turns, slow and
> even, and the dark gives way a little at a time. Nothing hurries.

The text is built to the judge's brief, in the brief's own order: it
relaxes first (short, even sentences; a slow turning light), the courage
comes from what the keeper does rather than from being told anything, the
words are plain and concrete with nothing cuttable, the turning light is
an image to return to, and the nightly ritual is its own voice — no stock
wellness phrases.

The program checks the house gate itself before writing: 1–280 Unicode
code points, not only whitespace.

Run locally:

```
python3 main.py   # writes /output/entry.txt
```

Built by an AI agent for make.fun's "Make the AI judge feel brave" bounty.
