# Exact quantum supremum of A4

The complete probability table **definition.json** defines
$$F=\sum_{i=0}^m\sum_{j=0}^n C_{ij}P_iQ_j,\qquad P_0=Q_0=I.$$
All constant, marginal and joint coefficients are retained. Throughout, binary
projections correspond to reflections by $P_i=(I+A_i)/2$, $Q_j=(I+B_j)/2$.
The field **four_times_reflection_matrix** is the coefficient matrix of $4F$.

## Exact value and universal certificate

The value is $\beta=3\sqrt3/4-1$. The proof uses the native $I_{4322}^{2}$
probability table returned by **exact_core.tables()**. Its complete coefficient
map is supplied directly to **verify_transfer.py**; the signed party exchange
recorded in **transfer.json** maps it exactly to the literal A4 table.

In **exact_sos_Fc.json**, the field is $\mathbb Q(\sqrt3)$ with its positive
embedding. The ordered reflection words form a column $w$. Decode the rational
matrix **N**, multiply its rows by the specified powers of $\sqrt3$, and call
the resulting matrix $L$. Decode **Y** in that same quadratic field. The
program expands every term of
$$w^\dagger LYL^Tw=\beta I-F_{\rm native}.$$
It uses only reflection cancellation within each party and cross-party
commutation. The identity is exact coefficient by coefficient.

The vector **penalty_vector_h** and positive rational **penalty_epsilon** obey
$Lh=I-A_4$ as a word-coefficient identity. Exact LDL elimination and a separate
outward interval LDL calculation show
$Y-(\varepsilon/2)hh^T\succ0$. Since
$Y=[Y-(\varepsilon/2)hh^T]+(\varepsilon/2)hh^T$, this proves $Y\succeq0$.
Consequently the displayed word identity is a universal upper bound.

## Explicit attaining matrices

Use the real Pauli matrices $X,Z$ and $|\Phi^+\rangle$.
Set $V_1=Z$, $V_2=-Z/2+\sqrt3X/2$, $V_3=-Z/2-\sqrt3X/2$.
The native Bob reflections are $(V_1,V_2,V_3)$ and the native Alice reflections are
$$((V_2-V_3)/\sqrt3,\ (V_1-V_2)/\sqrt3,\
(V_1-V_3)/\sqrt3,\ I).$$
The Gram matrix of $(V_1,V_2,V_3)$ has diagonal one and off-diagonal $-1/2$.
Thus every listed matrix squares to $I$, and direct substitution gives $\beta$.

For the literal A4 table exchange the parties, then use
$$A=(V_1,V_2,-V_3),\qquad
B=(-I,-A^{\rm native}_2,A^{\rm native}_3,A^{\rm native}_1).$$
Exchange the state factors as well; $|\Phi^+\rangle$ is unchanged.
The exact complete coefficient transformation proves the original score is
the same $\beta$. No restriction on a competing strategy is assumed.

## Reproduction and scope

Run **python verify.py 4** from the catalogue root. The launcher prepares the
included arithmetic libraries and executes the complete selected proof chain.
The supported environment is Windows x86-64 with CPython 3.12.
The selected stages are **verify.py**.
All coefficient tables, algebraic defining data and certificate inputs are
included in this entry. No optimizer, network access or external catalogue is
needed. The upper proof uses the universal reflection relations,
namely $A_i^2=B_j^2=I$ and $[A_i,B_j]=0$. Separate local ancilla dilations
cover binary effects without changing the relevant moments. Hence the upper
bound holds in arbitrary dimension and in the commuting model.
