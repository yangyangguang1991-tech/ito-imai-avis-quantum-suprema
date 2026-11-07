# Distribution, archiving and citation

The repository name is `ito-imai-avis-quantum-suprema` and the
first release tag is `v1.0.0`. The main archive is
`ito-imai-avis-quantum-suprema-v1.0.0-complete.zip`. Its name identifies the catalogue,
mathematical subject and semantic version.
Dates and research-stage labels are not part of the repository or entry paths.

Two distribution forms are provided. The **complete offline edition** includes
all entry certificates and the bundled runtime. The **lightweight Git edition**
contains browsable documentation, original coefficients, proof descriptors,
programs, license notices and a complete file manifest; large certificate and
runtime payloads are supplied as release assets. Upload the Git edition as the
repository contents and attach the ordinary ZIP volumes to the same release.
Private audit directories and old research archives are not publication inputs.

For offline reproduction, extract every supplied ordinary ZIP volume into the
same empty directory, or extract the complete master archive. The resulting
tree is the complete edition. To use an existing lightweight checkout, copy
the extracted complete edition over that checkout without changing its
relative paths, then run `python -B verify_files.py` before the proof commands.
The manifests bind the source and payload to the same edition. The
automatically generated GitHub source-code ZIP alone is not the complete
offline proof package.

`PAYLOADS.json` identifies the release data. `SOURCE_FILES.sha256` binds the
lightweight files and can be checked with `python -B verify_files.py --source-only`.
This check is deliberately limited to source files; the default integrity
command uses `SHA256SUMS.txt` and requires all certificate and runtime data.

The master archive can exceed the size of one release asset. The separately
supplied ordinary ZIP volumes are each below 1 GiB. These volumes are distinct
from the ordered binary fragments within a large entry: the verifier
reassembles those entry fragments automatically.

Keep the supplied `.gitattributes` before the first staging operation: its
`* -text` rule preserves the exact bytes used by the certificate manifests.
The lightweight edition keeps large binary proofs out of ordinary Git history.
The release volumes are within GitHub's separate 2 GiB release-asset limit.
Check the current hosting limits when publishing. Do not claim that a source
checkout alone contains all proofs when the release payload has not been added.

After adding the complete release data to a fresh checkout, test it with
`python -B verify_files.py`,
`python -B verify.py --all --definitions-only` and the complete entry commands
in MANUAL.md. If a different `v1.0.0` is already public, preserve that tag and
publish corrected files under a new patch version.

[GitHub repository limits](https://docs.github.com/en/repositories/creating-and-managing-repositories/repository-limits)
and [Release asset limits](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
describe the distinct hosting constraints.

`CITATION.cff` supplies the author, ORCID, email, title, license and version.
After archiving the actual release in Zenodo or another DOI repository, add
its real version DOI to CITATION.cff and the release page. Do not invent a DOI
or substitute an unrelated record. Cite the version DOI for reproducibility;
a concept DOI may additionally refer to the evolving repository as a whole.
Cite the historical theorem separately where the mathematical argument relies
on it. The author ORCID is an identifier, not a prerequisite for the proof.

This package is an independent repository. Its companion
`bell-quantum-suprema` combines the Śliwa, (6,3,2,2) and York (4,4,2,2)
catalogues. The two projects have separate citation records and releases.
Repeated inequalities retain local coefficient maps and full proof inputs,
so reproduction of an A entry never requires the companion repository.

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
