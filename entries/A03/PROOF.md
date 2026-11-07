# Exact quantum supremum of A3

The complete probability table **definition.json** defines
$$F=\sum_{i=0}^m\sum_{j=0}^n C_{ij}P_iQ_j,\qquad P_0=Q_0=I.$$
All constant, marginal and joint coefficients are retained. Throughout, binary
projections correspond to reflections by $P_i=(I+A_i)/2$, $Q_j=(I+B_j)/2$.
The field **four_times_reflection_matrix** is the coefficient matrix of $4F$.

## Exact path characterization

The entry uses projections with outcome 1. Its displayed table is equation (27) in Coladangelo's normalization. In the original local-bound-zero normalization the common exact quantum supremum is the real constant $q_*$ defined below. The proof applies to arbitrary mutually commuting Alice and Bob algebras. A finite-dimensional realization can approach this value. The existence of a normal infinite-dimensional strategy attaining it, and its strict nonattainment in finite dimension, are theorems of Coladangelo. We use that external theorem only for the dimension and exact attainment assertions. The upper bound and the approaching family are proved here.

## An explicit Jacobi variational definition

Put $d(u,v)=uv+(u-v)/2-1$ and $a(v)=\sqrt{1-v^2}/2$. For an integer $m\ge1$ choose real labels $c_0,\ldots,c_m$ in $[-1,1]$, with $c_0,c_m\in\{-1,1\}$. The real symmetric tridiagonal matrix $J$ has diagonal entries $d(c_{j-1},c_j)$ and off-diagonal entries $a(c_j)$ for $1\le j<m$. Define $q_* = \sup_{m,c}\lambda_{\max}(J)$. This is a scalar path problem with one parameter per internal edge. Its value is finite by the row-sum bound.

## The unrestricted upper bound

For the first two projections on each side set $Z=P_1+P_2-I, X=P_2-P_1$, and for the third set $W=2P_3-I$, using the corresponding three Bob projections on his side. Then $XZ=-ZX, X^2=I-Z^2, W^2=I$. Direct expansion of the displayed table gives

$$

 F=d(Z_A,Z_B)+\tfrac12 X_A W_B+\tfrac12 W_A X_B .

$$

Here is a construction of a bounded Borel scalar majorant, following the Riccati argument of Coladangelo. Fix any $q>q_*$. For any finite prefix starting at $+1$ and ending at $v\in[-1,1]$, form the Jacobi matrix of that prefix. Appending a terminal endpoint embeds it as a principal submatrix of an admissible path. Thus $qI-J\succeq(q-q_*)I$. Its last elimination pivot $p$ is at least $q-q_*$, by minimizing the quadratic form with last coordinate fixed to 1. Along an extension by one label the new pivot is $q-d(u,v)-a(u)^2/p$, where $u$ was the old last label. Define $P(v)$ to be the infimum of the last pivots from all nonempty prefixes ending at $v$. The one-edge prefix bounds it above by $q-d(1,v)$; the preceding positive lower bound holds uniformly. For each fixed list of earlier labels the last pivot depends continuously on $v$. The infimum is upper semicontinuous and hence Borel.

Writing $U(v)=a(v)^2/P(v)$, extending a prefix approaching the infimum at $u$ gives $U(u)+P(v)\le q-d(u,v)$. The reflection identity $d(-v,-u)=d(u,v)$ gives a second such inequality with the variables reversed. Set $H(u)=(U(u)+P(-u))/2$. Adding the inequalities gives $H(u)+H(-v)\le q-d(u,v)$. The arithmetic–geometric mean inequality on the four factors gives

$$

 H(u)H(-u)\ge \tfrac14\left(\sqrt{U(u)P(u)}+\sqrt{U(-u)P(-u)}\right)^2=a(u)^2.

$$

Both $H$ and its reciprocal are bounded.

Let $S=X_AW_B$. It anticommutes with $Z_A$, intertwines every bounded Borel function $f(Z_A)$ with $f(-Z_A)$, and $S^2=I-Z_A^2$. The self-adjoint operator $H(Z_A)^{-1/2} S H(Z_A)^{-1/2}/2$ therefore has square at most $I$. Hence $S/2\preceq H(Z_A)$. The same argument gives $W_A X_B/2\preceq H(-Z_B)$. The joint functional calculus of the commuting operators $Z_A,Z_B$ now bounds $F\preceq qI$. Let $q\downarrow q_*$. Binary effects can be dilated: for an effect $T$, the block projection with diagonal blocks $T,I-T$ and off-diagonal blocks $\sqrt{T(I-T)}$ compresses to $T$. Dilate one party at a time on separate ancillary spaces, keeping the other party's operators diagonal; the original correlations and cross-party commutation are preserved.

## Constructive lower bound

For a path use the basis indexed by $j=1,\ldots,m$. For odd $j$ put $(Z_A(j),Z_B(j))=(c_{j-1},c_j)$; for even $j$ put $(-c_j,-c_{j-1})$. On edges $j,j+1$, use the symmetric exchange with coefficient $\sqrt{1-c_j^2}$ in $X_A$ for even $j$ and $X_B$ for odd $j$; set the unused entries to zero. $W_A$ exchanges the odd edges and $W_B$ exchanges the even edges, with identity on unpaired sites. On both sides take projections $(I+Z-X)/2,(I+Z+X)/2,(I+W)/2$. Each is a projection by the two displayed relations. For any nonzero real vector $v$, the normalized state is $\sum_j v_j|j,j\rangle/\|v\|$. Substitution into the literal table gives $v^TJv/v^Tv$: the diagonal terms give $d(c_{j-1},c_j)$, and each edge gives $a(c_j)$. Choosing a top eigenvector establishes the reverse inequality.

For a wholly explicit approximating sequence enumerate paths with rational half-angle parameters, $c=(1-z^2)/(1+z^2),\ s=2z/(1+z^2)$, $z\ge0$ rational, also allowing $c=-1,s=0$. Enumerate nonzero rational trial vectors and all lengths by increasing combined size. Retain the largest score so far. Density, continuity at each fixed length and the Rayleigh principle prove monotone convergence to $q_*$. The accompanying program produces exact matrices and checks the score by tensor contraction. Its finite tests illustrate the family; the preceding argument proves convergence.

[Detailed references for exact-value theorems](REFERENCES.md).

The native path table equals the literal A3 table with no relabeling. Both **A3.json** and **path/definition.json** are checked against that table.

## Reproduction and scope

Run **python verify.py 3** from the catalogue root. The launcher prepares the
included arithmetic libraries and executes the complete selected proof chain.
The supported environment is Windows x86-64 with CPython 3.12.
The selected stages are **verify_transfer.py**, **path/verify.py**, **path/sequence_example.py**.
All coefficient tables, algebraic defining data and certificate inputs are
included in this entry. No optimizer, network access or external catalogue is
needed. The upper proof uses the universal reflection relations,
namely $A_i^2=B_j^2=I$ and $[A_i,B_j]=0$. Separate local ancilla dilations
cover binary effects without changing the relevant moments. Hence the upper
bound holds in arbitrary dimension and in the commuting model.
