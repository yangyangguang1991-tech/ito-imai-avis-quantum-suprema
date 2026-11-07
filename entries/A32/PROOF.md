# Exact quantum supremum of A32

The complete probability table is in **definition.json**. With index zero denoting
the identity, its Bell operator is

$$F=\sum_{i=0}^{m}\sum_{j=0}^{n} C_{ij}P_iQ_j,\qquad P_0=Q_0=I.$$

Thus the definition retains the constant, all marginal coefficients and every
joint coefficient. The local certificate stores the identical table in the sole
row of **catalogue.json**. Both the global checker and the independent physical
checker actually read that row. Substitution of $P_i=(I+A_i)/2$ and
$Q_j=(I+B_j)/2$ gives its **four_times_reflection_matrix**, representing exactly
$4F$. The public launcher checks both complete coefficient matrices.

## Exact value and attaining strategy

The exact value is $\beta=f(x_*)$. Its 20 real coordinates are the unique
zero of the full rational gradient of $f$ in

$$X=\prod_{j=1}^{20}[c_j-\rho,c_j+\rho].$$

The fields **center** and **radius** in **A32_complex_certificate.json** give the exact rational
$c_j$ and $\rho$. The same file fixes all chart signs, constant-reflection
indicators when present, the word basis and pivot choices. A decimal display or
the box centre does not replace $x_*$. The exact number is this isolated root
evaluation, whether or not a shorter radical expression is available.

The physical state is

$$|\psi(t)\rangle=\frac{|00\rangle+t|11\rangle}{\sqrt{1+t^2}},
\qquad t=(x_*)_0.$$

Settings are ordered with Alice first and Bob second. For a real active setting,
use

$$R_\varepsilon(u)=\frac{\varepsilon}{1+u^2}
\begin{pmatrix}1-u^2&2u\\2u&u^2-1\end{pmatrix}.$$

For a complex active setting put

$$n_\varepsilon(u,v)=
\frac{\varepsilon}{1+u^2+v^2}(2u,2v,1-u^2-v^2),$$

$$R=n_x\sigma_x+n_y\sigma_y+n_z\sigma_z,\qquad
\sigma_x=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
\sigma_y=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
\sigma_z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.$$

This entry uses the **complex** chart. For a real chart, the coordinates after
$t$ are one $u$ per active setting. For a complex chart, the first active setting
has $v=0$ and one coordinate $u$, while every remaining active setting has
successive coordinates $(u,v)$. The first-setting convention fixes the phase
freedom. A nonzero **reflection_types** entry, when present, is the constant
reflection $+I$ or $-I$; a zero is active. If that field is absent, all settings
are active. The field **signs** gives $\varepsilon=\pm1$ in the original setting
order. Orbit labels affect the construction of common annihilators, not the
dimension or validity of this physical witness.

The selected family modules implement these rational formulas. Each reflection
is Hermitian and squares to the identity, so $(I+R)/2$ is a projection. The state
is normalized. The rational function $f$ is the expectation of the original
complete probability polynomial in these matrices and this state. Therefore
$f(x_*)$ is a legal score attained with two-dimensional local spaces.

The root checker in **verify_sparse.py** constructs the map
$T(x)=x-R\nabla f(x)$ using the stored rational root preconditioner $R$.
It proves a derivative norm strictly below one on $X$ and a strictly interior
Krawczyk inclusion. The same derivative bound implies that $R$ is nonsingular.
The contraction theorem consequently proves existence and uniqueness of the
specified stationary root. **independent_complex.py** independently reconstructs the
literal probability expression and a physical-matrix root test. These arguments
do not infer a root from numerical convergence of an optimizer.

## Universal coefficient identity

Let $w$ be the declared word column in the universal reflection algebra

$$A_i^2=B_j^2=I,\qquad[A_i,B_j]=0.$$

Word reduction cancels adjacent equal letters within a party and commutes Alice
letters past Bob letters. It never commutes different settings of one party.
For this real symmetric Gram construction, grouping a word with its adjoint
preserves all coefficients of the Hermitian polynomial.

