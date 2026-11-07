# A67: exact quantum supremum

## 1. The frozen inequality and the exact number

Put $P_0=Q_0=\mathbb{I}$ and

$$

 F=\sum_{i,j=0}^5 C_{ij}P_iQ_j,\qquad
 C=\begin{pmatrix}
0&0&-1&-1&-1&0\\
0&-1&0&-1&1&-1\\
-1&-1&-1&0&1&1\\
-1&1&1&0&1&0\\
0&-1&0&1&0&0\\
-1&0&1&1&0&0
\end{pmatrix}.

$$

All marginal terms are retained. The public source file minimizes $-F$; the convention here maximizes $F$, without a scale change or an additive shift. Its 653-byte literal source has SHA256

`812b843b6a813074758a1c09ee7ee101bc859ac3ae6f1ea023046277e96cc190`.

The local deterministic maximum is zero. The coefficient of $Q_5$ is exactly $P_2-P_1$.

Here is a finite exact definition of the constant. The file `A67_ROOT_DEFINITION.json` specifies ten graph charts with two pivot rows each, sixty rational graph coordinates and four Schmidt coordinates. For a chart $U\in\mathbb R^{5\times2}$ with the specified $2\times2$ identity pivot, set

$$

 \Pi(U)=U(U^{\mathsf T}U)^{-1}U^{\mathsf T}.

$$

Use $\Pi(U)$ or its complement according to the frozen rank pattern

$$

 (\operatorname{rank} P_1,\ldots,\operatorname{rank} P_5;\operatorname{rank} Q_1,\ldots,\operatorname{rank} Q_5)
 =(2,2,3,3,3;2,3,3,3,2).

$$

Write $s=(1,x_{61},x_{62},x_{63},x_{64})$ and $S=\operatorname{diag}s$. With $A_0=B_0=\mathbb{I}$, $A_i=P_i$, $B_j=Q_j$, define the rational function

$$

 f(x)=\frac{\sum_{i,j=0}^5 C_{ij}\sum_{a,b=1}^5
 s_as_b(A_i)_{ab}(B_j)_{ab}}{\sum_a s_a^2}.

$$

Let $c\in\mathbb Q^{64}$ be the center recorded in that file and let

$$

 X=\prod_{a=1}^{64}[c_a-10^{-65},c_a+10^{-65}].

$$

The exact number used below is

$$

 \boxed{q_*=f(x_*),\qquad \nabla f(x_*)=0,\quad x_*\in X.}

$$

The root file hash is

`cb4be65e31be0000530d379a25e2f0f4ac0fc9be4ebbb04a4fb88dc77e3617f5`.

The rational box, chart choices and rational equations are part of the definition; decimal recognition is not used. The root verifier applies a rational preconditioned fixed-point map to $\nabla f$, proves strict inclusion in the exact rational box and contraction below one, and proves all Schmidt coefficients positive and distinct. Thus $x_*$ exists uniquely in $X$. Clearing the graph and normalization denominators gives polynomial equations over $\mathbb Q$ with a nonsingular isolated root, so $x_*$ and $q_*$ are algebraic. Numerically,

$$

 q_*=0.39906710294171027532265300958520463460099830075289\ldots .

$$

This is an implicit algebraic specification, not a claimed radical expression or minimal polynomial.

**Theorem 1.**

For the displayed frozen inequality,

$$

 \boxed{Q_{\mathrm{fin}}(A_{67})=Q_{\mathrm{sp}}(A_{67})
 =Q_{\mathrm{com}}(A_{67})=q_*.}

$$

The value is attained with the rank-pattern strategy defined above and

$$

 |\psi_*\rangle=\frac{\sum_{a=1}^5s_a|aa\rangle}{\sqrt{\sum_as_a^2}}.

$$

The upper certificate uses only $a_i^2=b_j^2=\mathbb{I}$, self-adjointness and $[a_i,b_j]=0$, where $P_i=(\mathbb{I}+a_i)/2$ and $Q_j=(\mathbb{I}+b_j)/2$. It does not impose the candidate's finite-dimensional relations on competing strategies.

## 2. A stationary family and its word-action kernel

Let $k$ be the signed cofactor vector of the $5\times4$ matrix $S[U_1\ U_2]$, and put $K=kk^{\mathsf T}/(k^{\mathsf T}k)$. Exact chart identities give $P_1Sk=P_2Sk=0$. The root and response checks give $Q_5k=0$ and a one-dimensional kernel of $D=S(P_2-P_1)S$, certified by $\det(D+K)\ne0$. Projector stationarity implies $[Q_5,D]=0$; the selected kernel occupation is fixed by an interval separation.

On an arbitrary complex auxiliary Bob space $E$, let

$$

 Q'_j=Q_j\oplus Z_j\ (j\le4),\qquad
 Q'_5=(Q_5\oplus0)+L,

$$

