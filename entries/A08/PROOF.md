# Exact quantum supremum of A8

The complete probability table **definition.json** defines
$$F=\sum_{i=0}^m\sum_{j=0}^n C_{ij}P_iQ_j,\qquad P_0=Q_0=I.$$
All constant, marginal and joint coefficients are retained. Throughout, binary
projections correspond to reflections by $P_i=(I+A_i)/2$, $Q_j=(I+B_j)/2$.
The field **four_times_reflection_matrix** is the coefficient matrix of $4F$.

## Five-square universal upper bound

Let $J$ be the joint block of **four_times_reflection_matrix**, so
$F=-3/2+\sum_{ij}J_{ij}A_iB_j/4$. Set
$$\lambda=(2\sqrt{70}/7,2\sqrt{70}/7,\sqrt{70}/7,\sqrt{70}/7,\sqrt{70}/7),
\quad D_j=\sum_iJ_{ij}A_i.$$
The literal coefficient calculation gives
$J\operatorname{diag}(1/\lambda)J^T$ diagonal and its trace plus
$\sum_j\lambda_j$ equal to $2\sqrt{70}$. Expansion therefore proves
$$\frac{\sqrt{70}-6}{4}I-F=
\sum_{j=1}^5\frac{(D_j-\lambda_jB_j)^2}{8\lambda_j}\succeq0.$$

## Attainment

Put $a=\sqrt{10/21}$, $z=\sqrt{11/21}$ and choose Alice's Bloch vectors
$$v_1=(a,0,z),\quad v_2=(-a/2,\sqrt{10/7}/2,z),\quad
v_3=(-a/2,-\sqrt{10/7}/2,z),\quad v_4=(1,0,0).$$
Set $u_j=\sum_iJ_{ij}v_i/\lambda_j$. The checker proves each $v_i,u_j$
has unit norm. On $|\Phi^+\rangle$ use $A_i=v_i\cdot\sigma$ and
$B_j=(u_j\cdot\sigma)^T$. Each square above annihilates the state.
Direct evaluation of the complete original probability polynomial gives
$(\sqrt{70}-6)/4$. Thus all three quantum suprema equal this value.

## Reproduction and scope

Run **python verify.py 8** from the catalogue root. The launcher prepares the
included arithmetic libraries and executes the complete selected proof chain.
The supported environment is Windows x86-64 with CPython 3.12.
The selected stages are **check_a8.py**.
All coefficient tables, algebraic defining data and certificate inputs are
included in this entry. No optimizer, network access or external catalogue is
needed. The upper proof uses the universal reflection relations,
namely $A_i^2=B_j^2=I$ and $[A_i,B_j]=0$. Separate local ancilla dilations
cover binary effects without changing the relevant moments. Hence the upper
bound holds in arbitrary dimension and in the commuting model.
