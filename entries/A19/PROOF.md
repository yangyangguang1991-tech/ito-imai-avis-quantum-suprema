# Exact quantum supremum of A19

The complete probability table **definition.json** defines
$$F=\sum_{i=0}^m\sum_{j=0}^n C_{ij}P_iQ_j,\qquad P_0=Q_0=I.$$
All constant, marginal and joint coefficients are retained. Throughout, binary
projections correspond to reflections by $P_i=(I+A_i)/2$, $Q_j=(I+B_j)/2$.
The field **four_times_reflection_matrix** is the coefficient matrix of $4F$.

## Exact root and physical realization

The exact value is $f(x_*)$, where $x_*$ is the unique zero of the gradient
of the rational physical score in the box specified by **A19_PAIR_ROOT_DEFINITION.json**.
The entries of **root** are rational centres, not exact optimizing parameters.
The rational radius and **root_preconditioner** define the contraction test:
$T(x)=x-R\nabla f(x)$ has derivative norm below one and maps the closed
box strictly into itself. Thus $R$ is invertible and the contraction theorem
proves the asserted unique gradient zero. All 39 chart coordinates are varied in this root definition.

All local spaces have dimension 4. For a rank-$r$ chart with pivot rows $p$,
form a 4-by-$r$ matrix $V$ with an identity submatrix on $p$ and fill the
other rows from successive chart coordinates in row order. Define
$$P=V(V^TV)^{-1}V^T.$$
The identity rows guarantee $V^TV\succ0$. Thus $P$ is a real orthogonal
projection for every real chart parameter. Settings are ordered Alice first and Bob second.

The **types** field refines this chart. A **fixed** measurement is
$\operatorname{diag}(1,1,0,0)$; a **pair** uses pivot rows $(0,1)$ and
nonpivot block $\operatorname{diag}(u,v)$; a **full** measurement uses the
four free entries of its nonpivot block. The final 15 coordinates are the
16 state coefficients in tensor-product order, with a fixed 1 inserted at
**state_pivot**. Normalize this vector. **pair_family.parameters** implements
these formulas, and **evaluate** contracts the complete literal Bell matrix.
This chart is used to construct one witness, not to restrict competitors.

## Root symmetry and the six-term upper certificate

The chart has 39 free real coordinates. The root verifier proves uniqueness
of its stationary point in the stated rational box. The six signed setting
relabelings in **A19_AUTOMORPHISMS.json** preserve the complete original Bell
polynomial. **symmetry19.py** applies each relabeling to the root box and
constructs a regular real orthogonal gauge for the two declared Jordan pairs.
The transformed root lies in a wider coordinate box on which the derivative
contraction proves uniqueness. A relabeling followed by this gauge therefore
returns the same stationary root. All root moments are invariant under the six
relabelings, and any word polynomial annihilating the root state also
annihilates each relabeled root strategy.

This symmetry statement is used only at the isolated root. It is not asserted
for every nearby chart point or for arbitrary competing strategies.

## Same-root coefficient identity and positivity

Let $w$ be the included 202-word reflection column. The 16 selected physical
action pivots are invertible on the root box. Exact inversion defines a
rational frame $N(x)$ and $r(x)=N(x)^Tw$ with
$r_i(x)|\psi(x)\rangle=0$. At $x_*$, the root symmetry above implies that
every relabeled polynomial $g(r_i(x_*))$ also annihilates the root state.

For a real symmetric Gram matrix $G$, define the universal polynomial

$$\mathcal S_*(G)=\frac16\sum_{g\in\mathcal G}
g(r(x_*))^\dagger Gg(r(x_*)).$$

Let $A_*$ map raw upper-triangular Gram coordinates to the signed orbit
coefficient sums of $\mathcal S_*(G)$, and let $b_*$ encode
$f(x_*)I-F$ in the same convention. Each off-diagonal coordinate represents
both symmetric entries. Signed coefficient sums pair with signed averages of
physical moments. The eight columns of $J_*$ are the value moment and the
seven derivatives selected by **jet_columns** in **A19_FRAME_SELECTION.json**.
They are a subset of the derivatives of the full 39-coordinate chart.

Freeze the scalar frame at $x_*$ and vary the physical chart. Since every
relabeled annihilator kills the root state, every squared norm and polarized
cross term has zero value and first derivative there. Hence

$$A_*^T J_*=0.$$

The target pairs to zero with the value column by definition of $f(x_*)$,
and to the negative selected partial derivatives of $f$ with the other seven
columns. All 39 stationary equations hold at the root, so

$$J_*^T b_*=0.$$

These are exact identities at the root, rather than numerical residual tests
or identities assumed throughout the surrounding box.

The normal checker proves invertibility of

$$K_*=A_* W A_*^T+J_*J_*^T,$$

where $W$ is diagonal, with weight one on diagonal Gram coordinates and
$1/2$ on off-diagonal coordinates. The exact **Z** construction implements
this convention. The two summand ranges are orthogonal and together span the
coefficient space, so $\operatorname{range}A_*=\ker J_*^T$.

For the supplied rational positive Gram seed $G_0$, put

$$e=b_*-A_*\operatorname{vec}(G_0),\qquad
\delta=W A_*^TK_*^{-1}e,\qquad
G_*=G_0+\operatorname{unvec}(\delta).$$

The compatibility identities imply $A_*\delta=e$ exactly. Thus every signed
orbit coefficient of $\mathcal S_*(G_*)$ equals that of $f(x_*)I-F$.
Both polynomials are invariant under the six-element group. The independent
directed-word expansion checks the reduction and restores the full polynomial
identity, including symmetry-forced zero coefficients.

The rational Neumann test includes both dyadic rounding and the outward
interval enclosure over the root box. Its error is strictly below one.
Exact interval LDL and a separate rational congruence calculation prove
$G_0-\eta I\succ0$. The bound on the complete correction is strictly smaller
than $\eta$, so $G_*\succ0$. Consequently

$$f(x_*)I-F=\frac16\sum_{g\in\mathcal G}
g(r(x_*))^\dagger G_*g(r(x_*))\succeq0.$$

Only the scalar coefficients use the attaining root and its symmetry.
The displayed operator identity uses universal reflection and cross-party
commutation relations, and imposes no symmetry or chart constraint on a
competing strategy. Together with the four-dimensional attaining strategy,
it proves $Q_{\mathrm{fin}}=Q_{\mathrm{sp}}=Q_{\mathrm{com}}=f(x_*)$.

## Reproduction and scope

Run **python verify.py 19** from the catalogue root. The launcher prepares the
included arithmetic libraries and executes the complete selected proof chain.
The supported environment is Windows x86-64 with CPython 3.12.
The selected stages are **physical19.py**, **root19.py**, **symmetry19.py**, **independent19.py**, **exact19.py**, **normal19.py**, **gram19.py**, **independent_global19.py**.
All coefficient tables, algebraic defining data and certificate inputs are
included in this entry. No optimizer, network access or external catalogue is
needed. The upper proof uses the universal reflection relations,
namely $A_i^2=B_j^2=I$ and $[A_i,B_j]=0$. Separate local ancilla dilations
cover binary effects without changing the relevant moments. Hence the upper
bound holds in arbitrary dimension and in the commuting model.