Evaluate $w$ on the physical state. The pivot submatrix selected in the
certificate is invertible throughout $X$, as established by interval inversion.
Solving against those pivots defines a rational coefficient matrix $N(x)$ and
annihilators $r(x)=N(x)^T w$ such that
$r_i(x)|\psi(x)\rangle=0$. For an orbit chart, the word-action rows concatenate
the Bell-preserving relabelings specified in **orbits**. The checker verifies
each relabeling on the complete reflection coefficient matrix. It does not
assume that arbitrary competing measurements possess this symmetry.

Let $\mathcal A(x)$ be the linear map from independent real symmetric Gram
coordinates to the coefficient vector of $r(x)^\dagger G r(x)$. Each
off-diagonal coordinate includes both symmetric matrix entries. Let $J(x)$
contain the value and first-derivative moment columns, separately for each orbit
when applicable. Let $b(x)$ be the complete coefficient vector of $f(x)I-F$.

Freeze the annihilator coefficients at $x$ and vary the physical state and
measurements with another parameter $y$. Every squared norm and polarized
cross term vanishes together with its first derivative at $y=x$. Thus

$$\mathcal A(x)^T J(x)=0,\qquad
J(x)^T b(x)=(0,-\nabla f(x)),$$

with the value/gradient block repeated for each Bell-preserving orbit.
The differentiation here acts only on the physical moments, not on the frozen
annihilator coefficients. These are rational identities. At $x_*$, stationarity
therefore gives $J(x_*)^Tb(x_*)=0$ exactly.

The certificate proves invertibility of

$$K(x)=\mathcal A(x)\mathcal A(x)^T+J(x)J(x)^T$$

on the required box. The two summand ranges are orthogonal. Their sum spans the
coefficient space because $K$ is invertible, giving

$$\operatorname{range}\mathcal A=\ker J^T.$$

Let $G_0$ be the stored rational Gram seed and, at $x_*$, define

$$e=b-\mathcal A\operatorname{vec}(G_0),\qquad
\delta=\mathcal A^TK^{-1}e,\qquad
G_*=G_0+\operatorname{unvec}(\delta).$$

The compatibility identities place $e$ in $\operatorname{range}\mathcal A$.
On this range $K$ acts as $\mathcal A\mathcal A^T$, so
$\mathcal A\delta=e$ exactly. Hence

$$\mathcal A\operatorname{vec}(G_*)=b.$$

This finite rational-function expression evaluated at the isolated algebraic
root is the definition of the corrected Gram. No nonzero coefficient residual
is discarded and no numerical matrix is silently substituted for $G_*$.

## Positivity and unrestricted upper bound

The checker proves $G_0-\eta I\succ0$ by exact Bareiss leading minors; the
positive rational $\eta$ is **Gram_margin**. The coefficient map, residual,
normal inverse and correction are bounded using outward interval arithmetic.
The final strictly rational comparison proves

$$\|\operatorname{unvec}(\delta)\|_{\mathrm{op}}<\eta.$$

It follows that $G_*\succ0$ and

$$\beta I-F=r(x_*)^\dagger G_*r(x_*)\succeq0.$$

The normal-system multiplication uses binary64 CPU products only inside
an explicit forward-error enclosure. **normal_roundoff.py** uses rational bounds
$\gamma_n=nu/(1-nu)$ with $u=2^{-52}$, checks the exact dyadic input scales and
sizes, and inflates the computed residual. The final inverse estimate uses a
fixed rational cap. Its acceptance criterion does not treat an uninflated
floating residual or eigenvalue as a rigorous bound.

The identity uses only the displayed universal reflection relations. It is
therefore valid on arbitrary Hilbert spaces with commuting observers. Private
ancilla dilations of the two parties cover binary effects while preserving all
constant, marginal and cross-party moments. Together with the two-qubit
attainment above, this proves

$$Q_{\mathrm{fin}}(A_{32})=
Q_{\mathrm{sp}}(A_{32})=
Q_{\mathrm{com}}(A_{32})=\beta.$$

## Reproduction

From the catalogue root run:

    python verify.py 32

The public launcher prepares the bundled arithmetic libraries and runs this
entry's **check.py**, which invokes both **verify_sparse.py** and **independent_complex.py**.
The supported release system is Windows x86-64 with CPython 3.12.
All mathematical inputs are included. No optimizer, network fetch, or external
catalogue is required.

