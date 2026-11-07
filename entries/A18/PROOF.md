# Exact quantum supremum of A18

The complete probability table **definition.json** defines
$$F=\sum_{i=0}^m\sum_{j=0}^n C_{ij}P_iQ_j,\qquad P_0=Q_0=I.$$
All constant, marginal and joint coefficients are retained. Throughout, binary
projections correspond to reflections by $P_i=(I+A_i)/2$, $Q_j=(I+B_j)/2$.
The field **four_times_reflection_matrix** is the coefficient matrix of $4F$.

## Exact algebraic value

In **A18_GLOBAL_EXACT_CERTIFICATE.json**, the integer polynomial in **root** and its rational
**center** plus or minus **radius** specify one real algebraic number
$\theta$. The exact value $\beta$ is **value**, evaluated in that field.
Its coefficient list is in **ascending** powers of $\theta$.
The root interval selects the embedding; a decimal approximation does not
define the value. The field and value polynomial identities are checked exactly.

## Exact universal upper identity

The certificate's **words** are words in the universal reflection algebra.
Decode **N_sparse** into $N$ in the specified real number field. Decode the
rational symmetric seed $G_0=\mathtt{Gram\_integer}/\mathtt{Gram\_denominator}$
and the exact algebraic entries **corrections** into a symmetric matrix $E$.
The final Gram matrix is explicitly $G=G_0+E$, not a floating approximation.
For $r=N^Tw$, the certificate identity is
$$\beta I-F=\frac1{|\mathcal G|}\sum_{g\in\mathcal G}g(r)^\dagger Gg(r).$$
The list **orbits** gives all signed setting relabelings in this average.
Each preserves the complete Bell coefficient matrix, as checked exactly.
Thus every summand is positive when $G\succeq0$; no symmetry is imposed on
arbitrary competing measurements or states.

The primary checker expands all invariant coefficient classes. Its independent
directed-word check restores the individual coefficients before taking the
orbit average, so there is no discarded high-order remainder. Multiplication
is exact in the polynomial quotient, and the specified real root interval
fixes the embedding. The field root is isolated by an endpoint sign change
and a nonvanishing derivative enclosure.

For positivity, exact Bareiss elimination proves $G_0-\eta I\succ0$ with
the positive rational **Gram_margin** $\eta$. Outward rational intervals
bound the absolute row sums of $E$ strictly below $\eta$. Since $E$ is symmetric,
$\|E\|_{\rm op}\le\max_i\sum_j|E_{ij}|<\eta$, so $G\succ0$.
The resulting exact operator identity proves $F\preceq\beta I$ in arbitrary
dimension. The physical strategy below attains that same field element.

## Explicit physical strategy

Write $X=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$,
$Y=\left(\begin{smallmatrix}0&-i\\i&0\end{smallmatrix}\right)$ and
$Z=\operatorname{diag}(1,-1)$. Every projection is $(I+R)/2$ for the
reflection $R$ below. When $h^2+k^2=1$, $h\ge0$, $|k|\le1$, use
$$|\psi\rangle=\sqrt{(1+k)/2}|00\rangle+
\sqrt{(1-k)/2}|11\rangle.$$
Its density matrix is
$[I\otimes I+k(Z\otimes I+I\otimes Z)+Z\otimes Z+
h(X\otimes X-Y\otimes Y)]/4$.
All radicands and denominators in the following formulas are checked in the
same real embedding as the upper certificate.

Put $f=\theta/4$, $e^2=1-f^2$, $z=(4f^2+2f-1)(1-f)$,
$h^2=1-z^2/e^2$, and take $e,h>0$, $k=z/e$. Set
$$\alpha=\frac{4f^2-2f-1}{4f^2-1},\quad
\gamma=-(f+1)(4f^2-2f-1),$$
$$a=(2e^2-z)/(e\alpha),\quad b=h/\alpha,\quad
c=e/\gamma,\quad d=h(1+f)/\gamma.$$
Use
$$A=(aZ+bX,\ aZ-bX,\ -cZ-dX,\ cZ-dX),$$
$$B=(-I,\ -eZ-fX,\ eZ-fX,\ -X,\ -X).$$
The checked identities give $a^2+b^2=c^2+d^2=e^2+f^2=1$.
The complete original probability polynomial evaluates to
$-3/2+(e-a)k/2+ae+ce/2+h(b+df+d)/2=\beta$.
In particular $\beta=-1/2+5\theta/4-7\theta^2/16$, and
$16\beta^3+83\beta^2+62\beta-37=0$; it is the unique positive root.

## Reproduction and scope

Run **python verify.py 18** from the catalogue root. The launcher prepares the
included arithmetic libraries and executes the complete selected proof chain.
The supported environment is Windows x86-64 with CPython 3.12.
The selected stages are **verify18.py**, **independent18.py**.
All coefficient tables, algebraic defining data and certificate inputs are
included in this entry. No optimizer, network access or external catalogue is
needed. The upper proof uses the universal reflection relations,
namely $A_i^2=B_j^2=I$ and $[A_i,B_j]=0$. Separate local ancilla dilations
cover binary effects without changing the relevant moments. Hence the upper
bound holds in arbitrary dimension and in the commuting model.
