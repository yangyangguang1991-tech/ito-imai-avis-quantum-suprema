# Exact quantum supremum of A20

The complete original probability matrix, including all marginal terms and the constant, is given in [definition.json](definition.json). The convention is $F=\sum_{i,j} C_{ij}P_iQ_j$, with $P_0=Q_0=I$. No further scaling or shift is made.

## Original functional and theorem
Use the frozen 4-setting Alice / 5-setting Bob probability coefficient table
in algebra/word_algebra/catalogue.json, id20, without translation or rescaling:
  [ 0,  0,-1,-2,-2, 0]
  [-3,  2, 2, 2, 2, 0]
  [ 0, -1,-1, 2, 0,-1]
  [-1, -1,-1, 0, 2, 1]
  [ 0, -1, 1, 0, 0, 0].
The top row/left column contain Bob/Alice marginals. With P=(I+A)/2,
Q=(I+B)/2, this is F=(1/4) sum_{i=0}^4 sum_{j=0}^5 T_ij A_i B_j,
where A_0=B_0=I and T is exactly the root-definition coefficient table.
The source file uses the opposite inequality direction; the frozen catalogue
records source_multiplier_for_F=-1. The table, rather than the historical label alone, fixes the normalization.

Let x_* be the unique zero of the nine rational first derivatives inside the
explicit rational box in A20_ROOT_DEFINITION.json. Let q_*=value(x_*).
The theorem established by the construction below is
  Q_fin(F)=Q_sp(F)=Q_com(F)=q_*.
The exact definition is an isolated algebraic root with rational box, not a
rounded decimal or merely a sequence of bounds. A nonsingular rational
polynomial system obtained by clearing the strictly positive chart
denominators establishes algebraicity. No minimal polynomial is needed for
this form of exact definition.

## 1. A legal attainer
The root verifier isolates x_* by a rational interval contraction argument and certifies
0<t_*<1. The stereographic Bloch formulas produce nine actual qubit
reflections with the frozen signs. The state is vec(diag(1,t_*))/sqrt(1+t_*^2).
Its score is q_* by direct substitution. This gives Q_fin>=q_*; restricted
Hessian or criticality alone is not used as a global upper bound.

## 2. Exact degree-two annihilator frames
The 62-word action matrix splits into character sectors of dimensions
9,13,19,21. Independently checked generic exact identities give respective
action-rank upper bounds 6,4,4,4:
  - the 9-dimensional sector uses CD/DC channels, with three explicit
    independent kernel vectors;
  - the other sectors use only D, C, or identity, each a 2-by-2 real channel.
The independent formal action calculation supplies these upper bounds.

The selected r-by-r action submatrix is invertible at the root by intervals.
For action matrix A with rows R and columns C, the frame defined by
  N_free=I, N_R=-A[R,C]^(-T) A[free,C]^T
satisfies N^T A[:,C]=0. The rank upper bound is essential: it implies every
other column lies in span A[:,C], hence N^T A=0 EXACTLY. An interval residual
containing zero would not imply this. These are full annihilator frames of
dimensions 3,9,15,17; they have 324 symmetric Gram coordinates altogether.

## 3. Why rank215 plus 24 exact compatibility relations is enough
Let Fmap:R^324->R^239 be the symmetric degree-two coefficient map compressed
by signed orbit SUMS. Let b be the same compression of q_*I-F. The 24 columns
of L comprise 13 exact moment/first-derivative functionals, 9 integer constant
identities, the inherited six-term identity and the new seventeen-term one.

The identities establish L^T Fmap=0 and L^T b=0 exactly. For the jets,
annihilation follows from p|psi>=r|psi>=0, while target compatibility follows
from full complex first-order stationarity. For the 11 non-jet functionals,
the separate symbolic checks establish annihilation; their length-four
support gives target compatibility because b has degree at most two.
The rank24 interval certificate proves rank L=24. The rank215 interval
certificate proves rank Fmap>=215. Therefore
  rank Fmap=215 and im Fmap=ker L^T,
and b belongs to im Fmap. No unproved claim that the 13 jets span all jets
or that the 24 relations were discovered exhaustively is required.

In particular, the exact correction to 215 selected Gram coordinates, obtained
by solving the chosen invertible 215-by-215 minor on 215 selected rows,
satisfies all 239 equations. Indeed the residual lies in im Fmap, and selected
row restriction is injective on that 215-dimensional image. The correction
is a rational function of x_*; a rational outward interval can enclose it.

The orbit normalization matters: coefficient vectors use signed SUMS; physical
moment jets use signed AVERAGES. The scripts use this dual normalization.
The coefficient table and the Gram are invariant under the exact four-element
symmetry group, so matching its 239 orbit sums matches all original coefficient
equations, including symmetry-forced zero orbits. Real symmetric Gram matrices
pair adjoint words equally, so using adjoint-paired coefficient classes loses
no self-adjoint polynomial equation.

## 4. Embed and add universal polynomial-zero directions
Embed the exact, possibly indefinite, 62-word Gram into the 142-word ABB basis.
For each of the fifteen declared unitary words u_d, choose its domain I_d so
u_d w_i stays within the basis, and denote the image J_d. Every u_d is a
product of reflections, hence u_d^*u_d=I in the universal bipartite algebra.

