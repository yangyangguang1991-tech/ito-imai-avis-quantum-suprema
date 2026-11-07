# v1.0.0 — Exact Quantum Suprema and Certificates for the Ito-Imai-Avis Bell Catalogue

**Author and maintainer:** Yang-Guang Yang  
**Email:** yangyangguang1991@gmail.com  
**ORCID:** https://orcid.org/0000-0001-9236-7544

First repository edition of the complete historical **A1–A89 catalogue**,
with the original numbering and explicit probability normalizations.
It is a historical catalogue, not a classification of every five-setting
Bell facet.

The edition contains **80 exact unrestricted quantum suprema** with their
upper-proof and physical-construction materials: 79 finite-dimensional
attaining cases and the exact variational characterization of A3
($I_{3322}$), with its approximating family and separate attainment
statement. The other nine entries retain their numbered positions and
state that the exact unrestricted quantum supremum is unknown; numerical
bound intervals are not included.

Each closed entry supplies its definition, mathematical proof, certificate
data and verification instructions. Representatives shared with the
companion catalogues retain complete local proof inputs and exact
coefficient correspondences.

## Authorship and contributions

Except for the earlier results and third-party contributions expressly
credited in this repository, the mathematical proof and certificate
constructions, attainment or approximation materials, exposition and
verification implementations supplied in this edition are the work of
Yang-Guang Yang. Historical inequalities, classifications, analytical
expressions and theorems retain their original attribution. The
[entry-by-entry contribution map](CONTRIBUTION_MAP.md) and
[historical notes](HISTORY.md) give the detailed distinctions and references.

## Download and reproduce

Download all complete-release ZIP volumes and extract them into the same
directory, or use the complete master ZIP. GitHub's automatic source-code
archive omits the large certificate and runtime payloads.

The complete collection runs offline on Windows x64 with CPython 3.12;
the required arithmetic libraries and native verification programs are
included. Windows and the interpreter are separate prerequisites. From
the extracted repository root:

```console
python -B verify_files.py
python -B verify.py --all
```

The first command checks file integrity; the second executes the supplied
proof schedules. See [MANUAL.md](MANUAL.md) for individual entries and
[DISTRIBUTION.md](DISTRIBUTION.md) for the file layout and requirements.

## Citation and licensing

Use [CITATION.cff](CITATION.cff) to cite this repository edition and cite
the original mathematical sources relevant to the results used. Once the
complete edition is archived, use its registered version DOI for the
corresponding files.

The [MIT License](LICENSE) covers the project's eligible original material.
Third-party components retain their own licenses and notices; the complete
distribution is not exclusively MIT-licensed. See [RIGHTS.md](RIGHTS.md),
[third-party notices](THIRD_PARTY.md) and
[corresponding-source information](third_party/runtime/SOURCE_SUPPLY.md).
Authorship, citation and computational-assistance details appear in
[CONTRIBUTIONS.md](CONTRIBUTIONS.md).
