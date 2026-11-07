# A80: exact quantum supremum

## 1. Statement and normalization

Let $P_0=Q_0=I$, and let $P_1,\dots,P_5$ and $Q_1,\dots,Q_5$ be projections with $[P_i,Q_j]=0$. We freeze the full probability expression

$$
\qquad\text{(E1)}
 F=\sum_{i,j=0}^{5}c_{ij}P_iQ_j,\qquad
(c_{ij})=\begin{pmatrix}
0&0&-1&-1&0&-1\\
0&-1&-1&1&-1&0\\
-1&-1&-1&0&1&1\\
-1&0&1&1&0&1\\
0&-1&1&0&0&0\\
-1&1&0&1&0&0
\end{pmatrix}.

$$

All marginal terms are retained. The convention is maximization, with classical bound zero. Exact enumeration of the $2^{10}=1024$ deterministic assignments gives $79$ assignments attaining that bound.

The symbols $Q_{\mathrm{fin}}$, $Q_{\mathrm{sp}}$ and $Q_{\mathrm{com}}$ denote respectively the supremum over finite-dimensional tensor-product strategies, spatial tensor-product strategies, and commuting-operator strategies. The inequalities between these models are sufficient for the argument; no general equality of the models is assumed.

**Theorem 1.**

Let $x_*$ be the unique root in the supplied rational isolating box of the forty-variable stationarity system defined in Section 2, and put $q_*=f(x_*)$. Then

$$

 Q_{\mathrm{fin}}(A_{80})=Q_{\mathrm{sp}}(A_{80})=Q_{\mathrm{com}}(A_{80})=q_*.

$$

The value is attained by a pure state and projective measurements on $\mathbb C^4\otimes\mathbb C^4$. Its decimal display begins

$$

 q_*=0.376986318533610806225685760913708107341382328264795045\ldots.

$$

The exact definition is the isolated algebraic root construction, not the displayed decimal or a fitted radical.

## 2. Exact value and attaining strategy

The certificate contains the ordered graph charts, rational center, rational isolating radius, and an inverse-Hessian proposal. Write

$$

 S=\operatorname{diag}(1,x_1,x_2,x_3),\qquad
 |\psi\rangle=\frac{\operatorname{vec}(S)}{\sqrt{\operatorname{Tr}(S^2)}}.

$$

For each measurement, use a real Grassmann graph $X=\Pi^{\mathsf T}[I_r;U]$ and set

$$
\qquad\text{(E2)}
 P=X(X^{\mathsf T}X)^{-1}X^{\mathsf T}.

$$

Here $\Pi$ is the explicitly supplied row permutation. The ten ranks are

$$

 (1,2,2,1,2)\quad\hbox{and}\quad(2,1,2,2,2).

$$

The three Schmidt ratios and all graph entries give forty variables. Define the rational function

$$
\qquad\text{(E3)}
 f(x)=\frac{\sum_{i,j=0}^{5}c_{ij}\operatorname{Tr}(SP_iSQ_j^{\mathsf T})}{\operatorname{Tr}(S^2)}.

$$

The equations are $\partial_k f(x)=0$, $1\leq k\leq40$. The root is isolated in a box of radius $10^{-180}$ about the supplied rational center. Outward integer intervals prove strict Krawczyk inclusion and contraction. All projector denominators are nonzero, and the Schmidt coefficients are positive and pairwise distinct in the box.

Consequently $x_*$ exists uniquely in this box. Clearing the nonvanishing denominators gives a nonsingular isolated algebraic system, so this is an exact algebraic specification. Formula (E2) proves projection identities without treating small numerical residuals as zero. The identity

$$

 \langle\operatorname{vec}(S),P\otimes Q\,\operatorname{vec}(S)\rangle
 =\operatorname{Tr}(SPSQ^{\mathsf T})

$$

proves that the physical score is exactly (E3). A separate verifier reconstructs the literal $6\times6$ probability expression and exports the state and all ten measurement matrices, together with certified entry enclosures.

The complete Schmidt/Grassmann chart also implies full real state and measurement stationarity. Distinct Schmidt coefficients permit all real state variations modulo local orthogonal variations. Since the Bell operator and the response matrices are real, the resulting eigenvector and commutator identities also give stationarity under complex variations. In particular,