where $Z_j$ are arbitrary projections and $L$ is any projection on $\operatorname{span}\{k\}\oplus E$. Embed the same state with no auxiliary component. The fifth-setting coefficient and $P_1Sk=P_2Sk=0$ imply $F'\psi_*=q_*\psi_*$. Bob's response operators are the original core responses extended by zero. Alice's first two responses change by opposite scalar multiples of $SKS$, which commute with the respective projectors. All state and unitary-measurement first variations therefore vanish throughout this family.

The passage from the 64-variable chart to full stationarity uses the singular-value decomposition of a real state matrix: positive distinct Schmidt coefficients allow every infinitesimal state change to be written as a diagonal variation and two local orthogonal variations. Complex imaginary variations at the real core have zero first derivative. The response argument above then extends stationarity to the entire complex family.

Let $w$ contain all reduced reflection words of total degree at most three, except the sixteen pure-Bob words

$$

 b_i b_j b_5\ (i\ne j\le4),\qquad b_5b_jb_5\ (j\le4).

$$

There are 420 retained words. The arbitrary-family action is captured by a finite tree representation: ordinary letters prepend or cancel on spectator nodes, and the special letter exchanges the kernel direction with the root. Boundary nodes outside the required depth are fixed. This is a legal reflection representation, and a linear intertwiner, not necessarily an isometry, sends it to every family member. The certified endpoint and boundary-frame calculations show that the common action on the retained words has rank 50.

Choose the 50 pivot words and 370 free words in `FACE_DEFINITION.json`. Normalize the exact action matrix to

$$

 \widehat V_{\mathrm{piv}}=I_{50},\qquad \widehat V_{\mathrm{free}}=T,
 \qquad N_{\mathrm{piv}}=-T^{\mathsf T},\quad N_{\mathrm{free}}=I_{370}.

$$

Thus $N^{\mathsf T}w\psi_*=0$ at every family member. The analytical tree argument and the interval pivot checks establish the common-kernel statement; samples alone would not establish it.

## 3. The coefficient problem

Represent a real symmetric $420\times420$ Gram matrix by coordinates $g_{ii}=G_{ii}$ and $g_{ij}=2G_{ij}$ for $i<j$. There are 88410 coordinates. After reducing only involutions and cross-party commutation, $w^*Gw$ has 26430 real Hermitian word classes. Its coefficient map $\mathcal C$ has one unit entry per column. Choosing one representative per class gives

$$

 \mathcal C R=I,
 \qquad K_0e_j=e_{\mathrm{nonrep}(j)}-e_{\mathrm{rep}(j)},
 \qquad \mathcal C K_0=0,

$$

where $K_0$ has 61980 independent columns and $\|K_0\|_\infty=419$.

The equation $G\widehat V=0$ is equivalent to 19775 independent linear equations $Eg=0$: all 50 equations on each free row, followed by the upper-triangular pivot equations. Independence follows by solving uniquely for $G_{\mathrm{free,piv}}$ and $G_{\mathrm{piv,piv}}$ given the arbitrary symmetric free block. Put

$$

 M=EK_0\in\mathbb R^{19775\times61980},\qquad
 b(q)=\operatorname{coeff}(q\mathbb{I}-F).

$$

The missing assertion in an approximate SOS is $b(q_*)\in\mathcal C(\ker E)$. Small residuals do not prove it.

## 4. Complete exact compatibility

### 4.1. Physical functionals

For every family member, state-action and measurement first-variation functionals annihilate both $b(q_*)$ and every polynomial $(N^{\mathsf T}w)^*H(N^{\mathsf T}w)$ with symmetric $H$. Indeed its factors kill the state, so both its state action and its first expectation derivative vanish.

A degree-six Bob tree with 1370 vertices in total supplies all state rows needed for the selected coefficient classes. For Alice variations, the opposite-party pullback metrics are taken from the real span of legal complex spectator families. On the shallow core-plus-five-node space this span contains the identity, ten real off-diagonal auxiliary metrics, six imaginary auxiliary metrics, and the core--auxiliary occupation cross term. Nearby Gram matrices with real first row are realized by Hermitian Householder reflections. Hence the eighteen chosen metric directions are genuine linear combinations of physical functionals. Bob core-unitary variations at the real reference are physical directly.

The selected 1458 state rows and 192 measurement rows are independently certified to have rank 1650. All their entries are reconstructed as interval-enclosed rational functions of the original isolated root. For the proof it is unnecessary to assert that these physical rows exhaust all possible first variations.

### 4.2. Local algebraic relations

Exact formal coefficient enumeration gives 996 zero rows of $M$, six 39-row blocks of rank at most ten, and four 275-row blocks. The local row supports of $ER$ avoid every Bell coefficient class, including the identity. Thus every local left relation pairs to zero with $b(q)$ for every $q$.

The crucial rank bound for a 275-row block has a short algebraic proof. In the five-vector frame $X=S[k,b_1k,\ldots,b_4k]$, write $M_a=X^{-1}a_aX$ and $v_a=M_ae_0$. Then

$$

 M_a^2=I,\qquad M_1e_0=M_2e_0=-e_0,
 \qquad \operatorname{rank}(M_1-I)=\operatorname{rank}(M_2-I)=3.

$$

