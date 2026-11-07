# A60: exact quantum supremum

## 1. Normalization and statement

For binary projections $P_i,Q_j$, put $P_0=Q_0=\mathbb{I}$ and

$$

 F_{60}=\sum_{i,j=0}^{5} C_{ij}P_iQ_j,\qquad
 C=\begin{pmatrix}
0&0&-1&-1&-1&0\\
0&-1&0&-1&1&-1\\
-1&0&-1&1&1&0\\
-1&-1&1&0&0&1\\
-1&1&1&0&1&0\\
0&-1&0&1&0&0
\end{pmatrix}.

$$

All marginal terms are included. The archived literal source uses minimization of $-F_{60}$; no further scaling or constant shift is applied. All $2^{10}$ deterministic assignments have score at most zero, and 67 attain zero. Set $A_i=2P_i-\mathbb{I}$ and $B_j=2Q_j-\mathbb{I}$. The reflection constant in $F_{60}$ is $-9/4$.

Let $Q_{\rm fin},Q_{\rm sp},Q_{\rm com}$ denote, respectively, the finite-dimensional tensor-product, spatial tensor-product, and commuting-operator suprema. Section 2 defines a particular real algebraic number $q_*=f(x_*)$ without using its decimal expansion as a definition.

**Theorem 1.**

For the normalization and isolated root specified below,

$$

 Q_{\rm fin}(F_{60})=Q_{\rm sp}(F_{60})=Q_{\rm com}(F_{60})=q_*.

$$

The value is attained on $\mathbb C^5\otimes\mathbb C^5$, and begins

$$

q_*=0.394003195337191282099869789055308985294299259572039670\ldots.

$$

The upper-bound identity uses only $A_i^2=B_j^2=\mathbb{I}$ and $[A_i,B_j]=0$.

The finite checks are supplied, not assumed as numerical evidence. The final assembler accepts the theorem only when all dependency bindings, normal ranks, inverse bounds and positivity inequalities pass. Neither a displayed zero gap nor an isolated candidate alone proves this theorem.

## 2. The exact root and attaining strategy

An ordered graph chart $\mathcal G_{d,p}(z)$ is the $d$ by $|p|$ matrix whose ordered pivot rows are the identity and whose other rows, in increasing row order, are filled with $z$ in row-major order. For a full-column-rank matrix $V$, write $\Pi(V)=V(V^{\mathsf T}V)^{-1}V^{\mathsf T}$.

For $x=(x_1,\ldots,x_{30})$ use the four zero-based ordered pivot lists

$$

(1,3),\quad(3,1),\quad(0,4),\quad(0).

$$

The first 22 coordinates fill their graph matrices $U_1,U_2,U_3,U_4$, of ranks $2,2,2,1$. Put

$$

P_i=\Pi(U_i)\ (i=1,2,3),\qquad P_4=\mathbb{I}-\Pi(U_4),\qquad
S=\operatorname{diag}(1,x_{27},x_{28},x_{29},x_{30}).

$$

Let $R=S[U_1\ U_3]$. The next four coordinates $x_{23},\ldots,x_{26}$ fill a $4$ by $2$ graph $Y$ with ordered pivot rows $(3,2)$. Set

$$

P_5=Q=\Pi(RY),\qquad
f(x)=\frac{\sum_{i,j=0}^{5}C_{ij}\operatorname{tr}(SP_iSP_j^{\mathsf T})}{\operatorname{tr}(S^2)}.

$$

Here $P_0=\mathbb{I}$. The exact rational center $x_0$ and rational preconditioner are given in the included file `A60_ROOT_DEFINITION.json`. Define

$$

 X=x_0+[-10^{-65},10^{-65}]^{30},\qquad
 \nabla f(x_*)=0,\quad x_*\in X,\qquad q_*=f(x_*).

$$

The center coordinates are exact terminating decimals; neither a rounded center nor an approximate root is substituted in the theorem.