$$
\qquad\text{(E4)}
 F\psi=q_*\psi,\qquad [P_i,K_i^A]=[Q_j,K_j^B]=0.

$$

Stationarity alone is not used as a global-optimality assertion.

## 3. An enlarged family of stationary strategies

The fourth measurement is special on each side. Let $h_A,h_B$ be its normalized response-kernel vectors, and set $N_A=h_Ah_A^*$ and $N_B=h_Bh_B^*$. The exact response-kernel construction proves
\begin{gather}\qquad\text{(E5)}
 K_4^Ah_A=K_4^Bh_B=0,\qquad P_4h_A=Q_4h_B=0,\\
 P_1Sh_B=P_2Sh_B=0,\qquad Q_1Sh_A=Q_2Sh_A=0.\nonumber
\end{gather}
The last identities follow from signed maximal-minor cofactors of the three-column frame matrices. They are algebraic identities, not interval-zero conclusions.

For one party write $R_i=2P_i-I$, $h=h_A$, $N=hh^*$ and $C_s=R_4+N$; the other party is analogous. Then $C_sh=0$ and $C_s^2=I-N$. Choose any auxiliary Hilbert space, a unit vector $e$, and a self-adjoint operator $D$ such that $De=0$ and $D^2=I-ee^*$. For $-1\leq t\leq1$ define

$$
\qquad\text{(E6)}
 R_4(t)=\begin{pmatrix}
 C_s+tN&\sqrt{1-t^2}\,he^*\\
 \sqrt{1-t^2}\,eh^*&D-tee^*
 \end{pmatrix}.

$$

All ordinary reflections are $R_i\oplus H_i$, with arbitrary auxiliary reflections $H_i$. Direct multiplication shows $R_4(t)^*=R_4(t)$ and $R_4(t)^2=I$. The special projector has core compression $P_4+(1+t)N/2$. The two parties may choose their auxiliary data and parameters independently.

**Lemma 2.**

Every strategy in this family has score $q_*$, satisfies $F\psi=q_*\psi$, and is stationary under every bounded local measurement variation, including complex variations leaving the displayed family.

**Proof.**

The frozen expression has the exact decomposition

$$

 F=F_0+P_4(Q_2-Q_1)+(P_2-P_1)Q_4,

$$

where $F_0$ contains neither special measurement. In particular $c_{44}=0$. The change in a special projector, applied to the core, has core and auxiliary rows proportional to $h^*$. Equations (E5) therefore make both changes of Bell action vanish. There is no product of the two special changes.

Changing Bob's special compression changes only Alice's responses for settings $1,2$, by opposite scalar multiples of $SN_BS$. Both $P_1$ and $P_2$ annihilate its range. The special response is unchanged and annihilates $h_A$, so it commutes with every block of (E6). All responses are core-supported; arbitrary auxiliary blocks commute with their zero auxiliary part. The same argument applies to Bob. Thus all response commutators vanish, which proves the first-variation claim.

∎

## 4. Finite word and coefficient spaces

Use the $676$ reduced words with at most two Alice and two Bob letters. Only adjacent equal same-party reflections cancel, and only cross-party letters commute. The common-kernel theorem forces sixteen Gram rows to vanish. The retained $660$ words split under the exact signed party symmetry into character dimensions $341$ and $319$. Their action ranks are $35$ and $30$, leaving kernel dimensions

$$

 341-35=306,\qquad319-30=289.

$$

The symmetry is $A_1\leftrightarrow B_2$, $A_2\leftrightarrow B_1$, $A_3\leftrightarrow B_3$, $A_4\leftrightarrow-B_4$, $A_5\leftrightarrow B_5$. Its relation to the isolated strategy is proved by exact root uniqueness and the response-kernel identities.

Symmetric Gram coordinates comprise diagonal entries and twice the upper off-diagonal entries. There are $109351$ coordinates and $43683$ invariant Hermitian coefficient coordinates. Let $\mathcal C$ be the integer coefficient map. Explicit integer matrices $R_4,K_4$ obey

$$
\qquad\text{(E7)}
 \mathcal C R_4=4I,\qquad\mathcal C K_4=0,

$$

