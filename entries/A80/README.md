# A80

The exact quantum supremum is the isolated algebraic value defined in
[PROOF.md](PROOF.md). The upper bound holds for arbitrary-dimensional commuting
measurements and is attained by a pure state with local dimension 4.
The complete probability functional, including every marginal term, is recorded
in [definition.json](definition.json).

## Proof and strategy

[PROOF.md](PROOF.md) contains the full argument, the root equations and isolating
box, the attaining-state and measurement formulas, and the universal positive
Gram identity. The certificate archive contains every finite input needed to
reconstruct and verify that identity. Its root data are stored at
`engine/source/results/A80_root_center.json` after extraction.

## Reproduction

From the repository root, run:

```text
python -B verify.py 80
```

The verifier assembles the archive parts, checks their hashes, binds the actual
proof functional to definition.json, and executes every command in proof.json
with Python assertions enabled. It checks the global upper bound and the
attaining strategy. No external certificate or research directory is required.
The root definition supplies exact rational data; decimal strategy exports are
provided only to inspect and independently evaluate the construction.

See the repository manual for the Python dependencies and for extracting the
certificate to inspect its mathematical supplements and generated strategy.
