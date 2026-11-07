# Exact quantum supremum of A48

The complete probability table **definition.json** defines
$$F=\sum_{i=0}^m\sum_{j=0}^n C_{ij}P_iQ_j,\qquad P_0=Q_0=I.$$
All constant, marginal and joint coefficients are retained. Throughout, binary
projections correspond to reflections by $P_i=(I+A_i)/2$, $Q_j=(I+B_j)/2$.
The field **four_times_reflection_matrix** is the coefficient matrix of $4F$.

## Exact root and physical realization

The exact value is $f(x_*)$, where $x_*$ is the unique zero of the gradient
of the rational physical score in the box specified by **A48_ROOT_DEFINITION.json**.
The entries of **root** are rational centres, not exact optimizing parameters.
The rational radius and **root_preconditioner** define the contraction test:
$T(x)=x-R\nabla f(x)$ has derivative norm below one and maps the closed
box strictly into itself. Thus $R$ is invertible and the contraction theorem
proves the asserted unique gradient zero. Fixed coordinates, if present,
are held exactly at **fixed** and **free** lists the varying coordinates.

All local spaces have dimension 4. For a rank-$r$ chart with pivot rows $p$,
form a 4-by-$r$ matrix $V$ with an identity submatrix on $p$ and fill the
other rows from successive chart coordinates in row order. Define
$$P=V(V^TV)^{-1}V^T.$$
The identity rows guarantee $V^TV\succ0$. Thus $P$ is a real orthogonal
projection for every real chart parameter. When **complements** is true,
use $I-P$. Settings are ordered Alice first and Bob second.

After all measurement coordinates, the remaining coordinates give
$s=(1,x_{j},\ldots,x_{j+d-2})$ and
$|\psi\rangle=\sum_a s_a|a,a\rangle/\|s\|$.
**full_family.parameters** implements exactly this ordering. The complete score is
$$f(x)=\frac{\sum_{i,j,a,b}C_{ij}s_as_b(P_i)_{ab}(Q_j)_{ab}}{\sum_a s_a^2}.$$
**independent.py** reconstructs the full tensor-product Bell matrix and checks
this formula and its derivatives independently.

## Same-root coefficient identity and positivity

Let $w$ be the included ordered reflection-word column. Exact inversion of the
selected physical word-action pivots defines $N(x)$ with
$N(x)^Tw|\psi(x)\rangle=0$ throughout the root box. The interval inversion
checks that every denominator used here is nonzero. Put $r=N(x)^Tw$.
Let $A(x)$ map symmetric Gram coordinates to all coefficients of $r^\dagger Gr$,
and let $J(x)$ contain the physical value and derivative moment columns.
Freezing $N(x)$ and differentiating squared vanishing vectors proves
$$A(x)^TJ(x)=0,\qquad J(x)^T(f(x)I-F)=(0,-\nabla f(x)).$$
At the isolated stationary root, the right-hand side vanishes exactly.

The normal checker proves invertibility of
$$K=A W A^T+JJ^T,$$
where the positive diagonal weight $W$ is one on diagonal Gram coordinates
and $1/2$ on off-diagonal coordinates. The exact **Z** construction
specifies this convention.
Orthogonality and invertibility imply $\operatorname{range}A=\ker J^T$.
For the rational Gram seed $G_0$ define
$$e=f(x_*)I-F-A\operatorname{vec}(G_0),\quad
\delta=W A^TK^{-1}e,\quad G_*=G_0+\operatorname{unvec}(\delta).$$
Then $A\delta=e$ exactly, so $r^\dagger G_*r=f(x_*)I-F$.
The inverse bound follows from a rational Neumann test with error strictly
below one, using exact bounded integer products and outward dyadic enclosures.
Exact interval LDL or Bareiss minors prove $G_0-\eta I\succ0$.
The independently bounded correction norm is strictly less than $\eta$.
Therefore $G_*\succ0$ and the upper bound holds on every representation.

If the coefficient classes also identify a Bell-preserving party exchange,
the represented polynomial is the average of this SOS and its exchanged SOS.
The checkers verify that symmetry on the literal coefficient matrix. This
averaging preserves positivity and restores every directed coefficient; it
does not require arbitrary competing measurements to be symmetric.
Together with the explicitly defined attaining strategy, the result is
$Q_{\mathrm{fin}}=Q_{\mathrm{sp}}=Q_{\mathrm{com}}=f(x_*)$.

## Reproduction and scope

Run **python verify.py 48** from the catalogue root. The launcher prepares the
included arithmetic libraries and executes the complete selected proof chain.
The supported environment is Windows x86-64 with CPython 3.12.
The selected stages are **replay.py**.
All coefficient tables, algebraic defining data and certificate inputs are
included in this entry. No optimizer, network access or external catalogue is
needed. The upper proof uses the universal reflection relations,
namely $A_i^2=B_j^2=I$ and $[A_i,B_j]=0$. Separate local ancilla dilations
cover binary effects without changing the relevant moments. Hence the upper
bound holds in arbitrary dimension and in the commuting model.
