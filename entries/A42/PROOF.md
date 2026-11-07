# Exact quantum supremum of A42

The complete probability table **definition.json** defines
$$F=\sum_{i=0}^m\sum_{j=0}^n C_{ij}P_iQ_j,\qquad P_0=Q_0=I.$$
All constant, marginal and joint coefficients are retained. Throughout, binary
projections correspond to reflections by $P_i=(I+A_i)/2$, $Q_j=(I+B_j)/2$.
The field **four_times_reflection_matrix** is the coefficient matrix of $4F$.

## Exact five-variable root and strategy

The exact value is $\beta=f(x_*)$, where $x_*=(t,a,c,b,d)$ is the unique
stationary root in the rational box **center** plus or minus **radius** in
**A42_twirl_certificate.json**. For any $u$ set
$c_u=(1-u^2)/(1+u^2)$, $s_u=2u/(1+u^2)$.
Take the state $(|00\rangle+t|11\rangle)/\sqrt{1+t^2}$ and reflections
$$A=(c_aZ-s_aX,\ c_aZ+s_aX,\ c_cZ+s_cX,\ c_cZ-s_cX,\ X),$$
$$B=(c_bZ-s_bX,\ c_bZ+s_bX,\ c_dZ-s_dX,\ c_dZ+s_dX,\ X).$$
The complete literal score is the rational function **phase42_family.value**
with phase $(1,0)$. Every displayed matrix squares to $I$.
Both the automatic-differentiation checker and the independent direct
probability checker prove a strict Krawczyk inclusion and contraction below
one on the specified box, establishing the unique exact stationary root.

## Phase-compatible kernel and complete coefficient range

For arbitrary real $p,q$ with $p^2+q^2=1$, replace the first Alice pair's
$X$ by $pX+qY$, and Bob's final $X$ by $pX-qY$.
The literal score is independent of this phase.
**verify_symbolic42_core.py** proves that identity as a polynomial reduction
modulo $p^2+q^2-1$, and proves all 28 columns of **kernel42.kernel**
annihilate every such state for every listed Bell-preserving relabeling.
It verifies the nonzero local-transform determinants and an identity
submatrix in the eight-column core. The interval computation checks every
denominator on the root box.

The coefficient map is averaged over the exact relabelings in **orbits**.
The four specified phases provide value and first-derivative moment columns.
With the kernel coefficients frozen, derivatives of the vanishing squared
norms give $A^TJ=0$. Phase-independence and root stationarity give
$J^T(\beta I-F)=0$. The checker proves
$K=AA^T+JJ^T$ invertible by exact integer products and rational interval
Neumann bounds. Hence $\operatorname{range}A=\ker J^T$.

For the included rational Gram seed define
$e=\beta I-F-A\operatorname{vec}(G_0)$ and
$G_*=G_0+\operatorname{unvec}(A^TK^{-1}e)$.
Then $A\operatorname{vec}(G_*)=\beta I-F$ exactly.
Bareiss minors prove $G_0-\eta I\succ0$; the verified correction norm is
strictly less than $\eta$. Thus the averaged SOS is positive and proves
$F\preceq\beta I$ for all commuting strategies.
The independent checker reconstructs the direct probability derivatives,
word map, and both entire normal-system products using arbitrary-size
integers. The phase identities are a separate indispensable part of the
complete selected chain, not a numerical assumption.

The displayed two-qubit strategy attains the same $\beta$, proving equality
of the finite-dimensional, spatial and commuting suprema.

## Reproduction and scope

Run **python verify.py 42** from the catalogue root. The launcher prepares the
included arithmetic libraries and executes the complete selected proof chain.
The supported environment is Windows x86-64 with CPython 3.12.
The selected stages are **verify_symbolic42_core.py**, **verify_twirl42.py**, **independent42.py**.
All coefficient tables, algebraic defining data and certificate inputs are
included in this entry. No optimizer, network access or external catalogue is
needed. The upper proof uses the universal reflection relations,
namely $A_i^2=B_j^2=I$ and $[A_i,B_j]=0$. Separate local ancilla dilations
cover binary effects without changing the relevant moments. Hence the upper
bound holds in arbitrary dimension and in the commuting model.