The replay proves strict contraction and strict self-inclusion for $x\mapsto x-R_{\rm pre}\nabla f(x)$ throughout $X$, using 384-bit integer outward intervals. In particular the stationary root exists and is unique. The same bounds imply invertibility of the preconditioner and Hessian. Every graph denominator is bounded away from zero. The support $R$ has rank four, and the signed entries of $S$ are nonzero and pairwise distinct. These checks also establish that the rational formulas are defined throughout $X$.

Both parties use the five projectors $P_1,\ldots,P_5$. Their ranks are $(2,2,2,4,2)$, and

$$

 |\psi\rangle=\frac{\operatorname{vec}S}{\sqrt{\operatorname{tr}(S^2)}}.

$$

This is a legal finite-dimensional strategy with expectation exactly $f(x_*)$. The independent exporter reconstructs the graph projectors, checks rational-center symmetry, idempotence and ranks, and computes the full $25$ by $25$ Kronecker Bell matrix. It exports the normalized state, all measurement matrices, and rational entry enclosures at the exact root. Decimal matrices are for inspection; the root and rational formulas specify the exact strategy.

## 3. Full stationarity and an equal-score family

Let $K=\mathbb{I}-\Pi(R)=hh^{\mathsf T}$ with $\|h\|=1$. The graph construction gives

$$

 P_1Sh=P_3Sh=0,\qquad Qh=0.

$$

The special response is $D=S(P_3-P_1)S$. It kills $h$. Stationarity in the $Y$ chart proves that $Q$ commutes with $D$ on $\operatorname{ran}R$; both vanish on $h$, so the full commutator is zero. Changes induced in $Q$ by variations of earlier graph coordinates consequently contribute zero to the first derivative. The other graph charts span their full rank-preserving tangent spaces. Party symmetry splits each shared measurement derivative into two equal one-party derivatives, hence both vanish.

The diagonal-state derivatives vanish by stationarity and homogeneity. Simultaneous orthogonal conjugation is a gauge symmetry. Since measurement derivatives already vanish, this gives vanishing state derivatives in directions $[L,S]$ for real skew matrices $L$. Distinct signed entries of $S$ make these directions span the symmetric off-diagonal matrices. The Bell action on $S$ is symmetric, so its residual is orthogonal to all antisymmetric directions too. Thus

$$

 F_{60}\operatorname{vec}S=q_*\operatorname{vec}S.

$$

Purely imaginary first variations vanish at this real strategy. This is full complex stationarity, not an assumption of global optimality.

Write $r_i=2P_i-\mathbb{I}$ and $C_s=2Q-\mathbb{I}+K$. For either party independently choose an auxiliary Hilbert space, a unit vector $e$, four arbitrary auxiliary reflections $H_i$, and $D_0=D_0^*$ with $D_0e=0$ and $D_0^2=\mathbb{I}-ee^*$. For $t\in[-1,1]$, define

$$

 R_i=r_i\oplus H_i\quad(i\le4),\qquad
 R_5(t)=\begin{pmatrix}C_s+tK&\sqrt{1-t^2}\,he^*\\
 \sqrt{1-t^2}\,eh^*&D_0-tee^*\end{pmatrix}.

$$

These are self-adjoint involutions. The only special-setting terms are

$$

P_5(Q_3-Q_1)+(P_3-P_1)Q_5;

$$

there is no $P_5Q_5$ term. Each change annihilates the core state. Ordinary responses change only by multiples of $SKS$ at settings 1 and 3, which commute with the relevant projectors. The special response kills the entire changed subspace. Therefore this whole family has the same Bell eigenaction and is fully stationary, with arbitrary complex auxiliaries on both parties.

## 4. Universal word action and the sixteen coordinate axes

Take all reduced reflection words of total degree at most three and local degree at most two. There are

$$

 276=76+100+100

$$

words: the words through total degree two, followed by $A_iA_kB_j$ and $A_iB_jB_k$ with unequal adjacent same-party letters. This is the historical level $2b$ word set.

