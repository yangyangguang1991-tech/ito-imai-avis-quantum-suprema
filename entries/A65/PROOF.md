# Exact quantum supremum of A65

The complete original probability matrix, including all marginal terms and the constant, is given in [definition.json](definition.json). The convention is $F=\sum_{i,j} C_{ij}P_iQ_j$, with $P_0=Q_0=I$. No further scaling or shift is made.

## 1. Frozen objective and normalization

Write P0=Q0=I and let Pi,Qj, i,j=1,...,5, be binary projectors. The frozen
probability objective is F=sum_{i,j=0}^5 Cij Pi Qj, with the full matrix

 C = [ 0   0  -1  -1  -1   0
       0  -1  -1  -1   1   0
       0  -1   1   0   0  -1
      -1  -1   0   1   0   1
      -1   1   1   0   1   0
      -1   0   0   1   1   0 ].

The first row and column contain Bob and Alice marginal coefficients; C00
is the constant. This is minus the literal polynomial in the archived A65
source, with no further scale or constant adjustment. Direct enumeration of
the 1024 deterministic assignments gives local maximum zero. The source hash
and exact integer matrix are bound by the root-definition JSON.

Introduce reflections Ai=2Pi-I and Bj=2Qj-I. The universal upper certificate
uses only Ai*=Ai, Bj*=Bj, Ai^2=Bj^2=I and Ai Bj=Bj Ai. Different measurements
on the same side are never commuted.

## 2. An explicit finite algebraic number

The complete exact definition is A65_FIXED_ROOT_DEFINITION.json together
with fixed_family65.py and the original A65_ROOT_DEFINITION.json. The latter
records a rational 60-coordinate center, radius 10^-60, all projector chart
pivots and complements, and a rational preconditioner. No decimal is used as
the definition of the optimum.

For a rank-r chart, put a 5-by-r matrix V equal to the identity in its listed
pivot rows and to the specified chart coordinates in its other rows. Define
P=V(V^T V)^(-1)V^T, or its complement I-P when the metadata says so. The ten
charts use r=1 or2. Their 56 real parameters, followed by four positive
Schmidt ratios, constitute the full coordinates. Let t=(1,t2,t3,t4,t5) and
let the state be

  |psi(t)> = (sum_{a=1}^5 ta |a,a>)/sqrt(sum_a ta^2).

For these charts define the explicit rational function

  f(x)= [sum_{i,j=0}^5 Cij sum_{a,b=1}^5
                      ta tb (Pi)ab (Qj)ab] / sum_a ta^2.

The box verifier applies a rationally preconditioned contraction to grad f
and checks a strictly negative Hessian throughout the box. Thus there is one
stationary root x* in that box. Every projector is legal there, and all five
Schmidt coefficients are positive and distinct. The root is an isolated real
solution of a rational polynomial system after denominators are cleared;
its coordinates, and hence q*=f(x*), are algebraic.

 Root isolation gives an actual
attaining strategy on C^5 tensor C^5. The global upper bound is supplied by the subsequent universal SOS identity.

## 3. Exact symmetry and the smaller coordinate system

Let p=(1,4,3,2,5), epsilon=(1,-1,1,-1,1), in one-based indexing, and
D=diag(1,-1,-1,1,-1). The Bell polynomial is invariant under swapping the
parties, relabeling both by p and flipping outcomes with signs epsilon.
The full chart transforms by an exact signed coordinate involution T.
That involution fixes the rational center and maps its uniform box onto
itself. Uniqueness of the stationary root therefore gives

 Qj = D[(1-epsilon_j)I/2 + epsilon_j P_{p(j)}]D

at x*. This statement concerns the attaining candidate; it is not imposed
on arbitrary competing quantum strategies.

The fixed subspace has32 coordinates:28 Alice chart coordinates and four
Schmidt ratios. An explicit integer embedding E into the60 full coordinates
satisfies

  E (E^T E)^(-1) E^T = (I+T)/2,
  E^T E = diag(2,...,2,1,1,1,1).

Invariance of f implies that at a fixed point grad f lies in this fixed
subspace. Therefore stationarity of the32-coordinate restricted function is
equivalent to all60 stationary equations. This justifies using its32
derivatives in the coefficient compatibility argument below.

## 4. Universal words and the annihilator frame

Let w contain the following276 reflection words:
 I; Ai; Bj; Ai Bj; Ai Ak (i!=k); Bj Bl (j!=l);
 Ai Ak Bj (i!=k); Ai Bj Bl (j!=l).

The candidate action of a word is the vectorization of A_word S B_word^T,
where S=diag(t). The signed swap acts on such matrices as M -> D M^T D.
Its positive and negative eigenspaces have dimensions15 and10, since D M
is respectively symmetric or skew-symmetric. The word space has character
dimensions141 and135. Checked interval minors attain the action dimensions
15 and10 on the entire root box. Therefore the exact annihilator dimensions
are126 and125.

