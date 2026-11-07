# Exact quantum supremum of A1

The complete probability table **definition.json** defines
$$F=\sum_{i=0}^m\sum_{j=0}^n C_{ij}P_iQ_j,\qquad P_0=Q_0=I.$$
All constant, marginal and joint coefficients are retained. Throughout, binary
projections correspond to reflections by $P_i=(I+A_i)/2$, $Q_j=(I+B_j)/2$.
The field **four_times_reflection_matrix** is the coefficient matrix of $4F$.

## Upper bound and attainment

The literal table is $C=\left(\begin{smallmatrix}0&0\\0&-1\end{smallmatrix}\right)$,
so $F=-PQ$. For commuting positive contractions,
$PQ=P^{1/2}QP^{1/2}\succeq0$. Thus $F\preceq0$ on any Hilbert space.
In one-dimensional local spaces choose the unit state, $P=0$ and $Q=1$.
The score is exactly zero. Therefore
$$Q_{\mathrm{fin}}(A_1)=Q_{\mathrm{sp}}(A_1)=Q_{\mathrm{com}}(A_1)=0.$$

The checker reads **literal_coefficients.json**, verifies that its four
coefficients are exactly those of $-PQ$, and directly evaluates this attaining
strategy. The public launcher binds that same consumed table to **definition.json**.

## Reproduction and scope

Run **python verify.py 1** from the catalogue root. The launcher prepares the
included arithmetic libraries and executes the complete selected proof chain.
The supported environment is Windows x86-64 with CPython 3.12.
The selected stages are **check.py**.
All coefficient tables, algebraic defining data and certificate inputs are
included in this entry. No optimizer, network access or external catalogue is
needed. The upper proof uses the universal reflection relations,
namely $A_i^2=B_j^2=I$ and $[A_i,B_j]=0$. Separate local ancilla dilations
cover binary effects without changing the relevant moments. Hence the upper
bound holds in arbitrary dimension and in the commuting model.