and a designated square submatrix of $K_4$ is $4I$ of order $65668$. Therefore $\mathcal C$ is surjective and $K_4/4$ is a basis of its complete kernel. These identities are checked by an independent literal word expansion.

Normalize each character action to $T=[I;T_F]$ in pivot/free order. The exact entries are rational functions of $x_*$. The map $E$ consists of the free rows of $GT$ and the upper triangle of its pivot rows. It has $20475$ independent equations and

$$
\qquad\text{(E8)}
 E(g)=0\iff GT=0\iff G=NHN^{\mathsf T},\qquad
 N=\begin{pmatrix}-T_F^{\mathsf T}\\I\end{pmatrix},\quad H=G_{FF}.

$$

Indeed the free equations determine $G_{FP}=-G_{FF}T_F$; the remaining pivot block is symmetric, so its upper triangle suffices. The same parametrization proves the independence of the equations.

Put $M=EK_4/4$. Rank-nullity and (E7) imply

$$
\qquad\text{(E9)}
 \dim\operatorname{coker}(\mathcal C|_{\ker E})=20475-\operatorname{rank} M.

$$

This formula identifies the precise linear obstruction to a Gram representation at the prescribed value.

## 5. The 2045 physical compatibility conditions

The degree-four reference tree has local dimension $89$. Its state-action span has exact dimension $1865$. The enlarged family still factors through this tree: map its root to $R_4(t)h$ and each ordinary descendant to the corresponding word applied to that vector. The map is generally nonisometric. This preserves the $595$-dimensional common kernel for words of degree at most two on each side.

Every coefficient polynomial from (E8) is a linear combination of $n_i^*n_j$, where each $n_i$ kills the reference state throughout the family. Its state action is zero, and its *expectation* derivative under any measurement variation is zero by the product rule. The operator derivative itself need not vanish. Lemma 2 proves that the same functionals kill $q_*I-F$.

The degree-two opposite-action metrics span eighteen real directions: twelve real symmetric directions and six imaginary antisymmetric directions. The additional real direction, absent when $t$ is fixed to zero, is

$$
\qquad\text{(E10)}
 \begin{pmatrix}0&H\\H^*&0\end{pmatrix},\qquad
 H=[h,R_1h,R_2h,R_3h,R_5h].

$$

It is obtained from the difference of the physical metrics at $t$ and $-t$. The raw rational tree coordinates eliminate square roots from its certificate entries.

For completeness, the dimension upper bound uses three reductions. First, every word derivative pulls back through the nonisometric tree map by the skew-Hermitian generator $L^*KL$. Second, duplication of an entire representation as an auxiliary summand shows that every core/auxiliary variation is a state-action functional modulo the common kernel. Third, special-reflection identities reduce the special core variation to two directions per real or imaginary parity. The four ordinary settings contribute $3+4+4+4$ directions. Common core gauge removes six real directions or nine imaginary directions; the ordinary core commutant is certified to be scalar. Thus at most eleven directions remain per real metric and eight per imaginary metric:

$$
\qquad\text{(E11)}
 \dim\mathcal N\leq1865+12\cdot11+6\cdot8=2045.

$$

The accompanying proof notes give the duplication and pullback arguments in full, including arbitrary auxiliary dimensions.

An explicit $2045$-square minor proves the matching lower bound. Every entry is reconstructed in outward dyadic arithmetic over a fresh isolated root. An integer inverse-defect certificate yields

$$

 \|I-RJ\|_\infty\leq
 \frac{204140278454848167493}{1208925819614629174706176}<1.

$$

Therefore the physical compatibility space has exactly dimension $2045$. In particular, it gives $2045$ independent linear functionals killing both $\mathcal C(\ker E)$ and the target $b(q_*)$. Only this certified lower bound on the number of independent physical normals is needed for the closure: the complementary minor in the next section supplies the matching algebraic bound independently of (E11).

## 6. Certification of the complementary minor

Choose the supplied $18430$ rows and columns of $M$. Let $B$ be this exact root matrix and $B_0$ its stored binary64 proposal. The verifier freshly reconstructs the character actions from the root and certifies their error relative to the stored actions. It then recomputes the sparse product with $K_4$ using integer digits, accounting for every omitted or rounded entry. The resulting full-matrix bound is

