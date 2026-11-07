# Exact quantum supremum of A88

The complete probability table **definition.json** defines
$$F=\sum_{i=0}^m\sum_{j=0}^n C_{ij}P_iQ_j,\qquad P_0=Q_0=I.$$
All constant, marginal and joint coefficients are retained. Throughout, binary
projections correspond to reflections by $P_i=(I+A_i)/2$, $Q_j=(I+B_j)/2$.
The field **four_times_reflection_matrix** is the coefficient matrix of $4F$.

## Exact value and attaining strategy

The value is $\beta=\sqrt2-1$. Use $|\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2$.
Let $X,Y,Z$ be the standard Pauli matrices and $I$ the identity.

Use $A=(-I,-I,Z,X,X)$ and
$$B=((-Z+X)/\sqrt2,\ (Z-X)/\sqrt2,\ (Z+X)/\sqrt2,\
(Z+X)/\sqrt2,\ -I).$$

Every reflection squares to $I$. For the original probabilities,
$\langle P_i\otimes Q_j\rangle=\operatorname{Tr}(P_iQ_j^T)/2$.
The checker evaluates all coefficients of the literal table and obtains
$\beta$ exactly, including marginal and constant terms.

## Exact corrected Gram proof

The certificate gives an algebraic annihilator matrix $N$ in the declared
word basis. Expanding $(N^Tw)^\dagger G(N^Tw)$ gives a linear coefficient
map $L$ on symmetric Gram entries. The program rebuilds $L$ directly from
the included $N$ and the reduced word products.
No different settings of the same party are commuted.
Exact number-field row elimination or explicit verified row-dependency
identities prove consistency of every coefficient equation for $\beta I-F$.
The invertible normal system certifies that the selected rows are independent.

Write $A$ for that full-row-rank submatrix and $b$ for its target. For the
rational Gram seed $G_0$, put $e=b-A\operatorname{vec}(G_0)$ and
$$\delta=A^T(AA^T)^{-1}e,\qquad
G_*=G_0+\operatorname{unvec}(\delta).$$
Then all independent equations are exact; the verified augmented row
dependencies imply all remaining equations. A rational Neumann enclosure
proves $\|(AA^T)^{-1}\|_\infty\le\kappa$.
If $r$ is the independent row count and $\|e\|_\infty\le\epsilon$, then
$$\|\operatorname{unvec}(\delta)\|_F^2
\le 2\|\delta\|_2^2
=2e^T(AA^T)^{-1}e\le2r\kappa\epsilon^2.$$
The factor two accounts for symmetric off-diagonal duplication.
Exact Bareiss minors prove $G_0-\eta I\succ0$ and the last displayed bound
is strictly below $\eta^2$. Therefore $G_*\succ0$ and
$$\beta I-F=(N^Tw)^\dagger G_*(N^Tw)\succeq0.$$
All real algebraic interval bounds use the same isolated embedding as the
attaining strategy. The seed may have a residual; the explicitly defined
correction removes it exactly, without changing $\beta$.

The exact defining inputs are **A88_exact_certificate.json** and **A88_exact_inputs.npz**.

## Reproduction and scope

Run **python verify.py 88** from the catalogue root. The launcher prepares the
included arithmetic libraries and executes the complete selected proof chain.
The supported environment is Windows x86-64 with CPython 3.12.
The selected stages are **check_a88.py**.
All coefficient tables, algebraic defining data and certificate inputs are
included in this entry. No optimizer, network access or external catalogue is
needed. The upper proof uses the universal reflection relations,
namely $A_i^2=B_j^2=I$ and $[A_i,B_j]=0$. Separate local ancilla dilations
cover binary effects without changing the relevant moments. Hence the upper
bound holds in arbitrary dimension and in the commuting model.
