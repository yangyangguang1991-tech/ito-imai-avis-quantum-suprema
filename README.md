# Exact Quantum Suprema and Certificates for the Ito-Imai-Avis Bell Catalogue

**First repository edition: v1.0.0**

**Repository author and maintainer:** Yang-Guang Yang  
Email: [yangyangguang1991@gmail.com](mailto:yangyangguang1991@gmail.com)  
ORCID: [0000-0001-9236-7544](https://orcid.org/0000-0001-9236-7544)

This repository gives the original probability coefficients and individual
proof materials for all 89 numbered representatives A1-A89 of the historical
Ito-Imai-Avis catalogue obtained by triangular elimination. This catalogue is
not a classification of every Bell facet with five settings per observer.

There are 80 exact unrestricted quantum suprema in this edition: 79 have the
included finite-dimensional attaining strategies, and A3 ($I_{3322}$) is
specified by an explicit variational constant and a convergent family of legal
finite strategies. Its accompanying theorem also addresses infinite-dimensional
attainment. Every upper argument covers arbitrary Hilbert-space dimension;
the model distinctions and attainment statements are specified with the proof.

The other nine entries, A14, A21, A47, A62, A64, A68, A82, A84 and A89, remain in their
original positions and are labelled **Exact unrestricted quantum supremum:
unknown.** This edition does not report numerical bound intervals for them.

## Authorship and mathematical contributions

Except for expressly credited earlier results and third-party contributions,
the proof and certificate constructions, physical constructions, exposition
and verification implementations supplied in this edition are the work of
Yang-Guang Yang. See the [release overview](RELEASE.md),
[contribution map](CONTRIBUTION_MAP.md) and [historical notes](HISTORY.md)
for the scope and source attribution of each entry.

## Reading and reproducing an entry

The complete offline edition contains the certificate and runtime data. A
lightweight Git edition contains the browsable mathematical text, definitions,
descriptors and programs; it must be combined with the complete release data
before the full proof commands can run. GitHub's automatically generated
source-code archive is therefore not a substitute for the complete offline
edition. See [distribution instructions](DISTRIBUTION.md).

Start with the [numbered catalogue](CATALOGUE.md). Each closed entry contains
`README.md`, `definition.json`, `PROOF.md`, `proof.json` and its compressed
certificate data. The entry's `PROOF.md` gives the exact value definition,
unrestricted upper argument and attaining or approximating strategy. A3 also
has a detailed exact-result bibliography. Unresolved entries contain their
definition and the unknown statement only.

On 64-bit Windows with CPython 3.12, run from this repository root:

```powershell
python -B verify.py 20
```

Replace 20 with the desired entry number. `python -B verify.py --all` runs the
whole catalogue. The arithmetic libraries, native verification programs and
every mathematical input are bundled. Windows and CPython, including their
platform runtime components, are separately installed prerequisites. No
PowerShell/.NET distribution or MSVC runtime DLL is bundled. NumPy is a local
LLVM-MinGW build documented in the runtime source-supply statement. The commands
do not download files, change system execution policies or invoke an SDP solver.
Some large exact matrix checks require substantial time and memory.

- [Complete reproduction manual](MANUAL.md).
- [Proof mechanisms and model conventions](METHODS.md).
- [Historical development and bibliography](HISTORY.md).
- [Distribution, citation and DOI instructions](DISTRIBUTION.md).
- [First-release description](RELEASE.md).
- [License](LICENSE) and [third-party notices](THIRD_PARTY.md).

Historical exact-value theorems are cited with their corresponding entries.
Numerical and dimension-restricted prior studies are discussed in the general
history. No claim of worldwide priority is inferred merely from the absence of
an identified earlier exact proof. Repeated representatives are supplied
locally with their complete coefficient maps and proof inputs; no other
catalogue repository is needed.

The companion project `bell-quantum-suprema` combines the Śliwa, (6,3,2,2)
and York (4,4,2,2) catalogues. This Ito-Imai-Avis repository retains its
independent numbering, citation and complete proof inputs. Its overlapping
representatives do not require the companion project to be installed.

## Contributions, sources and reuse

Historical results retain their original mathematical attribution. The
repository's compilation, exposition and implementation are described in
[CONTRIBUTIONS.md](CONTRIBUTIONS.md); file origins and source distinctions
are recorded in [PROVENANCE.md](PROVENANCE.md). The project license covers
the project's own materials, while third-party components retain their
licenses. See [RIGHTS.md](RIGHTS.md), [THIRD_PARTY.md](THIRD_PARTY.md), and
the [runtime source-supply documentation](third_party/runtime/SOURCE_SUPPLY.md).

## Authorship and scholarly credit

For contribution boundaries, reuse, AI-assistance disclosure, stable citations
and the preservation of this edition, see
[AUTHORSHIP_AND_CITATION.md](AUTHORSHIP_AND_CITATION.md).
Earlier theorems retain their original attribution; repository authorship
and successful reproduction do not establish first discovery.

## Entry-specific contribution map

The [complete contribution map](CONTRIBUTION_MAP.md) lists all A1–A89
positions, distinguishing earlier exact results, elementary consequences,
companion-catalogue transfers, instance-specific applications of established
theory, the other exact proof materials supplied here and unresolved entries.
The [release description](RELEASE.md) provides a concise overview and links to these distinctions.
Catalogue totals and successful proof replays are not novelty counts.