$$

 \|M-M_0\|_\infty\leq
 \frac{127320799779}{302231454903657293676544}
 <4.2127\times10^{-13}.

$$

Tighter rowwise bounds are retained for the actual inverse check.

A numerical block solve proposes an inverse, quantized to a dyadic matrix $R$. Signed base-$2^{18}$ digits reduce the products to exact integer sparse dot products. Each dot has at most $330$ terms and a proved absolute partial-sum bound below $2^{53}$; integer carry and row-sum bounds prevent machine overflow. This proves rational bounds

$$

 \|I-RB\|_\infty\leq d<1,\qquad \|R\|_\infty\leq r,

$$

including the root perturbation through the rowwise product $|R|\delta$. Hence

$$
\qquad\text{(E12)}
 B\text{ is invertible},\qquad\|B^{-1}\|_\infty\leq\frac{r}{1-d}.

$$

Numerical LU factors are only proposals. The acceptance calculation is exact rational arithmetic with explicitly bounded integer products.
In the completed computation,

$$

 d=\frac{866858734713305150242386603673}
 {2596148429267413814265248164610048}<0.000334,

$$

and the certified inverse bound is

$$

 \|B^{-1}\|_\infty\leq
 \frac{19200159285920799668049441082015410552832}
 {519056314106540101823001155601275}<36990513.

$$

The physical normals give $\operatorname{rank} M\leq18430$, and the complementary minor gives the reverse inequality. Equation (E9) now shows that the physical normals exhaust the entire algebraic coefficient obstruction. Since they kill $b(q_*)$,

$$
\qquad\text{(E13)}
 b(q_*)\in\mathcal C(\ker E).

$$

This is complete compatibility, before positivity is addressed.

## 7. Positive correction without changing the value

Choose a rational reference $g_0$ by rounding and character-projecting the supplied high-precision Gram proposal. No numerical residual is declared zero. Independent exact integer congruences prove the free-block margins

$$

 H_{0,+}\succeq2^{-30}I_{306},\qquad
 H_{0,-}\succeq2^{-31}I_{289}.

$$

Define a coefficient-exact affine reference

$$

 g_a=g_0+\frac{R_4}{4}\bigl(b(q_*)-\mathcal Cg_0\bigr).

$$

Then $\mathcal Cg_a=b(q_*)$ identically. Outward root intervals and exact integer calculations give

$$
\begin{gathered}
 \|g_a-g_0\|_\infty<4.8330\times10^{-45},\\
 \|Eg_a\|_\infty<3.7152\times10^{-45},\qquad
 \|K_4/4\|_\infty=6930.
\end{gathered}
$$

Let $I,J$ be the selected row and column indices of $B=M_{I,J}$. Set

$$

 t_J=-B^{-1}(Eg_a)_I,\qquad t_{J^c}=0,\qquad
 g_*=g_a+(K_4/4)t.

$$

By (E13), $-Eg_a$ lies in $\operatorname{im}M$. The selected columns span that image, and restriction to the selected rows is injective on it. Thus the correction solves *all* face equations, not just the selected rows. It also preserves the exact coefficient vector.

Each free-block operator perturbation is bounded by

$$
\qquad\text{(E14)}
 306\left(\|g_a-g_0\|_\infty+
 6930\|B^{-1}\|_\infty\|(Eg_a)_I\|_\infty\right).

$$

Substitution of the certified rational bounds gives a free-block operator correction strictly below

$$

 2.915\times10^{-31}<2^{-31}.

$$

The final checker performs this comparison with exact rational numbers. Hence both corrected free blocks are positive definite.

Combining the exact coefficients and (E8) gives

$$

 q_*I-F=n_+^*H_+n_++n_-^*H_-n_-,\qquad H_+\succ0,\quad H_-\succ0,

$$

with $306$ and $289$ kernel polynomials. All coefficients are exact rational functions of the isolated root; the inverse formula above defines the correction exactly. This identity holds in the universal reflection algebra and gives $Q_{\mathrm{com}}\leq q_*$. The four-dimensional strategy gives $Q_{\mathrm{fin}}\geq q_*$. Theorem 1 follows. Binary effects are covered by simultaneous local reflection dilations on separate auxiliary factors, preserving cross-party commutation.

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
