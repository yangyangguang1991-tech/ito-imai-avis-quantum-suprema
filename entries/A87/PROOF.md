# Exact quantum supremum of A87

The complete original probability matrix, including all marginal terms and the constant, is given in [definition.json](definition.json). The convention is $F=\sum_{i,j} C_{ij}P_iQ_j$, with $P_0=Q_0=I$. No further scaling or shift is made.


## Exact value and explicit attaining strategy

Let $x_*=(a_1,a_2,a_3,u,b_5,p,s)$ be the unique stationary root of the rational
function below in the exact box specified by
`algebra/strategy/A87_ROOT_DEFINITION.json`. The box centre, radius and rational
preconditioner are inputs to the interval contraction proof; the centre itself
is not the root.

Put

$$R(z)=\frac{(1-z^2)Z+2zX}{1+z^2},\quad
\alpha=\frac{1-2p^2}{1+2p^2},\quad
\gamma=\frac{2p}{1+2p^2}.$$

For $R(u)=u_z Z+u_x X$, define
$V_0=-u_x Z+u_z X$, and
$U=R(u)\otimes I_2$, $V=V_0\otimes Z$, $W=V_0\otimes X$.
Use the following four-dimensional local reflections:

$$\begin{aligned}
(A_1,A_2,A_3,A_4,A_5)&=(R(a_1)\otimes I_2,R(a_2)\otimes I_2,
 R(a_3)\otimes Z,R(a_3)\otimes X,R(a_3)\otimes X),\\
(B_1,B_2,B_3,B_4)&=(\alpha U-\gamma V+\gamma W,
 \alpha U+\gamma V-\gamma W,\alpha U+\gamma V+\gamma W,
 -\alpha U+\gamma V+\gamma W),\\
B_5&=R(b_5)\otimes I_2.
\end{aligned}$$

The three operators $U,V,W$ square to $I$ and anticommute pairwise, while
$\alpha^2+2\gamma^2=1$. Thus every displayed operator is a Hermitian reflection.
The state is

$$|\psi\rangle=\frac{|00\rangle+|11\rangle+s|22\rangle+s|33\rangle}
{\sqrt{2+2s^2}}.$$

With $t=(1,1,s,s)$, $A_0=B_0=I_4$ and the literal table $T$ for $4F$, define

$$f(x)=\frac{\sum_{i,j=0}^{5}T_{ij}\sum_{a,b=0}^{3}
t_at_b(A_i)_{ab}(B_j)_{ab}}{4\sum_{a=0}^{3}t_a^2}.$$

The matrices here are real, and this is exactly their Bell expectation.
The rational stationary system $\nabla f(x_*)=0$, its isolating box and
$\beta=f(x_*)$ constitute the exact algebraic definition. The root checker
proves a strict self-mapping contraction, not merely a small residual.

## Common-action family and full stationarity

For the upper certificate one uses a larger attaining circle family. In the
second internal qubit replace the repeated $X$ in $A_4,A_5$ by
$cX-dY,cX+dY$, respectively, with $c^2+d^2=1$. The corresponding four Bob
combinations are given explicitly in `algebra/stationarity/stationarity87.py`.
Polynomial reduction modulo the circle equation proves Hermiticity, the
reflection identities and independence of the Bell score from this circle.
The displayed witness is the member $(c,d)=(1,0)$.

The same symbolic calculation proves the complete first-order measurement and
state conditions from the seven isolated stationary equations, including the
additional relation used to express the Pauli action features. These are
properties of the attaining family and scalar certificate construction. They
are not added as relations on arbitrary competing observables.

## Exact annihilators and coefficient compatibility

The universal word list has276 words: the identity, single generators,
cross-party pairs, ordered distinct same-party pairs and both types of
three-letter word with a distinct same-party pair. Words are reduced only by
reflection cancellation and cross-party commutation. The exact eight-element
Bell-preserving signed permutation group is checked on the original table.

The independently reconstructed Pauli action gives a276-row matrix of56
polynomial features. Six rational character sectors and their polynomial
annihilator columns are provided in the frame data. Exact multiplication
checks every annihilator equation; interval nonsingular minors check all
denominators and the action ranks at the isolated root. A separate global
minor proves action rank40, so the common annihilator dimension is236.
The six Gram orders are14,14,60,60,44,44. Twirling preserves the target and
annihilation; cross-sector contributions vanish by the exact signed symmetries.

Let $L$ map the six symmetric Gram blocks to the1877 signed orbit coefficient
sums of the universal Hermitian polynomial. These sums encode the full
invariant polynomial, including the symmetry-forced zero coefficients.
The target $b$ is the corresponding coefficient vector of $\beta I-F$.

The exact compatibility construction has three parts. Constant action/moment
relations are checked from the regenerated Pauli features. Physical moment
derivatives give left-null functionals because both factors in each polarized
annihilator product kill the physical state; their target pairings vanish by
the complete first-order conditions. Finally, additional functionals supported
on199 higher-word coefficient positions are constructed from an exact
168-pivot rational-function echelon witness. Every rebuilt equation of all six
Gram blocks is reduced to zero, leaving31 parameterized free directions.
Their support has no constant, marginal or joint Bell monomial, so their
pairing with $b$ is zero without a numerical tolerance.

At the root, a certified interval minor proves independence of105 selected
compatible functionals. Hence $\operatorname{rank}L\le1877-105=1772$.
A separately reconstructed1772-square coefficient minor $D=L[I,C]$ has an
exact integer Neumann certificate, proving the reverse inequality. Therefore
the selected functionals span the entire left kernel and $b$ lies in
$\operatorname{range}L$.

## Same-value correction and positivity

Let $g_0$ be the supplied dyadic six-block Gram seed and put

$$g_*=g_0+E_C D^{-1}(b_I-L_Ig_0).$$

Here $E_C$ inserts corrections into the selected Gram coordinates. This is a
finite rational-function expression at the same algebraic root as the
attaining strategy. The residual belongs to $\operatorname{range}L$ and is
zero on the selected rows; row restriction is injective on this1772-dimensional
range. Consequently $Lg_*=b$ in every coefficient, exactly.

Dyadic enclosures of the full coefficient minor and frames are rebuilt.
The inverse test uses signed integer digit products with explicit overflow
bounds and Python integer accumulation. The interval width, dyadic rounding
and target evaluation error all enter the correction estimate. For each of
the six blocks a rational congruence witness proves a strict positive margin
larger than the entire correction. Thus every corrected Gram block is
positive definite. The three deliberate coefficient, inverse and Gram
alterations are rejected by their corresponding mathematical checks.

After the eight-element group average, these identities give a positive
noncommutative sum of squares for $\beta I-F$ in the universal algebra
$A_i^2=B_j^2=I$, $[A_i,B_j]=0$. They apply in every commuting representation,
of arbitrary dimension. Partywise reflection dilations include binary effects.
The explicit four-dimensional local strategy gives the reverse inequality,
so

$$Q_{\mathrm{fin}}(A_{87})=Q_{\mathrm{sp}}(A_{87})=
Q_{\mathrm{com}}(A_{87})=\beta.$$

## Reproduction

Run `python verify.py 87` from the catalogue root. `replay.py` runs every stage
in `STEPS.json`: the original coefficient/word algebra, isolated root, circle
identities, full stationarity, regenerated action, complete frames, twirl,
rebuilt echelon equations, root denominators,105-function independence,
1772-minor enclosure and exact inverse, positive Gram correction, negative
controls, and final premise assembly. All mathematical inputs are included;
no earlier result file or external optimization run is a prerequisite.
