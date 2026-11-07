# Exact quantum supremum of A26

The complete probability table **definition.json** defines
$$F=\sum_{i=0}^m\sum_{j=0}^n C_{ij}P_iQ_j,\qquad P_0=Q_0=I.$$
All constant, marginal and joint coefficients are retained. Throughout, binary
projections correspond to reflections by $P_i=(I+A_i)/2$, $Q_j=(I+B_j)/2$.
The field **four_times_reflection_matrix** is the coefficient matrix of $4F$.

## Exact algebraic value

In **A26_GLOBAL_EXACT_CERTIFICATE.json**, the integer polynomial in **root** and its rational
**center** plus or minus **radius** specify one real algebraic number
$\theta$. The exact value $\beta$ is **value**, evaluated in that field.
Its coefficient list is in **descending** powers of $\theta$.
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

Put $m=\theta$, and let $h$ be the field polynomial
**field.h_coefficients_descending**. Define
$$u=\frac{4m+1}{2(4m^2-4m-1)},\quad
r=\frac{m}{4m^2-4m-1},\quad n=2(h(m-1)-1),$$
$$c=2\{h(1+1/(4m))+1\}n-1,\quad
w^2=\frac{1-r^2-4m^2(1-u^2)}{n^2-4m^2},\quad v^2=1-u^2-w^2.$$
Take $v,w>0$, $s=2mv$, $z=nw$ and $k=cw$.
The field checker proves all reflection norm identities and $h^2+k^2=1$.
Use
$$A=(uX-vY-wZ,\ rX-sY+zZ,\ -rX-sY+zZ,\ uX+vY+wZ,\ X),$$
$$B=(rX+sY-zZ,\ uX-vY-wZ,\ -rX+sY-zZ,\ uX+vY+wZ,\ X).$$
Direct expansion gives
$-2+w^2+wz-z^2+h\{u(r+1)+s^2+sv-v^2\}+kz=\beta$.
The exact irreducibility and value-polynomial calculation is supplied by
**verify_algebra26.py**. Its degree-13 value polynomial is explicitly stored
in **A26_VALUE_MINPOLY.json**.

## Reproduction and scope

Run **python verify.py 26** from the catalogue root. The launcher prepares the
included arithmetic libraries and executes the complete selected proof chain.
The supported environment is Windows x86-64 with CPython 3.12.
The selected stages are **verify_algebra26.py**, **verify26.py**, **verify26_directed.py**, **independent26.py**.
All coefficient tables, algebraic defining data and certificate inputs are
included in this entry. No optimizer, network access or external catalogue is
needed. The upper proof uses the universal reflection relations,
namely $A_i^2=B_j^2=I$ and $[A_i,B_j]=0$. Separate local ancilla dilations
cover binary effects without changing the relevant moments. Hence the upper
bound holds in arbitrary dimension and in the commuting model.
