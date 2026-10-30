<a name="section-1"></a>

# New mathematics — Constraints, Equations and Stability

> **Edition scope:** original AI-assisted supplement or study material. Some prerequisite lessons are withheld for source review; their titles are plain text, not unavailable links. [Attribution and scope](../../SOURCES.md#pending).


> **Review status: unverified.** AI-assisted educational draft; human scientific review remains pending. [Sources and limitations](../../SOURCES.md).


**AI SUPPLEMENT:** original questions designed for this lecture. No problem below is presented as a copied or authenticated Morin/competition problem. Source paragraphs identify the concept being practiced. Difficulty and time are estimates, not quotas or evidence of mastery.

These fourteen problems support two new prerequisites: N1–N8 for [Math 6, linear algebra](am01-math-6-linear-algebra-for-constraints.md), and N9–N14 for [Math 7, second-order equations and stability](am01-math-7-second-order-equations-and-stability.md). They do not require repeating the 27 pilot exercises and do not count toward either physics set.

[Progressive hints](am01-new-mathematics-hints.md) · [Separate solutions](am01-new-mathematics-solutions.md)

<a name="section-2"></a>

## Problem index

| ID | Focus | Estimated difficulty | Time |
| --- | --- | --- | --- |
| [AM01-N1](am01-new-mathematics-practice.md#section-3) | Row reduction and a null-space basis | Foundation | 15 min |
| [AM01-N2](am01-new-mathematics-practice.md#section-4) | A distance constraint in six coordinates | Developing | 20 min |
| [AM01-N3](am01-new-mathematics-practice.md#section-5) | Two affine planes and their tangent direction | Foundation | 15 min |
| [AM01-N4](am01-new-mathematics-practice.md#section-6) | An affine velocity set on a changing ellipse | Developing | 25 min |
| [AM01-N5](am01-new-mathematics-practice.md#section-7) | Recover normals from zero virtual work | Developing | 20 min |
| [AM01-N6](am01-new-mathematics-practice.md#section-8) | A coordinate map and its singularity | Transfer | 30 min |
| [AM01-N7](am01-new-mathematics-practice.md#section-9) | Inhomogeneous systems and compatibility | Developing | 20 min |
| [AM01-N8](am01-new-mathematics-practice.md#section-10) | A singular crossing versus a poor equation | Transfer | 30 min |
| [AM01-N9](am01-new-mathematics-practice.md#section-11) | Solve an oscillator and prove completeness | Foundation | 20 min |
| [AM01-N10](am01-new-mathematics-practice.md#section-12) | Remove a constant drive by shifting equilibrium | Developing | 20 min |
| [AM01-N11](am01-new-mathematics-practice.md#section-13) | Growth does not disappear because one trajectory decays | Developing | 25 min |
| [AM01-N12](am01-new-mathematics-practice.md#section-14) | A zero quadratic term and a quartic stability test | Transfer | 30 min |
| [AM01-N13](am01-new-mathematics-practice.md#section-15) | Linearize a coordinate-dependent inertia carefully | Transfer | 30 min |
| [AM01-N14](am01-new-mathematics-practice.md#section-16) | Energy decay and uniqueness without complex roots | Transfer | 25 min |

<a name="section-3"></a>

## AM01-N1

**Row reduction and a null-space basis**

**Source:** Original AI mathematics exercise for the rank prerequisite to P086–P095.

**Prerequisite concepts:** [AM01 Math 6 - Linear Algebra for Constraints](am01-math-6-linear-algebra-for-constraints.md)

**Prerequisite tags:** #am01/math-6

**Estimated difficulty/time:** Foundation; 15 minutes.

Solve $A\mathbf u=0$ for $A=\begin{pmatrix}1&2&-1\\2&4&-2\\0&1&1\end{pmatrix}$. Find its rank, a null-space basis, and the number of free variables. Explain why the second row removes no additional freedom.

[Hints, open only as needed](am01-new-mathematics-hints.md#section-2) · [Solution, open after an attempt](am01-new-mathematics-solutions.md#section-2)

<a name="section-4"></a>

## AM01-N2

**A distance constraint in six coordinates**

**Source:** Original AI exercise connecting rank to the rod model in P137–P143.

**Prerequisite concepts:** [AM01 Math 6 - Linear Algebra for Constraints](am01-math-6-linear-algebra-for-constraints.md)

**Prerequisite tags:** #am01/math-6

**Estimated difficulty/time:** Developing; 20 minutes.

Two particles in space obey $f=|\mathbf r_2-\mathbf r_1|^2-\ell^2=0$, $\ell>0$. Write its $1\times6$ Jacobian and derive the dimension of its null space. Separate the allowed variations into common translations and changes of relative direction. What fails if the equation is instead used with $\ell=0$?

[Hints, open only as needed](am01-new-mathematics-hints.md#section-3) · [Solution, open after an attempt](am01-new-mathematics-solutions.md#section-3)

<a name="section-5"></a>

## AM01-N3

**Two affine planes and their tangent direction**

**Source:** Original AI mathematics exercise; local coordinate reasoning for P158–P176.

**Prerequisite concepts:** [AM01 Math 6 - Linear Algebra for Constraints](am01-math-6-linear-algebra-for-constraints.md)

**Prerequisite tags:** #am01/math-6

**Estimated difficulty/time:** Foundation; 15 minutes.

Solve $x+y+z=1$, $x-y+z=0$. Parameterize the intersection, find the tangent null space of the coefficient matrix, and explain why the position set itself is not a vector space.

[Hints, open only as needed](am01-new-mathematics-hints.md#section-4) · [Solution, open after an attempt](am01-new-mathematics-solutions.md#section-4)

<a name="section-6"></a>

## AM01-N4

**An affine velocity set on a changing ellipse**

**Source:** Original AI applied-mathematics exercise for fixed-time versus actual changes.

**Prerequisite concepts:** [AM01 Math 6 - Linear Algebra for Constraints](am01-math-6-linear-algebra-for-constraints.md) · AM01 Math 5 - Chain Rule and Coordinate Changes (not included; [edition scope](../../SOURCES.md#pending))

**Prerequisite tags:** #am01/math-6 #am01/math-5

**Estimated difficulty/time:** Developing; 25 minutes.

Let $a>0$ be constant and $b(t)>0$ be prescribed. A point obeys $x^2/a^2+y^2/b(t)^2=1$. Derive the equations for virtual variations and actual velocities. Show that one particular allowed velocity is $(0,\dot b\,y/b)$ and give all velocities by adding a tangent direction. Evaluate both conditions at $(x,y)=(0,b)$.

[Hints, open only as needed](am01-new-mathematics-hints.md#section-5) · [Solution, open after an attempt](am01-new-mathematics-solutions.md#section-5)

<a name="section-7"></a>

## AM01-N5

**Recover normals from zero virtual work**

**Source:** Original AI mathematics exercise for ideal constraint reactions in P201–P234.

**Prerequisite concepts:** [AM01 Math 6 - Linear Algebra for Constraints](am01-math-6-linear-algebra-for-constraints.md)

**Prerequisite tags:** #am01/math-6

**Estimated difficulty/time:** Developing; 20 minutes.

At a point constrained by $x+y=1$ and $z=0$, find all vectors $\mathbf R$ satisfying $\mathbf R\cdot\delta\mathbf r=0$ for every admissible tangent variation. Express them using the two constraint gradients. If the first constraint is replaced by $2x+2y=2$, how does its multiplier change?

[Hints, open only as needed](am01-new-mathematics-hints.md#section-6) · [Solution, open after an attempt](am01-new-mathematics-solutions.md#section-6)

<a name="section-8"></a>

## AM01-N6

**A coordinate map and its singularity**

**Source:** Original AI mathematics exercise for local charts and the mass matrix.

**Prerequisite concepts:** [AM01 Math 6 - Linear Algebra for Constraints](am01-math-6-linear-algebra-for-constraints.md) · AM01 Math 5 - Chain Rule and Coordinate Changes (not included; [edition scope](../../SOURCES.md#pending))

**Prerequisite tags:** #am01/math-6 #am01/math-5

**Estimated difficulty/time:** Transfer; 30 minutes.

Consider $\mathbf r(u,\theta)=(u+a\cos\theta,a\sin\theta)$ with $a>0$. Compute the two tangent columns, their determinant, and the kinetic matrix for a particle of mass $m>0$. Determine where the map is a regular local coordinate choice. At $\theta=\pi/2$, exhibit a nonzero coordinate variation with zero first-order physical displacement.

[Hints, open only as needed](am01-new-mathematics-hints.md#section-7) · [Solution, open after an attempt](am01-new-mathematics-solutions.md#section-7)

<a name="section-9"></a>

## AM01-N7

**Inhomogeneous systems and compatibility**

**Source:** Original AI mathematics exercise for affine admissible velocities.

**Prerequisite concepts:** [AM01 Math 6 - Linear Algebra for Constraints](am01-math-6-linear-algebra-for-constraints.md)

**Prerequisite tags:** #am01/math-6

**Estimated difficulty/time:** Developing; 20 minutes.

Solve $u+v=2$, $v+w=1$. Write the complete solution as one particular vector plus a null-space vector. Determine whether appending $u+2v+w=3$ changes the set, and whether appending $u+2v+w=4$ instead is possible.

[Hints, open only as needed](am01-new-mathematics-hints.md#section-8) · [Solution, open after an attempt](am01-new-mathematics-solutions.md#section-8)

<a name="section-10"></a>

## AM01-N8

**A singular crossing versus a poor equation**

**Source:** Original AI mathematics exercise for the regularity caveat SC-04/SC-07.

**Prerequisite concepts:** [AM01 Math 6 - Linear Algebra for Constraints](am01-math-6-linear-algebra-for-constraints.md)

**Prerequisite tags:** #am01/math-6

**Estimated difficulty/time:** Transfer; 30 minutes.

Compare (a) $x^2-y^2=0$ at the origin and at $(1,1)$, and (b) $(y-x)^2=0$ at the origin. For each, inspect the Jacobian and actual solution set. In (a), show that a differentiable path through the origin on the set can have velocity only along one of two lines, even though its linearized equation imposes no restriction. Explain why the two singularities differ.

[Hints, open only as needed](am01-new-mathematics-hints.md#section-9) · [Solution, open after an attempt](am01-new-mathematics-solutions.md#section-9)

<a name="section-11"></a>

## AM01-N9

**Solve an oscillator and prove completeness**

**Source:** Original AI mathematics exercise for second-order equations used in the supplementary physics practice.

**Prerequisite concepts:** [AM01 Math 7 - Second Order Equations and Stability](am01-math-7-second-order-equations-and-stability.md)

**Prerequisite tags:** #am01/math-7

**Estimated difficulty/time:** Foundation; 20 minutes.

Solve $\ddot z+9z=0$ with $z(0)=2$, $\dot z(0)=-3$. Verify the equation and initial data, compute the conserved quadratic quantity $(\dot z^2+9z^2)/2$, and explain why another solution with the same data cannot differ. Treat the variables as dimensionless mathematical quantities.

[Hints, open only as needed](am01-new-mathematics-hints.md#section-10) · [Solution, open after an attempt](am01-new-mathematics-solutions.md#section-10)

<a name="section-12"></a>

## AM01-N10

**Remove a constant drive by shifting equilibrium**

**Source:** Original AI mathematics exercise supporting spring and Atwood transfer problems.

**Prerequisite concepts:** [AM01 Math 7 - Second Order Equations and Stability](am01-math-7-second-order-equations-and-stability.md)

**Prerequisite tags:** #am01/math-7

**Estimated difficulty/time:** Developing; 20 minutes.

For $m,k>0$ and constant $F_0$, solve $m\ddot q+kq=F_0$ with $q(0)=q_0$, $\dot q(0)=v_0$. Derive the shift rather than quoting a forced-oscillator formula, and check units of the equilibrium and frequency.

[Hints, open only as needed](am01-new-mathematics-hints.md#section-11) · [Solution, open after an attempt](am01-new-mathematics-solutions.md#section-11)

<a name="section-13"></a>

## AM01-N11

**Growth does not disappear because one trajectory decays**

**Source:** Original AI mathematics exercise for instability and second-order initial data.

**Prerequisite concepts:** [AM01 Math 7 - Second Order Equations and Stability](am01-math-7-second-order-equations-and-stability.md)

**Prerequisite tags:** #am01/math-7

**Estimated difficulty/time:** Developing; 25 minutes.

Solve $\ddot z-4z=0$ for general $z(0)=z_0$, $\dot z(0)=v_0$. Specialize to $(z_0,v_0)=(1,0)$. Identify initial data for which the forward-time growing term vanishes, and explain why that special family does not make the equilibrium stable.

[Hints, open only as needed](am01-new-mathematics-hints.md#section-12) · [Solution, open after an attempt](am01-new-mathematics-solutions.md#section-12)

<a name="section-14"></a>

## AM01-N12

**A zero quadratic term and a quartic stability test**

**Source:** Original AI mathematics exercise supporting the critical rotating-hoop analysis.

**Prerequisite concepts:** [AM01 Math 7 - Second Order Equations and Stability](am01-math-7-second-order-equations-and-stability.md)

**Prerequisite tags:** #am01/math-7

**Estimated difficulty/time:** Transfer; 30 minutes.

Let $L=m\dot q^2/2-V(q)$ with $m>0$ and $V(q)=a q^2/2+b q^4/4$, where $b>0$ and $a$ can have either sign or vanish. Find all equilibria and classify their local stability as $a$ changes. Give the nonzero linear small-oscillation frequencies where applicable. Explain the $a=0$ case without relying on a vanished quadratic coefficient.

[Hints, open only as needed](am01-new-mathematics-hints.md#section-13) · [Solution, open after an attempt](am01-new-mathematics-solutions.md#section-13)

<a name="section-15"></a>

## AM01-N13

**Linearize a coordinate-dependent inertia carefully**

**Source:** Original AI mathematics exercise connecting coordinate geometry and small-oscillation dynamics.

**Prerequisite concepts:** [AM01 Math 7 - Second Order Equations and Stability](am01-math-7-second-order-equations-and-stability.md) · [AM01 Math 6 - Linear Algebra for Constraints](am01-math-6-linear-algebra-for-constraints.md)

**Prerequisite tags:** #am01/math-7 #am01/math-6

**Estimated difficulty/time:** Transfer; 30 minutes.

Let $L=A(q)\dot q^2/2-k(q-q_*)^2/2$, with $A(q)=m(1+q^2/a^2)$ and $m,a,k>0$. Derive the exact equation, then substitute $q=q_*+\varepsilon\eta$ and retain only first order in $\varepsilon$. Obtain the local frequency and identify the orders of the discarded terms.

[Hints, open only as needed](am01-new-mathematics-hints.md#section-14) · [Solution, open after an attempt](am01-new-mathematics-solutions.md#section-14)

<a name="section-16"></a>

## AM01-N14

**Energy decay and uniqueness without complex roots**

**Source:** Original AI mathematics exercise supporting the damped-oscillator representation in M09.

**Prerequisite concepts:** [AM01 Math 7 - Second Order Equations and Stability](am01-math-7-second-order-equations-and-stability.md)

**Prerequisite tags:** #am01/math-7

**Estimated difficulty/time:** Transfer; 25 minutes.

For $m,b,k>0$, prove that every solution of $m\ddot q+b\dot q+kq=0$ has nonincreasing $E=m\dot q^2/2+kq^2/2$. Use the same idea to prove that two solutions with the same initial position and velocity coincide for later times. Does monotonicity alone prove that an arbitrary nonnegative quantity tends to zero?

[Hints, open only as needed](am01-new-mathematics-hints.md#section-15) · [Solution, open after an attempt](am01-new-mathematics-solutions.md#section-15)

[Section index](README.md) · [Home](../../README.md)
