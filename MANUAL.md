# Reproduction manual

Use the complete offline edition for mathematical reproduction. If starting
from the lightweight Git edition, first add the complete release data as
described in DISTRIBUTION.md. The source edition alone does not include the
large certificate and runtime archives, and the verifier never downloads them.

## Platform and dependencies

Use 64-bit Windows on x86-64 with CPython 3.12. The mathematical libraries
(NumPy, SciPy, SymPy, mpmath, python-flint and threadpoolctl) and required native
verification programs are included, with their license notices. NumPy is a
local LLVM-MinGW build with a documented binary64 ABI patch; see
`third_party/runtime/SOURCE_SUPPLY.md`. No PowerShell/.NET distribution or
MSVC runtime DLL is bundled, and no compiler installation is needed to run
the supplied verification binaries. Windows and the CPython installation,
including their own platform runtime components, remain prerequisites.
The proof launcher extracts the shared runtime for its child processes.
Verification does not change system configuration or execution policies.
Local security policies must permit running the supplied programs. No proof
command downloads software. Do not use Python's `-O` or `-OO` options:
mathematical assertions must remain enabled.

Use a local directory with sufficient free disk space for a certificate,
its temporary expanded data and any exact matrices produced while checking.
The largest entries require several gigabytes of working memory. Run one
entry at a time if memory is limited. A slow exact matrix operation is not
evidence that the proof has completed; wait for the command to finish.

## Commands

From the extracted repository root:

```powershell
python -B verify.py 20
python -B verify.py --all
```

The first command checks only A20; the second processes every entry in order.
For a closed entry the launcher checks the original full probability matrix,
the probability/reflection conversion, the deterministic local bound and
the binding to the coefficients actually consumed by that proof. It verifies
the certificate archive digest, extracts the inputs into a fresh temporary
directory, supplies the bundled libraries and runs all prescribed proof stages.
A stage failure terminates the command with a nonzero exit code. For an
unresolved entry it checks the literal definition and prints the unknown
statement; that output is not a proof of a quantum optimum.

To inspect one uncompressed certificate without running its full proof:

```powershell
python -B verify.py 20 --extract verification-output/A20
```

The destination must not already exist. This extraction checks its digest and
functional binding; it does not perform the mathematical proof. The complete
command above remains the reproduction entry point. Likewise,
`python -B verify.py --all --definitions-only` checks original definitions
and classical local bounds only.

## Uniform entry layout

```text
entries/
  A01/
    README.md
    definition.json
    PROOF.md
    proof.json
    certificate.zip
  ...
  A14/
    README.md
    definition.json
  ...
  A89/
    README.md
    definition.json
```

A large certificate is stored as `certificate.zip.part001`, `.part002`, and so on,
instead of a single ZIP. `proof.json` gives the ordered list and SHA256 of the
reassembled archive. The verifier handles these parts automatically. They
are binary fragments; do not try to unzip an individual fragment. A3's
additional `REFERENCES.md` supplies its detailed exact-result bibliography.
The different internal mathematical inputs reflect the different proofs:
radical fields, isolated roots, Gram matrices, rational witnesses or a path
construction. Their purpose is specified in the entry proof.

## Exactness and physical realizations

Integers and fractions are exact. Algebraic values are defined by their
polynomials and real embeddings, or by a finite rational system with a proven
unique root in an explicit box. A printed decimal is supplementary. In the
implicit constructions the state and measurements are evaluated at that
unique root, and the upper certificate uses the same root. Positive margins
are certified with exact arithmetic or rigorously outward error bounds.

The proof data include all chart signs, projector ranks, coordinate orderings
and normalization factors required to reconstruct the strategies. When an
entry is transferred from another representative, its exact coefficient map
also specifies how measurements are relabelled or outcome-flipped. A finite
approximating family is distinguished explicitly from a finite attainer.

## Integrity and licensing

`SHA256SUMS.txt` records the distributed files, and `verify_files.py` checks
those digests. File integrity alone is not mathematical verification. Keep all
runtime parts and certificate fragments together. The original code and
documentation use the MIT License; bundled third-party notices remain in force.

## Runtime corresponding sources

The complete release also contains the corresponding-source archives and
build materials identified in [the runtime source-supply documentation](third_party/runtime/SOURCE_SUPPLY.md).
These are supplementary source materials for the bundled software; they are
not new mathematical certificates and are not needed to execute a proof.
The lightweight Git edition omits these archives alongside the large proof
and runtime payloads. Their versions, licenses, origins and checksums remain
documented in the Git edition, and every source archive is included in the
complete release volumes and master archive. Keep these materials with the
binary distribution when archiving or redistributing the complete edition.

The project's MIT license does not replace third-party licenses. See
[RIGHTS.md](RIGHTS.md), [CONTRIBUTIONS.md](CONTRIBUTIONS.md) and
[PROVENANCE.md](PROVENANCE.md) for the respective licensing and attribution scope.

When describing an archival deposit, state explicitly that this is a mixed-license
distribution: MIT covers the project's own contributions, and the bundled
third-party components retain the licenses identified in the source-supply
statement. Do not describe the complete archive as exclusively MIT-licensed.