Take six symmetric $5\times5$ parameter matrices $V,U_1,\ldots,U_5$. Define

$$
\begin{aligned}
 L_a&=U_av_a+M_a^{\mathsf T}U_ae_0-Ve_0-M_a^{\mathsf T}Vv_a,\\
 Z_a&=U_ae_0-Vv_a,\\
 Y_{ab}&=U_av_b+M_a^{\mathsf T}U_be_0-M_a^{\mathsf T}Vv_b\quad(a\ne b).
\end{aligned}
$$

The 275 components consist of the columns of $V$, the columns of the five $U_a$, the five vectors $Z_a$, and the twenty vectors $Y_{ab}$. This parameterization is injective because it explicitly contains all columns of $U_a,V$.

An exact noncommutative bilinear expansion of each of the 270 distinct column patterns gives zero or a signed scalar component of $L_a$. Thus $L_a=0$ gives a left relation. There are 90 parameters. For $a=1,2$,

$$

 L_a=(M_a^{\mathsf T}-I)(U_a+V)e_0,

$$

so each contributes at most three independent constraints. The other three contribute at most five each. Therefore the constraint rank is at most 21 and the block has at least $90-21=69$ independent relations. Its rank is at most 206. This calculation requires no common metric and no numerical zero test. The interval construction also certifies a 21-row constraint minor at the actual root.

### 4.3. Matching ranks

From the local relations select 43 zero-row relations, five relations from the rank-ten blocks, and 96 relations from the four rank-206 blocks. Together with the 1650 physical rows these give 1794 coefficient functionals. Their joint independence is checked on a square minor at the original root, with exact directed intervals and an exact integer inverse-defect test. Each corresponding action-space row $\gamma$ satisfies

$$

 \gamma E=\lambda\mathcal C,\qquad \gamma M=0,\qquad \lambda b(q_*)=0.

$$

Consequently $\operatorname{rank} M\le19775-1794=17981$.

A separately selected minor $B$ of $M$ has order 17981. Exact integer verification, including all rows, and the separately certified root perturbation give

$$

 \|I-R_BB\|_\infty<4.357\times10^{-6}<1,
 \qquad \|B^{-1}\|_\infty<4034770.

$$

The dyadic inverse proposal is regenerated during replay; its numerical origin is irrelevant after this exact test. Hence $\operatorname{rank} M=17981$, and the 1794 compatible functionals form its complete left kernel. This is the step that upgrades approximate coefficient agreement to an exact solvability statement.

## 5. Positive correction at the same value

An untrusted numerical proposal is rounded to a rational Gram matrix $G_0$ with denominator $2^{200}$. The independent reference verifier proves

$$

 H_0:=(G_0)_{\mathrm{free,free}}>\eta I,
 \qquad \eta=2^{-36},

$$

by an exact congruence test; its defect is below $9.737\times10^{-9}$. Let $g_0$ be its coordinate vector and set

$$

 g_a(q)=g_0+R\bigl(b(q)-\mathcal Cg_0\bigr).

$$

Exact class summation gives $\mathcal Cg_a(q)=b(q)$. Root interval arithmetic proves the conservative bounds

$$

 \|g_a(q_*)-g_0\|_\infty<6.224\times10^{-60},\qquad
 \|Eg_a(q_*)\|_\infty<1.612\times10^{-49}.

$$

Let $I,J$ denote the row and column sets of $B=M[I,J]$. Define the exact algebraic correction

$$

 z=-B^{-1}(Eg_a(q_*))_I,\qquad
 g_*=g_a(q_*)+(K_0)_Jz.

$$

Complete compatibility implies $Eg_*=0$ on *all* 19775 rows, while $\mathcal Cg_*=b(q_*)$. The free block changes by less than

$$

 370\left(6.224\times10^{-60}
 +419\cdot4034770\cdot1.612\times10^{-49}\right)
 <1.009\times10^{-37}<\eta.

$$

Thus $H_*=(G_*)_{\mathrm{free,free}}$ is strictly positive. Since $Eg_*=0$,

$$

 G_*=NH_*N^{\mathsf T},\qquad
 \boxed{q_*\mathbb{I}-F=(N^{\mathsf T}w)^*H_*(N^{\mathsf T}w),\quad H_*>0.}

$$

These formulas, the exact root, the selected indices, and the rational input matrices completely specify the final Gram certificate without printing a huge inverse in decimal form.

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

For completeness, the final positive Gram identity gives
$Q_{\mathrm{com}}\le q_*$, while the five-dimensional construction gives
$Q_{\mathrm{fin}}\ge q_*$. The spatial supremum lies between them. For binary
effects, use the local reflection dilation

$$
\begin{pmatrix}2E-I&2\sqrt{E(I-E)}\\
2\sqrt{E(I-E)}&I-2E\end{pmatrix}.
$$

A common local ancilla accommodates every setting; the parties use separate
ancillas. Functional calculus preserves cross-party commutation, and
compression preserves all marginal and cross-party probabilities. Thus the
same unrestricted bound also covers arbitrary binary effects.