A reference family member has five core coordinates, one auxiliary root, and four ordinary auxiliary leaves. At $t=0$ the special reflection swaps $h$ with the root; ordinary auxiliary reflections interchange the root and their leaf. Complete unused boundary edges by $+1$ loops. For any family member, put $\eta=R_5h$. The map that fixes the core and sends a tree node $u$ to $R_u\eta$ intertwines every required word action, because $R_5\eta=h$ and

$$

 R_5x=C_sx+\eta\langle h,x\rangle\quad(x\text{ in the core}).

$$

The map need not be isometric. This proves that the common action kernel of the entire family equals the kernel of the reference action.

Let $H_0$ be core plus root, and let $F_0$ span the four leaves. The action lies in

$$

 (H_0\otimes H_0)\oplus(F_0\otimes U)\oplus(U\otimes F_0),

$$

where

$$

 U=\operatorname{span}\{Sh,r_2Sh,r_4Sh,C_sSh+(h^{\mathsf T}Sh)e\}.

$$

Hence the action rank is at most $36+16+16=68$. Under party exchange, the upper bounds are 37 and 31. Exact interval minors of these orders prove both equalities. The raw word character dimensions are 141 and 135, so both common-kernel dimensions are 104.

For each ordinary Alice leaf $i$, its $r_2Sh$ and $r_4Sh$ components are reached uniquely by $A_iA_5B_2$ and $A_iA_5B_4$, respectively. The matching rank 68 proves that the four vectors spanning $U$ are independent. Dual coordinates therefore isolate these sixteen words, including their Bob counterparts. Their eight pairs give eight coordinate axes in each character space. In a normalized action matrix $T$ with $T_P=\mathbb{I}$, the corresponding columns are exactly coordinate vectors. Consequently any same-value positive Gram has those sixteen character rows zero. This concerns Gram rows; the individual unitary words do not annihilate the state.

## 5. Complete coefficient compatibility

Use the unnormalized rational character words $w_i+w_{\tau i}$ and $w_i-w_{\tau i}$, with singleton words in the plus sector. For two real symmetric character Gram matrices $H_+,H_-$, let $h$ consist of diagonal entries and twice the upper off-diagonal entries. There are 19,191 such coordinates. The exact coefficient map

$$

 C_{\rm coeff}:\mathbb R^{19191}\longrightarrow\mathbb R^{7191}

$$

uses coefficients summed over adjoint and party-swap orbits. Equivalently the corresponding polynomial basis is the average over each orbit. The checker regenerates every word product using only reflection cancellation and cross-party commutation.

Integer sparse matrices $R_4,K_4$ satisfy

$$

 C_{\rm coeff}R_4=4\mathbb{I},\qquad C_{\rm coeff}K_4=0,

$$

and a 12,000-row submatrix of $K_4$ is $4\mathbb{I}$. Thus $R=R_4/4$ is a right inverse and $K=K_4/4$ is a full coefficient-kernel basis.

The equations $H_\pm T_\pm=0$ have 8,271 independent symmetric coordinates: all free rows and the upper triangular pivot rows. Denote this linear map by $E$. Set $M=EK$. An exact inverse-defect certificate proves that a specified $6,868$ by $6,868$ minor of $M$ is invertible at $x_*$. Root perturbations of every normalized action entry are included in this check.

There are 1,403 independent compatible coefficient functionals, comprising 979 state-action functionals, 120 measurement first variations, and 304 local identities. The state words require local degree at most four and are evaluated on a legal 90-dimensional reference tree. Measurement templates use the five-dimensional core generators and eighteen opposite-party metric directions: one constant, ten real auxiliary off-diagonal, six imaginary auxiliary off-diagonal, and one core-auxiliary cross direction. Each is a real linear combination of legal stationary-family metrics. For any face polynomial $n^*Hn$, $n\psi=0$ on the whole family, so both its state action and its measurement first variations vanish. The same functionals vanish on $q_*\mathbb{I}-F_{60}$ by the stationary-family theorem.