The domain-rank identities plus interval nonsingular pivot matrices prove
each N_d^T V[I_d,:]=0 exactly. Put R0_d=embed(I_d,N_d), R1_d=embed(J_d,N_d).
For any fixed rational symmetric H_d,
  w^*(R0_d H_d R0_d^T-R1_d H_d R1_d^T)w=0
universally: this is p^*H_d p-(u_d p)^*H_d(u_d p).
No auxiliary-family restriction is imposed on arbitrary competitors in this
identity. The domain annihilation is needed separately to ensure that both
R0_d and R1_d kill the candidate action columns, hence the assembled raw Gram
annihilates them. The image annihilation follows from left multiplication of
the exactly zero polynomial action, not from a small numerical residual.

## 5. Twirl, then prove PSD by a nonorthogonal complement
Twirl the assembled raw Gram over the four exact catalogue symmetries. This
preserves the represented target polynomial. The review independently checks
that the two generators are exactly D->-D and C->-C on the formal action,
so their common annihilator is invariant and G V_*=0 survives twirling.
Here V_* contains the selected 21 formal action columns.

Let Q have 121 rational columns projected exactly into the four distinct
character sectors, with column counts 24,20,38,39. The certified invertibility
of X=[V_*,Q] proves it is a complement. Since the twirled G is invariant,
cross-character terms of Q^T G Q vanish exactly. Its four diagonal blocks
are the blocks formed in certify_proposal.py. Their strict positive interval LDL pivots establish the exact congruence
  X^T G X = diag(0_21,H24,H20,H38,H39) >= 0.
Thus G>=0, of rank121. Q need not be orthogonal, and no separate full ABB
coefficient-map rank, full kernel span, or rank21 upper bound is needed.

## 6. Universal bound and model scope
The final identity q_*I-F=w^*G w is in the universal algebra with only
  A_i^2=B_j^2=I and [A_i,B_j]=0.
The use of candidate-root equations in scalar coefficients does not impose
candidate measurement identities on competing operators. Positive G gives
q_*I-F>=0 for every Hilbert-space representation, including the commuting
model. The legal finite-dimensional attainer gives the reverse inequality;
finite <= spatial <= commuting then forces equality in all three models.

Binary POVMs can be included by dilation. A self-adjoint contraction A dilates
to [[A,sqrt(I-A^2)],[sqrt(I-A^2),-A]]. Put Alice's and Bob's ancillary two-space
factors separately. Functional calculus preserves every cross-party
commutator, so the dilated families commute across parties and compression
of their pair products recovers the original binary-POVM correlations. The
universal reflection upper bound therefore includes binary POVMs as well.



## Explicit matrix convention

Write the isolated root as $x_*=(t,a,u,v,b,c,d,e,h)$. The rational centre,
radius and inverse-Jacobian proposal are in
`algebra/root/A20_ROOT_DEFINITION.json`. Expand its coordinates as

$$z=(t,a,u,v,u,-v,b,0,c,0,d,0,e,h,e,-h,0,1).$$

There are nine reflections, Alice's four followed by Bob's five. For setting
$j=0$ use $(u_j,v_j)=(z_1,0)$; for $1\le j\le8$ use
$(u_j,v_j)=(z_{2j},z_{2j+1})$. With the corresponding exact sign
$\epsilon_j$ stored in the root definition, set

$$n_j=\frac{\epsilon_j}{1+u_j^2+v_j^2}(2u_j,2v_j,1-u_j^2-v_j^2),
\qquad R_j=\begin{pmatrix}(n_j)_z&(n_j)_x-i(n_j)_y\\
(n_j)_x+i(n_j)_y&-(n_j)_z\end{pmatrix}.$$

Take $A_i=R_{i-1}$, $B_j=R_{3+j}$ and the state
$(|00\rangle+t|11\rangle)/\sqrt{1+t^2}$. All projections are $(I+R_j)/2$.
If $T$ denotes the complete reflection table for $4F$, the rational score is

$$f(x)=\frac14\left[T_{00}+\frac{1-t^2}{1+t^2}
\left(\sum_iT_{i0}a_{iz}+\sum_jT_{0j}b_{jz}\right)
+\sum_{ij}T_{ij}\left(a_{iz}b_{jz}+\frac{2t}{1+t^2}
(a_{ix}b_{jx}-a_{iy}b_{jy})\right)\right].$$

Here $a_i,b_j$ are the indicated Bloch vectors. This specifies the state,
measurements and value without a rounded numerical surrogate.

## Reproduction

Run `python verify.py 20` at the catalogue root. The complete sequence is
`run_all.py`: literal coefficients, root isolation, full first-order identities,
independent action ranks, six-term and seventeen-term compatibility, negative
controls, the 24-dimensional left kernel and 215-dimensional coefficient range,
all fifteen unitary domains, the exact word/twirl identities, and the final
Gram positivity checked again by a separate interval LDL calculation.
All intermediate results are generated in a temporary directory. No archived
pass report is used as a substitute for one of these stages.
