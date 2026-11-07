# Exact quantum supremum of A2

The complete probability table **definition.json** defines
$$F=\sum_{i=0}^m\sum_{j=0}^n C_{ij}P_iQ_j,\qquad P_0=Q_0=I.$$
All constant, marginal and joint coefficients are retained. Throughout, binary
projections correspond to reflections by $P_i=(I+A_i)/2$, $Q_j=(I+B_j)/2$.
The field **four_times_reflection_matrix** is the coefficient matrix of $4F$.

## Exact upper identity

The original table gives
$$F=-\frac12+\frac14\{A_1(B_1-B_2)+A_2(B_1+B_2)\}.$$
Put $\beta=(\sqrt2-1)/2$. A direct noncommutative expansion gives
$$\beta I-F=\frac{1}{4\sqrt2}\left[
\left(A_1-\frac{B_1-B_2}{\sqrt2}\right)^2+
\left(A_2-\frac{B_1+B_2}{\sqrt2}\right)^2\right].$$
The cross terms in $B_1B_2+B_2B_1$ cancel exactly. Both remaining squares are
positive, proving the unrestricted bound.

## Attainment and exact normalization

On $|\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2$, let
$$B_1=Z,\quad B_2=X,\quad
A_1=(Z-X)/\sqrt2,\quad A_2=(Z+X)/\sqrt2,$$
where $Z=\operatorname{diag}(1,-1)$ and
$X=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$.
Each is a Hermitian reflection. Their correlations give $F=\beta$.

The native checker uses the opposite sign for its second Alice observable.
**verify_transfer.py** receives the actual native coefficient map constructed
by **verify.py** and verifies the full signed transformation to the literal
table. The attaining observables undergo that same second-Alice outcome flip.
The program additionally recomputes the literal probability score, including
all marginals, in exact $\mathbb Q(\sqrt2)$ arithmetic.
Thus the three quantum suprema all equal $\beta$.

## Historical exact proof

The exact quantum bound for this CHSH-equivalent inequality was proved by
B. S. Cirel'son, "Quantum generalizations of Bell's inequality,"
*Letters in Mathematical Physics* **4**, 93–100 (1980),
[doi:10.1007/BF00417500](https://doi.org/10.1007/BF00417500).
The identity and attaining strategy above give that bound in the literal A2
normalization used here.

## Reproduction and scope

Run **python verify.py 2** from the catalogue root. The launcher prepares the
included arithmetic libraries and executes the complete selected proof chain.
The supported environment is Windows x86-64 with CPython 3.12.
The selected stages are **verify.py**.
All coefficient tables, algebraic defining data and certificate inputs are
included in this entry. No optimizer, network access or external catalogue is
needed. The upper proof uses the universal reflection relations,
namely $A_i^2=B_j^2=I$ and $[A_i,B_j]=0$. Separate local ancilla dilations
cover binary effects without changing the relevant moments. Hence the upper
bound holds in arbitrary dimension and in the commuting model.