Within each character choose the listed pivot action rows Fp. A remaining
row Fr is eliminated by the rational identity

  er - Fr Fp^(-1) ep.

These columns give rational-function matrices N+(x), N-(x). Their values at
x* annihilate the physical word-action vector. The inverse pivots are
verified by outward rational interval arithmetic. The coefficients use
rational character sums rather than floating square-root normalizations.

## 5. Coefficient map and the exact compatibility mechanism

Take a real symmetric Gram block G+ of order126 and G- of order125. Their
universal polynomial is

 w* [N+ G+ N+^T + N- G- N-^T] w.

Reduce words only by adjacent reflection cancellations and cross-party
commutation, and identify adjoint pairs in a self-adjoint polynomial. The
two-term signed swap preserves both the target and each character Gram
block. Hence equality of7191 signed orbit coefficient sums is equivalent
to equality of the full invariant universal polynomials.

Let L be the7191-by15876 coefficient map acting on raw upper-triangular
Gram entries, and let b encode q* I-F. Put

 Delta = diag(1 for diagonal entries, 1/2 for off-diagonal entries).

Let J have33 columns: normalized signed orbit moments of the physical
candidate and their32 fixed-family derivatives. For fixed N(x*) every
annihilator square and every polarized cross term has zero expectation and
zero first derivative at x*. Consequently

  L^T J = 0.

The first component of J^T b is q*-f(x*)=0. The other32 components are
-partial_k f(x*)=0. Consequently

  J^T b = 0.

These are exact structural identities. A small numerical value for either
residual would not suffice. The signed moment for an orbit is its signed
average; the implementation may use one representative because all fixed-
family strategies and their derivatives respect the swap symmetry.

## 6. Exact correction of a nearby positive Gram matrix

Set H=[L J] and

  K = L Delta L^T + J J^T.

The exact normal-map certificate proves K invertible. Let G0 be the supplied
dyadic Gram blocks, with g0 their raw upper-triangular entries. Define

  r = b-Lg0,
  delta_g = Delta L^T K^(-1) r,
  g = g0+delta_g.

Because L^T J=0 and J^T r=0, K preserves range(J) and its orthogonal
complement. It follows that J^T K^(-1)r=0 and hence

  L delta_g = r,     Lg=b.

Thus the corrected coefficients satisfy the operator identity exactly,
without raising q* by a residual-compensation term. All coefficients belong
to the algebraic field generated by x*.

The exact verifiers establish:
 (a) certify K invertible by an outward interval enclosure and a rational
     inverse proposal P with ||I-PK||_infinity<1;
 (b) certify G0 has a strict positive margin, using exact outward arithmetic;
 (c) bound the correction strongly enough that both final blocks remain
     positive definite.

The construction of the approximate inverse uses floating arithmetic only
to propose integers. Its final residual is checked through bounded integer
digit products and Python integer reconstruction, with explicit overflow
and exact-representability guards. Rounded normal-matrix error and interval
error in H must both enter the Neumann bound.

These three strict inequalities give the universal identity

  q* I - F = w* [N+ G+ N+^T + N- G- N-^T] w,  G+,G- positive definite.

This implies an upper bound in every representation of the universal
bipartite reflection algebra, including arbitrary complex Hilbert spaces
and the commuting-operator model. Combined with the explicit five-dimensional
local strategy it proves

  Q_fin(A65)=Q_sp(A65)=Q_com(A65)=q*.

Binary POVMs are included by commuting partywise reflection dilations. For
a self-adjoint contraction A, the usual block reflection with diagonal A,-A
and off-diagonal sqrt(I-A^2) preserves all required compressed expectations.
Separate ancillas on the two sides preserve cross-party commutation.


## Independent coefficient and arithmetic checks

The independent interface verifier reconstructs the literal polynomial on all
1024 deterministic assignments, checks the signed character action on all276
words and compares7191 coefficient equations against a separate free-word
expansion. A separate integer congruence checker repeats positivity of the two
Gram blocks. The final scalar review independently recomputes the correction
bound and the strictly remaining positive margin from the freshly generated
exact quantities.

## Reproduction

Run `python verify.py 65` from the catalogue root. The selected complete program
is `algebra/certificate/verify_complete.py`. Its strategy directory contains the
full root, symmetry-fixed root and character definitions. Its gram directory
contains the exact dyadic Gram seed. It freshly constructs the interval frame,
integer normal matrix and inverse certificate, then checks the corrected Gram,
independent integer positivity, coefficient interfaces and final scalar bounds.
All prerequisite result files are produced by these checks in their specified
order. The exact value is the isolated algebraic root evaluation above; the
finite five-dimensional strategy actually attains it.
