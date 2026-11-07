# Mathematical material provenance

This repository distinguishes the origin of a mathematical result from the origin of its exposition, verification programs and certificate files. A citation gives scholarly credit; it does not by itself grant permission to copy protected text, software or other material.

## Project contributions

Yang-Guang Yang is responsible for the assembly and maintenance of this edition. He has confirmed that the local research materials were prepared under his direction, that he is authorized to license the project's new code, documentation and certificate files, and that there are no undisclosed rightsholders or restrictions affecting those contributions. This confirmation does not extend to the third-party materials identified below.

The earlier notice `CH-Bell exact-value research project contributors`, retained in the A2 and A4 certificate archives, identifies local project contributions under an earlier project name. Those copyright and permission notices are preserved. The project license applies only to rights held in the project's own contributions; it does not transfer ownership of an earlier theorem or replace a third-party license.

A2 reuses the project's CHSH implementation. A3 includes the project's I3322 path and variational implementation. A4, A5, A6 and A7 transport local implementations for York Y6, Y51, Y9 and Y169, respectively. Their exact coefficient transformations are included in their own archives. These are transfers within the same research project; the native proof materials are present locally, and the reader does not need a companion repository. Reuse of a mathematical proof or its implementation is not counted as a fresh discovery.

The file-level [provenance map](PROVENANCE.json) covers all 89 definitions and the members of all 80 mathematical certificate archives. It distinguishes retained local files, locally adapted files, and release files. These classifications are based on the local source archives, assembly programs and revision records. A file hash establishes identity, not independent authorship or legal clearance.

## Catalogue mathematics and coefficient sources

The historical catalogue and its numbering are attributed to Avis, Imai, Ito and Sasaki and to Ito, Imai and Avis. The bibliographic references are in [HISTORY.md](HISTORY.md). The coefficient identification for A2 through A89 uses the [fixed coefficient distribution of T. Hrga and collaborators](https://github.com/HrgaT/Bell_inequality_data/tree/4822d81eb827a52717feca6319716b6439ffb532).

Each entry's `definition.json` provides the full integer probability table in the maximization convention. The provenance map records the historical source identification and the sign change relating it to that table. Historical source hashes identify materials consulted during the coefficient comparison; they do not indicate that those files are distributed. A1 is the elementary positivity inequality, written directly.

The certificate archives use 76 project-generated coefficient inputs. Each is constructed directly from the complete public probability matrix in deterministic row-major order, retaining its stated orientation. These inputs contain the setting counts and the resulting integer polynomial; they do not copy an upstream file's projection or commutation wrapper. The literal parsers, coefficient comparisons and subsequent proof obligations remain operative. Their hashes identify the local coefficient inputs, not purported copies of historical source files.

No explicit repository license was identified in the inspected upstream coefficient distribution. Accordingly, this edition does not bundle its original files or infer a permission grant from public availability. It records the historical mathematical identification and supplies project-written implementations and representations of the Bell functionals. No new ownership of the underlying mathematical facts, historical results or upstream collection is asserted. Neither citation nor a change of file format would confer a license over protected upstream material.

## Earlier theorems and reproduced arguments

Earlier exact-value results remain attributed to their authors. The CHSH theorem is credited in A2. The detailed A3 bibliography identifies the unrestricted I3322 results, the path and variational constructions, and the distinctions between exact value, finite-dimensional attainment and infinite-dimensional attainment. The project's implementations and explanatory text are distinguished from those earlier mathematical results.

The remaining entries include the proof materials on which this edition relies. The absence of an earlier exact-value citation in an entry is not a claim of worldwide priority. General numerical and methodological antecedents are discussed in [HISTORY.md](HISTORY.md), without being presented as proofs of exact values they did not establish.

No complete external article, publisher PDF or external article TeX source is included in the mathematical certificate archives. References to an external article are citations, not an assertion that its text is covered by this repository's license.

## Licenses and scope of the map

The [MIT License](LICENSE) applies to the project's own code, documentation and certificate representations to the extent that the project holds rights in them. Existing notices remain applicable. The [third-party statement](THIRD_PARTY.md) describes the separately distributed software components; their own licenses and corresponding-source conditions are not replaced by MIT.

`PROVENANCE.json` maps public entry files and archive members to their source categories and records their content hashes. A certificate member path is relative to the reassembled archive identified by that entry's `proof.json`. The map does not include generated output from running a checker and is not a substitute for a mathematical proof or a software license. Runtime software is outside the mathematical-material inventory and has a separate component and source record.
