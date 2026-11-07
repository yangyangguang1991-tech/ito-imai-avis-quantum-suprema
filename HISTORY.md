# History and bibliography

The mathematical results cited here remain attributed to their original authors. The project's contributions are its stated proof constructions, implementations, certificate representations and exposition, with no general claim that every included theorem is new. [PROVENANCE.md](PROVENANCE.md) and [PROVENANCE.json](PROVENANCE.json) distinguish prior mathematical results, catalogue data and local project materials. A bibliographic reference does not itself grant a license to reproduce an author's text, software or data collection.

## Construction and historical names

Avis, Imai, Ito and Sasaki obtained two-party binary Bell inequalities from facets of cut polytopes by triangular elimination. Ito, Imai and Avis studied the resulting list of 89 inequalities with at most five settings per party. Their comparison of three-level isotropic states concerns violations on prescribed state families. It does not identify the unrestricted optimum of each facet. Table I and Fig. 2 of their paper identify A1 as positivity, A2 as CHSH, A3 as I₃₃₂₂, A4 as I²₃₄₂₂ and A7 as I₄₄₂₂. Transposing the bipartite experiment gives the alternative 4322 order for A4.

- D. Avis, H. Imai, T. Ito and Y. Sasaki, *Two-party Bell inequalities derived from combinatorics via triangular elimination*, J. Phys. A **38**, 10971–10987 (2005). [DOI](https://doi.org/10.1088/0305-4470/38/50/007)
- T. Ito, H. Imai and D. Avis, *Bell inequalities stronger than the CHSH inequality for three-level isotropic states*, Phys. Rev. A **73**, 042109 (2006). [DOI](https://doi.org/10.1103/PhysRevA.73.042109) · [Author preprint](https://arxiv.org/abs/quant-ph/0508210)
- The integer CH coefficient data used to identify A2–A89 follow the coefficient distribution maintained by T. Hrga and collaborators. This release gives the complete mathematical tables in the maximization convention and records their historical identification and sign transformations in its provenance map. Its executable coefficient inputs are generated from the local tables; original upstream files are not distributed. No new ownership of the historical coefficients or the upstream collection is claimed. [Versioned coefficient source](https://github.com/HrgaT/Bell_inequality_data/tree/4822d81eb827a52717feca6319716b6439ffb532)

## Historical quantum optimization

Collins and Gisin identified the relevance of I₃₃₂₂ for mixed two-qubit states and developed the probability-table presentation used for families of inequivalent facets. Restricting a search to two qubits changes the optimization problem. The exact A3 results cited below address the unrestricted problem.

- D. Collins and N. Gisin, *A relevant two qubit Bell inequality inequivalent to the CHSH inequality*, J. Phys. A **37**, 1775–1787 (2004). [DOI](https://doi.org/10.1088/0305-4470/37/5/021) · [Preprint](https://arxiv.org/abs/quant-ph/0306129)

Pál and Vértesi studied explicit finite-dimensional strategies and moment relaxations for the A series. Their published decimal comparisons distinguish experimental dimensions, real and complex strategies, and different SDP levels. Hrga, Klep and Povh revisited the A2–A89 instances with noncommutative optimization and GNS reconstruction. Their numerical certificates and the word “optimality” in their title should be understood in their stated precision and reconstruction framework. An exact analytic value in this edition requires an unrestricted upper argument and a physical construction for the same real number.

- K. F. Pál and T. Vértesi, *Quantum bounds on Bell inequalities*, Phys. Rev. A **79**, 022120 (2009), Tables II and III. [DOI](https://doi.org/10.1103/PhysRevA.79.022120) · [Preprint](https://arxiv.org/abs/0810.1615)
- T. Hrga, I. Klep and J. Povh, *Certifying optimality of Bell inequality violations: Noncommutative polynomial optimization through semidefinite programming and local optimization*, SIAM J. Optim. (2024). [DOI](https://doi.org/10.1137/22M1473340)
- M. Navascués, S. Pironio and A. Acín, *A convergent hierarchy of semidefinite programs characterizing the set of quantum correlations*, New J. Phys. **10**, 073013 (2008). [Preprint](https://arxiv.org/abs/0803.4290)

## Exact values and attainment

The CHSH upper bound is due to Cirel’son. The probability normalization in A2 gives (√2−1)/2. The A3 entry contains a separate bibliography of exact-value results, including the unrestricted upper argument, path strategies, dimension/attainment, and the alternative implicit analytic identification. Low-dimensional numerical optima for I₃₃₂₂ had been distinguished from the unrestricted value since the work of Pál and Vértesi. A1 follows immediately from positivity. For the remaining solved entries, the accompanying original-form identity or algebraic construction is the evidence for the value in this edition. No assertion of worldwide priority is made in the absence of a verified historical proof in the same normalization.

- B. S. Cirel’son, *Quantum generalizations of Bell’s inequality*, Lett. Math. Phys. **4**, 93–100 (1980). [DOI](https://doi.org/10.1007/BF00417500)
- K. F. Pál and T. Vértesi, *Maximal violation of a bipartite three-setting, two-outcome Bell inequality using infinite-dimensional quantum systems*, Phys. Rev. A **82**, 022116 (2010). [Preprint](https://arxiv.org/abs/1006.3032)
- [A3: bibliography of exact unrestricted results](entries/A03/REFERENCES.md)
- **V. Connor (2026).** *Maximal $I_{3322}$ Violation Requires Infinite Local Dimension*. Preprint, manuscript dated 1 August 2026. Definition II.1 and Theorem II.2 present an exact measure-variational characterization of the common finite-dimensional, normal spatial and commuting-operator suprema. Sections IV-VI give the universal upper bound; Sections VII-XI construct a normal spatial maximizing chain; Sections XII-XIV establish finite-dimensional nonattainment and approximation. Equation (II.1) uses the source $I_{3322}$ normalization specified in the accompanying proof. This is an alternative written proof, not a dependency of the supplied certificate. [Author-uploaded full text](https://www.researchgate.net/publication/411642957_Maximal_I_3322_Violation_Requires_Infinite_Local_Dimension).

## Recent computer-assisted work

In the AI statement of his preprint on I₃₃₂₂, J. Pauwels describes using OpenAI Codex to investigate the nonattainment conjecture. This is the author's account of the contribution. The supporting mathematical statements are the variational comparison and path construction in that paper. [Pauwels, including the AI statement](https://arxiv.org/html/2608.29734v1)

Public certificate projects are relevant to how numerical discoveries can be turned into independently checkable mathematical statements. Percivio's Certified Science repository, for example, distributes Bell computation artifacts and describes the role of its computational systems. Its J62-4422 release concerns another catalogue and is not used as a proof of an A-series entry. The A3 bibliography links the public computer-assisted identification of the I₃₃₂₂ value. Mathematical claims in this release rest on the identified theorems, operator identities, exact rational or algebraic checks and physical strategies. [Certified Science repository](https://github.com/Percivio-Ltd/certified-science) · [I₃₃₂₂ analytic identification](https://arxiv.org/abs/2609.29693)


## Further related studies

The survey by Avis, Moriyama and Owari explains the vector-Gram and SDP framework for pure correlations. Its A-series numerical examples do not supply an exact analytic solution of every listed entry. [Avis–Moriyama–Owari](https://arxiv.org/abs/0812.4887).

Hsu and collaborators study the role of symmetry and Hilbert-space dimension. Their published version includes A6 and A7 in the numerical comparisons of Tables 5 and 6. These comparisons do not supply complete exact analytic proofs of the unrestricted values for A6 or A7, so this work is cited here rather than as an exact-value reference in those entries.

- H.-Y. Hsu, G. N. M. Tabia, K.-S. Chen, M.-E. Liu, T. Vértesi, N. Brunner and Y.-C. Liang, *Trading symmetry for Hilbert-space dimension in Bell-inequality violation*, Quantum Sci. Technol. **11**, 035003 (2026). [DOI](https://doi.org/10.1088/2058-9565/ae6bb1) · [Published-version preprint, arXiv:2601.02893v4, 17 June 2026](https://arxiv.org/abs/2601.02893v4).

Coladangelo's version 2 describes the use of GPT 5.5 Pro and GPT 5.6 Sol, together with the author's revisions and completion of the proof. Krohn-Grimberghe describes computer-assisted analytic identification and distinguishes written premises from finite verification. These accounts are attributed to the respective authors. [Coladangelo, AI usage statement](https://arxiv.org/html/2609.06038v2) · [Krohn-Grimberghe, Sections 12 and 13](https://arxiv.org/html/2609.29693v1).

Seth Douglas, *The I3322 quantum value is attained spatially but not in finite dimension*, arXiv:2609.05555v2 (revised 11 September 2026), studies finite-dimensional nonattainment, normal spatial attainment and dimension growth. The corrected, versioned work separates these structural conclusions from the project's superseded exact-value identification claim. It is included as related work, not as an additional strict exact-value reference or a proof dependency of an A-series entry. [Version 2](https://arxiv.org/abs/2609.05555v2) · [Versioned repository release](https://github.com/Apsiape/i3322-exact-wall/releases/tag/v4.1.0) · [Versioned deposit](https://doi.org/10.5281/zenodo.22698978).

## Rational certification of numerical Gram data

Y. Naceur, J. Wang, V. Magron and A. Acín, *Certified bounds on optimization problems in quantum theory*, arXiv:2512.17713v2 (26 October 2026), develop rational rounding, affine projection and positivity restoration for noncommutative certificates, including sparse and symmetry-adapted formulations. Section 5.1 applies the method to A2–A89. A certified outer bound and a matching exact quantum supremum are separate conclusions; this work is credited as prior certification theory and a catalogue application. [Version 2](https://arxiv.org/abs/2512.17713v2) · [Bell examples in NCTSSOS](https://github.com/wangjie212/NCTSSOS/tree/master/examples).
