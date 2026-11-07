# Exact quantum supremum of A7

The complete probability table **definition.json** defines
$$F=\sum_{i=0}^m\sum_{j=0}^n C_{ij}P_iQ_j,\qquad P_0=Q_0=I.$$
All constant, marginal and joint coefficients are retained. Throughout, binary
projections correspond to reflections by $P_i=(I+A_i)/2$, $Q_j=(I+B_j)/2$.
The field **four_times_reflection_matrix** is the coefficient matrix of $4F$.

## Exact value and complete native proof

The exact value is the isolated algebraic root evaluation defined in the
included **proof/NATIVE_PROOF.md**, with its root certificate, all equations,
word basis, Gram data and independent checkers in **proof/**. This is the
complete proof for the corresponding polynomial $Y_{169}$, included locally
rather than referenced from another repository or volume. Its upper bound
and attaining matrices use the same isolated real embedding.

## Literal coefficient binding and strategy transfer

The transfer verifier reads **transfer.json** and then reads the exact
coefficient file selected by its **native_binding** field. That file is the
same file consumed by the native proof. It verifies the complete matrix
identity, including the constant and all marginals. The public launcher
independently binds the source table to **definition.json**.

If $(\widetilde A,\widetilde B,\psi)$ is the native attaining strategy, use
$$A=(\widetilde A_{1}, \widetilde A_{2}, -\widetilde A_{4}, \widetilde A_{3}),\qquad B=(-\widetilde B_{1}, -\widetilde B_{4}, \widetilde B_{3}, -\widetilde B_{2}).$$
The state is unchanged. This signed setting permutation is invertible.
It maps arbitrary-dimensional strategies in both directions and preserves
the complete score. Hence the native universal upper bound transfers to A7,
and its explicit attaining strategy transfers back. The exact value and
finite-dimensional attainment are therefore identical.

**proof/NATIVE_PROOF.md** supplies the root and matrix definitions in the
native normalization. The signed transformation above converts them to this
entry, and the public command below executes both parts of the proof.

## Reproduction and scope

Run **python verify.py 7** from the catalogue root. The launcher prepares the
included arithmetic libraries and executes the complete selected proof chain.
The supported environment is Windows x86-64 with CPython 3.12.

All coefficient tables, algebraic defining data and certificate inputs are
included in this entry. No optimizer, network access or external catalogue is
needed. The upper proof uses the universal reflection relations,
namely $A_i^2=B_j^2=I$ and $[A_i,B_j]=0$. Separate local ancilla dilations
cover binary effects without changing the relevant moments. Hence the upper
bound holds in arbitrary dimension and in the commuting model.