The 304 local identities use the sixteen exact axis columns above. Here twice a face row is an integer Gram-coordinate selector. Exact multiplication with $K_4$ proves 48 zero rows and 256 two-row relations. Their coefficient lifts have only 380 nonzero integer numerators, denominator eight, and satisfy

$$

 (N_8/8)C_{\rm coeff}=LE,\qquad N_8 b(q)=0\quad\text{for every }q.

$$

The last identity holds because their support avoids every Bell coefficient orbit. It does not rely on a numerical cancellation at $q_*$.

An independently reconstructed 1,403-square coefficient-normal minor has an exact interval inverse defect below one. Since $C_{\rm coeff}$ is onto, independence of these coefficient normals implies independence of their lifted left normals of $E$. They annihilate $M$ and $Eh_a(q_*)$, where $h_a$ is any exact coefficient solution. Finally,

$$

 1403+6868=8271.

$$

The displayed normals therefore exhaust the left kernel of $M$. This is the required complete compatibility theorem. No claim that a selected physical parameter sampling is intrinsically complete is used in this final dimension argument.

## 6. Correction at the same algebraic value

A rational reference has both 104-dimensional free blocks bounded below by

$$

 \eta\mathbb{I},\qquad \eta=2^{-28}.

$$

The proof applies rational approximate inverse-Cholesky congruences and verifies every resulting product with exact integers. It is not a floating eigenvalue test. Let $b(q)=\operatorname{coeff}(q\mathbb{I}-F_{60})$, and form the exact affine reference

$$

 h_a(q)=h_0+R\bigl(b(q)-C_{\rm coeff}h_0\bigr).

$$

Then $C_{\rm coeff}h_a(q)=b(q)$ identically. At the exact root, certified bounds are

$$

 \|h_a(q_*)-h_0\|_\infty<2.240\times10^{-63},\quad
 \|Eh_a(q_*)\|_\infty<2.037\times10^{-53},\quad
 \|K\|_\infty=1760.

$$

The certified complementary inverse norm is less than $332775$. Solve the selected equations for a coefficient-kernel correction and set its other coordinates to zero. Complete compatibility proves that this solution satisfies every face equation. The induced change in either free Gram block has operator norm at most

$$

 104\left(2.240\times10^{-63}
       +1760\cdot332775\cdot2.037\times10^{-53}\right)<\eta.

$$

All final comparisons use the exact rational bounds in the receipts, rather than these displayed rounded bounds. The corrected blocks are strictly positive and the coefficient identity remains at $q_*$ exactly.

For the resulting kernel polynomials $n_+,n_-$,

$$

 q_*\mathbb{I}-F_{60}=n_+^*G_+n_++n_-^*G_-n_-,\qquad
 G_+,G_-\succ0,\quad G_\pm\in\mathbb R^{104\times104}.

$$

The coefficients are explicitly defined algebraic quantities: the isolated root, rational normalized actions, rational reference, and the inverse of the specified nonsingular minor. This is a finite exact construction, even though the full corrected matrices are not printed as enormous algebraic fractions.

The identity is universal in the commuting reflection algebra and proves the unrestricted upper bound. The five-dimensional strategy proves the matching lower bound. Binary POVMs are covered by local projective dilations, preserving all cross-party commutation relations. Together with the finite exact verifications specified above, this proves Theorem 1.

## Reproduction and exact representation

Run the entry through the repository verifier as described in README.md.
The archive contains the complete coefficient table, the rational center and
preconditioner defining the isolated root, selected minor indices, exact
coefficient maps, and all programs used by the proof. Mathematical supplements
inside the archive give the detailed finite-tree, stationarity, and compatibility
arguments used above. Every numerical inverse or reference matrix is an input
to exact verification, not an assumed certificate of positivity or rank.

The exact attaining state and measurements are the graph-projector and Schmidt
formulas at the unique isolated root. Exported decimal matrices are evaluations
of those formulas, not replacements for the algebraic definitions. A complete
replay checks the original Bell coefficients, root isolation, all complementary
minor rows, compatibility, positive correction, and the independent physical
score. No external data file, solver service, or original research directory is
required.
