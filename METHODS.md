# Mathematical conventions and proof mechanisms

For a literal probability table C, with the constant at position (0,0), let
F=sum C_ij P_i Q_j, with P_0=Q_0=I. The first column and first row are Alice's
and Bob's marginal terms. The supplied conversion matrix represents exactly 4F
after P_i=(I+A_i)/2 and Q_j=(I+B_j)/2. Deterministic local strategies have
maximum zero in this convention.

Q_fin denotes the supremum over all finite local dimensions, Q_sp the normal
spatial tensor-product supremum, and Q_com the commuting-operator supremum.
In general Q_fin<=Q_sp<=Q_com. A universal commuting upper certificate and
a matching finite strategy prove equality of the three. If matching values
are approached by finite strategies rather than attained, the argument uses
the supremum and does not assert finite attainment. A3 states its separate
variational and dimension theorem explicitly.

The finite sum-of-squares certificates use only Hermiticity, A_i^2=B_j^2=I
and cross-party commutation. Candidate-specific symmetry or annihilation is
used to construct scalar coefficients, not imposed on competing observables.
Two-party reflection dilations of binary effects preserve all the moments
in the Bell polynomial, extending the bounds to binary POVMs.

Several entries use explicit radical or algebraic-field Gram matrices.
Others define an isolated stationary root of a finite physical chart, then
construct an exact correction of a rational positive Gram seed at that same
root. Full coefficient compatibility is established from moment identities,
stationarity and any additional exact null relations. An invertible normal
map or a full-rank coefficient minor supplies an exact right inverse on the
compatible range. The correction is bounded strictly below the certified
positive margin. This proves an operator identity with no unpaid residual.
Root isolation or fixed-dimensional optimization alone supplies no universal
upper bound; the positivity and complete coefficient identity are essential.

The bounded-roundoff implementations use IEEE 754 binary64 CPU arithmetic
with rounding to nearest. Their rational error budgets include the matrix
product and interval errors; a floating residual or eigenvalue alone is not
an acceptance criterion. The supplied CPU arithmetic libraries are part of
the reproduction environment. Exact integer and rational implementations
instead certify their integer-size and overflow bounds directly.

The numbered entry proof specifies the exact map, word convention, arithmetic
and independent checks used in that case. Historical sources and exact-result
attribution are documented separately from the reproducible certificate.
