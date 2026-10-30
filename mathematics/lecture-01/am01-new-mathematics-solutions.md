<a name="section-1"></a>

# New mathematics — Constraints, Equations and Stability — Worked Solutions

> **Edition scope:** original AI-assisted supplement or study material. Some prerequisite lessons are withheld for source review; their titles are plain text, not unavailable links. [Attribution and scope](../../SOURCES.md#pending).


> **Review status: unverified.** AI-assisted educational draft; human scientific review remains pending. [Sources and limitations](../../SOURCES.md).


**Spoiler boundary:** open this note only when ready to inspect solutions. These are AI-generated worked solutions with separately recorded computational or alternative-derivation checks, not independent human scientific approval. Each problem remains in `status: unverified`.

<a name="section-2"></a>

## AM01-N1

**Row reduction and a null-space basis** · [Problem](am01-new-mathematics-practice.md#section-3)

Rows 1 and 3 are independent, while row 2 is twice row 1. After replacing row 2 by zero, the equations are $u+2v-w=0$ and $v+w=0$. Let $w=s$; then $v=-s$ and $u=3s$. Every solution is $s(3,-1,1)$, so a basis is $\{(3,-1,1)\}$, rank is 2 and nullity is $3-2=1$. The nonzero basis vector is independent by itself. Substitution gives $3+2(-1)-1=0$ and $-1+1=0$; the dependent row also vanishes.

**Independent check:** Exact row reduction and direct matrix multiplication are checked in the physics verification script.

**Common mistakes:** Counting written rows rather than pivots; choosing three free variables; reporting only one particular zero solution.

**Review prerequisites:** [AM01 Math 6 - Linear Algebra for Constraints](am01-math-6-linear-algebra-for-constraints.md)

<a name="section-3"></a>

## AM01-N2

**A distance constraint in six coordinates** · [Problem](am01-new-mathematics-practice.md#section-4)

The Jacobian is $A=(-2\mathbf d^T,2\mathbf d^T)$: the first three entries differentiate $\mathbf r_1$ and the last three differentiate $\mathbf r_2$. Because $|\mathbf d|=\ell>0$, rank is 1 and nullity is 5. With $\delta\mathbf r_1=\mathbf c-\mathbf w/2$, $\delta\mathbf r_2=\mathbf c+\mathbf w/2$, the condition becomes $2\mathbf d\cdot\mathbf w=0$. The common translation $\mathbf c$ has three free components; $\mathbf w$ lies in the two-dimensional perpendicular plane. Thus $3+2=5$ independently checks the count. For $\ell=0$, the actual set is $\mathbf r_1=\mathbf r_2$, dimension 3, while this squared-distance equation has zero Jacobian and falsely suggests six linearized freedoms. Replace it by three independent component equalities to obtain a regular description.

**Independent check:** The Jacobian is differentiated symbolically; the translation/relative-coordinate construction separately establishes all five directions.

**Common mistakes:** Treating each particle displacement as independent; applying the rank-one count at zero separation; mistaking a poor constraint representation for a six-dimensional physical set.

**Review prerequisites:** [AM01 Math 6 - Linear Algebra for Constraints](am01-math-6-linear-algebra-for-constraints.md)

<a name="section-4"></a>

## AM01-N3

**Two affine planes and their tangent direction** · [Problem](am01-new-mathematics-practice.md#section-5)

Subtracting gives $2y=1$, so $y=1/2$. Then $x+z=1/2$. Set $x=s$: $(x,y,z)=(0,1/2,1/2)+s(1,0,-1)$. The two coefficient rows are independent, so rank is 2. Homogeneous increments satisfy $\delta y=0$, $\delta z=-\delta x$, and their null space is spanned by $(1,0,-1)$. The position line does not contain the origin, so it is affine rather than a vector subspace; differences of its points are tangent vectors.

**Independent check:** Direct substitution verifies the affine line; exact elimination verifies the rank and tangent basis.

**Common mistakes:** Using the inhomogeneous position equations for a virtual displacement; assuming every straight line is a vector subspace.

**Review prerequisites:** [AM01 Math 6 - Linear Algebra for Constraints](am01-math-6-linear-algebra-for-constraints.md)

<a name="section-5"></a>

## AM01-N4

**An affine velocity set on a changing ellipse** · [Problem](am01-new-mathematics-practice.md#section-6)

At fixed time,
$$\frac{2x}{a^2}\delta x+\frac{2y}{b^2}\delta y=0.$$
For actual motion,
$$\frac{2x}{a^2}\dot x+\frac{2y}{b^2}\dot y=\frac{2y^2\dot b}{b^3}.$$
The proposed particular velocity gives the right side directly. The vector $\mathbf w=(-ay/b,bx/a)$ satisfies the homogeneous equation because the two contributions are $-2xy/(ab)$ and $+2xy/(ab)$. On the ellipse this vector is nonzero and the constraint rank is 1, so all velocities are $(0,\dot b\,y/b)+c\mathbf w$, with arbitrary rate coefficient $c$. At the top, the virtual condition gives $\delta y=0$, while the actual condition gives $\dot y=\dot b$; horizontal variation or velocity remains free. This affine set is not generally equal to the tangent subspace.

**Independent check:** Substitution verifies the particular and homogeneous parts separately, including the top-point limit.

**Common mistakes:** Omitting the explicit-time derivative; interpreting $\delta t=0$ as zero actual time derivative of the prescribed geometry.

**Review prerequisites:** [AM01 Math 6 - Linear Algebra for Constraints](am01-math-6-linear-algebra-for-constraints.md) · AM01 Math 5 - Chain Rule and Coordinate Changes (not included; [edition scope](../../SOURCES.md#pending))

<a name="section-6"></a>

## AM01-N5

**Recover normals from zero virtual work** · [Problem](am01-new-mathematics-practice.md#section-7)

A tangent variation is $(s,-s,0)$. Its pairing with $(R_x,R_y,R_z)$ is $(R_x-R_y)s$. Vanishing for every real $s$ requires $R_x=R_y$, with $R_z$ unrestricted. Thus $\mathbf R=(p,p,r)=p\nabla(x+y-1)+r\nabla z$. The multipliers are $(p,r)$. Replacing the first function by $2(x+y-1)$ doubles its gradient, so the same physical vector uses multiplier $p/2$. The reaction is invariant although the multiplier is not.

**Independent check:** The null-space dot-product argument and the independent normal-span calculation give the same full family.

**Common mistakes:** Concluding $\mathbf R=0$; assigning multiplier values without specifying the constraint-function normalization.

**Review prerequisites:** [AM01 Math 6 - Linear Algebra for Constraints](am01-math-6-linear-algebra-for-constraints.md)

<a name="section-7"></a>

## AM01-N6

**A coordinate map and its singularity** · [Problem](am01-new-mathematics-practice.md#section-8)

The columns are $(1,0)$ and $(-a\sin\theta,a\cos\theta)$. Their determinant is $a\cos\theta$, so the map is regular where $\cos\theta\ne0$. The mass matrix is
$$M=m\begin{pmatrix}1&-a\sin\theta\\-a\sin\theta&a^2\end{pmatrix},\qquad \det M=m^2a^2\cos^2\theta.$$
For a variation $(c_1,c_2)$, the quadratic form is $m[(c_1-a\sin\theta c_2)^2+(a\cos\theta c_2)^2]$, positive for nonzero variation on a regular patch. At $\theta=\pi/2$, choose $\delta u=a\delta\theta\ne0$. The physical first-order displacement is $(\delta u-a\delta\theta,0)=0$. This is a failure of the coordinate chart, not proof that the physical mass vanishes. Near the upper boundary $y=a$, the inverse angle branch is not a smooth two-dimensional chart.

**Independent check:** Determinants and the mass-matrix quadratic form are checked symbolically; the explicit null combination verifies the singular point.

**Common mistakes:** Assuming two symbols automatically mean two independent coordinate directions; interpreting a chart singularity as a new physical force.

**Review prerequisites:** [AM01 Math 6 - Linear Algebra for Constraints](am01-math-6-linear-algebra-for-constraints.md) · AM01 Math 5 - Chain Rule and Coordinate Changes (not included; [edition scope](../../SOURCES.md#pending))

<a name="section-8"></a>

## AM01-N7

**Inhomogeneous systems and compatibility** · [Problem](am01-new-mathematics-practice.md#section-9)

With $v=s$, $u=2-s$ and $w=1-s$, so the solution family is $(2,0,1)+s(-1,1,-1)$. Its homogeneous direction solves $u+v=0$, $v+w=0$. Adding the two original equations gives $u+2v+w=3$ identically, so the first appended condition is redundant. The alternative right side 4 conflicts with this exact consequence: there is no solution. Rank counting only after ignoring right-hand-side compatibility would miss this impossibility.

**Independent check:** Exact substitution confirms every family member and the redundant row; elimination of the inconsistent augmented row produces $0=1$.

**Common mistakes:** Counting a redundant equation as a new independent restriction; discussing nullity without first checking whether an affine solution exists.

**Review prerequisites:** [AM01 Math 6 - Linear Algebra for Constraints](am01-math-6-linear-algebra-for-constraints.md)

<a name="section-9"></a>

## AM01-N8

**A singular crossing versus a poor equation** · [Problem](am01-new-mathematics-practice.md#section-10)

In (a), the set is the union of $y=x$ and $y=-x$. Its gradient $(2x,-2y)$ vanishes at the origin, so the linearization permits the entire plane. But a differentiable path through zero has $x^2-y^2=(u^2-v^2)\varepsilon^2+o(\varepsilon^2)$; dividing by $\varepsilon^2$ and taking the limit requires $u^2=v^2$. Its possible first-order velocities form two crossing lines, not a vector space: $(1,1)$ and $(1,-1)$ are allowed but their sum $(2,0)$ is not. There is no single regular curve chart at the crossing. At $(1,1)$ the gradient is $(2,-2)$, rank 1, and the nearby branch is $y=x$ with tangent $(s,s)$.

In (b), the squared equation also has zero gradient, but its actual set is just the single straight line $y=x$. The equivalent regular equation $y-x=0$ has gradient $(-1,1)$ everywhere. Here the singularity comes from a bad equation representation rather than a crossing of physical branches. Neither case permits blindly applying $n-k$ to the written number of equations.

**Independent check:** The factorization gives the exact sets; the leading-order path argument checks the tangent possibilities independently of the zero Jacobian.

**Common mistakes:** Equating a singular linearized null space with the true tangent set; assuming every vanishing gradient means the actual set itself is nonsmooth.

**Review prerequisites:** [AM01 Math 6 - Linear Algebra for Constraints](am01-math-6-linear-algebra-for-constraints.md)

<a name="section-10"></a>

## AM01-N9

**Solve an oscillator and prove completeness** · [Problem](am01-new-mathematics-practice.md#section-11)

Write $z=A\cos3t+B\sin3t$. At zero, $A=2$ and $3B=-3$, so $z=2\cos3t-\sin3t$. Its derivative is $-6\sin3t-3\cos3t$ and its second derivative is $-18\cos3t+9\sin3t=-9z$. Initial data follow directly. The conserved quadratic quantity is its initial value $(9+36)/2=45/2$.

If $z_1,z_2$ share those data, their difference $w$ obeys $\ddot w+9w=0$ with both initial values zero. Multiplication by $\dot w$ proves $(\dot w^2+9w^2)/2$ remains zero. Nonnegativity forces $w=\dot w=0$. The displayed solution is therefore complete for the prescribed initial values.

**Independent check:** Direct symbolic differentiation checks the equation, initial values and conserved quantity; the nonnegative-energy uniqueness argument is a conceptual proof.

**Common mistakes:** Using the initial derivative itself as the sine coefficient; giving a trial solution without fixing both constants or checking uniqueness.

**Review prerequisites:** [AM01 Math 7 - Second Order Equations and Stability](am01-math-7-second-order-equations-and-stability.md)

<a name="section-11"></a>

## AM01-N10

**Remove a constant drive by shifting equilibrium** · [Problem](am01-new-mathematics-practice.md#section-12)

A constant solution has $kq_*=F_0$, so $q_*=F_0/k$. Put $\eta=q-q_*$; then $m\ddot\eta+k\eta=0$. The initial values are $\eta(0)=q_0-F_0/k$ and $\dot\eta(0)=v_0$. Thus
$$q(t)=\frac{F_0}{k}+\left(q_0-\frac{F_0}{k}\right)\cos\omega t+\frac{v_0}{\omega}\sin\omega t,\qquad \omega=\sqrt{k/m}.$$
Substituting cancels the oscillating terms and leaves $F_0$ on the right. If $q$ is a length, $F_0/k$ is a length and $k/m$ has inverse-time-squared units. The solution is exact for this linear equation; a nonlinear spring would need an approximation or another solution method.

**Independent check:** Equation residual and both initial values are checked symbolically; units are checked using force and stiffness definitions.

**Common mistakes:** Shifting the initial velocity by a constant position; forgetting the particular solution; treating an exact linear result as automatically exact for nonlinear forces.

**Review prerequisites:** [AM01 Math 7 - Second Order Equations and Stability](am01-math-7-second-order-equations-and-stability.md)

<a name="section-12"></a>

## AM01-N11

**Growth does not disappear because one trajectory decays** · [Problem](am01-new-mathematics-practice.md#section-13)

The initial equations are $A+B=z_0$ and $2(A-B)=v_0$, so
$$z(t)=\frac12\left(z_0+\frac{v_0}{2}\right)e^{2t}+\frac12\left(z_0-\frac{v_0}{2}\right)e^{-2t}.$$
For $(1,0)$ this is $(e^{2t}+e^{-2t})/2$. The growing coefficient vanishes only when $v_0=-2z_0$. On that one-dimensional line of initial states the solution decays, but arbitrarily small perturbations away from it produce a nonzero growing coefficient and eventual departure from any fixed small neighborhood. Thus the equilibrium is unstable. If this equation approximates a nonlinear system, use its growth conclusion only while the disturbance remains in the linear regime.

**Independent check:** The general expression is differentiated and checked against both initial data; stability is assessed from the existence of arbitrarily small growing disturbances.

**Common mistakes:** Calling an equilibrium stable because one solution decays; ignoring the initial derivative; extrapolating a linearized exponential indefinitely beyond its small-disturbance regime.

**Review prerequisites:** [AM01 Math 7 - Second Order Equations and Stability](am01-math-7-second-order-equations-and-stability.md)

<a name="section-13"></a>

## AM01-N12

**A zero quadratic term and a quartic stability test** · [Problem](am01-new-mathematics-practice.md#section-14)

For $a>0$, the only equilibrium is $q=0$, with curvature $a>0$ and frequency $\sqrt{a/m}$. It is a strict minimum and stable. For $a<0$, zero has negative curvature and is unstable. Two additional equilibria exist at $q_\pm=\pm\sqrt{-a/b}$. Their curvature is $a+3b(-a/b)=-2a>0$, so both are stable with frequency $\sqrt{-2a/m}$.

For $a=0$, the only equilibrium remains zero, but $V''(0)=0$. The actual potential is $bq^4/4$, a strict local and global minimum. Conserved energy $E=m\dot q^2/2+bq^4/4$ implies $|q|\le(4E/b)^{1/4}$ and $|\dot q|\le\sqrt{2E/m}$. Sufficiently small initial energy keeps the entire state near zero, proving stability. There is no nonzero amplitude-independent frequency from linearization; the linear frequency is zero and higher-order dynamics matters.

**Independent check:** Equilibria and curvatures are checked by exact differentiation; the quartic bounds provide an independent nonlinear energy proof at zero curvature.

**Common mistakes:** Using $V=0$ as an automatic instability verdict; omitting the two equilibria for $a<0$; assigning the harmonic formula a positive frequency at the quartic minimum.

**Review prerequisites:** [AM01 Math 7 - Second Order Equations and Stability](am01-math-7-second-order-equations-and-stability.md)

<a name="section-14"></a>

## AM01-N13

**Linearize a coordinate-dependent inertia carefully** · [Problem](am01-new-mathematics-practice.md#section-15)

The exact derivatives give
$$A(q)\ddot q+\frac12A'(q)\dot q^2+k(q-q_*)=0,$$
so here
$$m(1+q^2/a^2)\ddot q+\frac{mq}{a^2}\dot q^2+k(q-q_*)=0.$$
With $q=q_*+\varepsilon\eta$, the first term is $\varepsilon A(q_*)\ddot\eta+O(\varepsilon^2)$, the velocity-squared term is $O(\varepsilon^2)$, and the restoring term is $\varepsilon k\eta$. Thus
$$A(q_*)\ddot\eta+k\eta=0,\qquad \omega^2=\frac{k}{m(1+q_*^2/a^2)}.$$
For $q_*=0$, some leading nonlinear corrections are actually cubic: $q^2\ddot q$ and $q\dot q^2$ each scale as $\varepsilon^3$. In either case they do not enter the first-order equation. This order counting assumes a smooth family of small-amplitude motions with scaled velocities and accelerations, not an arbitrarily high-frequency perturbation whose derivatives grow as amplitude shrinks.

**Independent check:** The exact Euler–Lagrange expression and its first-order expansion are checked symbolically; the special zero-equilibrium cubic order is verified separately.

**Common mistakes:** Keeping only $A\ddot q$ in the exact equation; discarding the entire geometry before evaluating $A(q_*)$; counting powers of displacement while ignoring velocity scaling.

**Review prerequisites:** [AM01 Math 7 - Second Order Equations and Stability](am01-math-7-second-order-equations-and-stability.md) · [AM01 Math 6 - Linear Algebra for Constraints](am01-math-6-linear-algebra-for-constraints.md)

<a name="section-15"></a>

## AM01-N14

**Energy decay and uniqueness without complex roots** · [Problem](am01-new-mathematics-practice.md#section-16)

Multiplication by $\dot q$ yields $dE/dt=-b\dot q^2\le0$. For two solutions with the same initial data, let $z=q_1-q_2$. Linearity gives $m\ddot z+b\dot z+kz=0$, and $z(t_0)=\dot z(t_0)=0$. Its energy $E_z=m\dot z^2/2+kz^2/2$ is initially zero and nonincreasing for $t\ge t_0$, so $E_z\le0$. But positive $m,k$ also give $E_z\ge0$. Therefore $E_z=0$ and both $z,\dot z$ vanish. This proves forward uniqueness without solving a characteristic polynomial.

Monotonicity alone does not prove a zero limit: for example $1+e^{-t}$ is positive and decreasing toward 1. Additional dynamical reasoning would be needed to conclude a particular damped model approaches zero; the general monotonicity statement by itself is weaker.

**Independent check:** The energy identity is checked algebraically, and the zero-data nonnegative-energy argument proves uniqueness conceptually.

**Common mistakes:** Confusing nonincreasing energy with monotonic position; claiming every decreasing nonnegative function must tend to zero; using an oscillatory formula without establishing its applicable damping regime.

**Review prerequisites:** [AM01 Math 7 - Second Order Equations and Stability](am01-math-7-second-order-equations-and-stability.md)

[Section index](README.md) · [Home](../../README.md)
