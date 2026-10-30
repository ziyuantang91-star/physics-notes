<a name="section-1"></a>

# AM02 Additional Mathematics Solutions

> **Edition scope:** original AI-assisted supplement or study material. Some prerequisite lessons are withheld for source review; their titles are plain text, not unavailable links. [Attribution and scope](../../SOURCES.md#pending).


> **Review status: unverified.** AI-assisted educational draft; human scientific review remains pending. [Sources and limitations](../../SOURCES.md).


**AI SUPPLEMENT — solutions, not learner records.** The derivations and checks support review; human scientific acceptance remains pending. Verification code and its limits are recorded in internal review documentation (not included in this collection).

<a name="section-2"></a>

## AM02-M01

**Polar basis from Cartesian components**. [Question](am02-additional-mathematics-practice.md#section-2) · [AM02 Math A - Moving Bases and Vector Products](am02-math-a-moving-bases-and-vector-products.md) · AM01 Math 5 - Chain Rule and Coordinate Changes (not included; [edition scope](../../SOURCES.md#pending)).

Component differentiation gives $\dot{\mathbf e}_r=\dot\theta\mathbf e_\theta$, $\dot{\mathbf e}_\theta=-\dot\theta\mathbf e_r$. Hence
$$\mathbf v=\dot r\mathbf e_r+r\dot\theta\mathbf e_\theta,\quad
\mathbf a=(\ddot r-r\dot\theta^2)\mathbf e_r+(2\dot r\dot\theta+r\ddot\theta)\mathbf e_\theta.$$
For constant radius/speed this is $\mathbf v=r_0\omega\mathbf e_\theta$ and $\mathbf a=-r_0\omega^2\mathbf e_r$. Direct Cartesian second derivatives of $(r_0\cos\omega t,r_0\sin\omega t)$ agree.

**Independent check / limits:** The acceleration is inward and has length/time² units.

**Common mistake:** Holding the polar basis fixed.

<a name="section-3"></a>

## AM02-M02

**Triple product and nonassociativity**. [Question](am02-additional-mathematics-practice.md#section-3) · [AM02 Math A - Moving Bases and Vector Products](am02-math-a-moving-bases-and-vector-products.md) · AM01 Math 5 - Chain Rule and Coordinate Changes (not included; [edition scope](../../SOURCES.md#pending)).

The $x$ component is $a_y(b_xc_y-b_yc_x)-a_z(b_zc_x-b_xc_z)$. Grouping and adding a canceling $a_xb_xc_x$ pair gives $b_x(\mathbf a\cdot\mathbf c)-c_x(\mathbf a\cdot\mathbf b)$. Cyclic relabeling of axes proves $y,z$. For the suggested basis vectors, $\mathbf a\times(\mathbf b\times\mathbf c)=\mathbf e_x\times\mathbf e_z=-\mathbf e_y$, while $(\mathbf a\times\mathbf b)\times\mathbf c=0$. The two bracketings differ.

**Independent check / limits:** The numerical basis-vector check independently fixes the sign.

**Common mistake:** Dropping parentheses or swapping a cyclic permutation for an arbitrary swap.

<a name="section-4"></a>

## AM02-M03

**A fixed vector seen by rotating axes**. [Question](am02-additional-mathematics-practice.md#section-4) · [AM02 Math A - Moving Bases and Vector Products](am02-math-a-moving-bases-and-vector-products.md) · AM01 Math 5 - Chain Rule and Coordinate Changes (not included; [edition scope](../../SOURCES.md#pending)).

Transport gives $D\mathbf u/dt=-\boldsymbol\Omega\times\mathbf u$. The component equations imply $\ddot u_x=-\Omega^2u_x$, $\dot u_x(0)=0$. Thus $u_x=u_0\cos\Omega t$, $u_y=-u_0\sin\Omega t$, $u_z=0$. The norm is $|u_0|$ by $\sin^2+\cos^2=1$; independently its squared norm derivative is $-2\mathbf u\cdot(\boldsymbol\Omega\times\mathbf u)=0$.

**Independent check / limits:** At $\Omega=0$ components are constant; positive frame rotation produces negative component rotation.

**Common mistake:** Using the inertial derivative for changing rotating components.

<a name="section-5"></a>

## AM02-M04

**Gradients in the rotation Lagrangian**. [Question](am02-additional-mathematics-practice.md#section-5) · [AM02 Math A - Moving Bases and Vector Products](am02-math-a-moving-bases-and-vector-products.md) · AM01 Math 5 - Chain Rule and Coordinate Changes (not included; [edition scope](../../SOURCES.md#pending)).

Scalar-triple symmetry gives $\mathbf v\cdot(\boldsymbol\Omega\times\mathbf r)=\mathbf r\cdot(\mathbf v\times\boldsymbol\Omega)$, whose gradient is $\mathbf v\times\boldsymbol\Omega$. The second gradient is $\Omega^2\mathbf r-(\boldsymbol\Omega\cdot\mathbf r)\boldsymbol\Omega$. In the stated check the scalar functions are $-v\Omega y$ and $\Omega^2(x^2+y^2)/2$, giving $(0,-v\Omega,0)$ and $(\Omega^2x,\Omega^2y,0)$, exactly the vector results.

**Independent check / limits:** Direct scalar component differentiation agrees and fixes both signs.

**Common mistake:** Allowing held-fixed velocity to vary with position in a partial derivative.

<a name="section-6"></a>

## AM02-M05

**Euler homogeneity with a cross term**. [Question](am02-additional-mathematics-practice.md#section-6) · [AM02 Math B - Homogeneity and Kinetic Forms](am02-math-b-homogeneity-and-kinetic-forms.md) · AM01 Math 5 - Chain Rule and Coordinate Changes (not included; [edition scope](../../SOURCES.md#pending)).

The chain rule yields $ug_u+vg_v=kg$ for differentiable degree-$k$ $g$. Direct derivatives are $T_u=Au+Cv+d$ and $T_v=Cu+Bv+e$. Therefore $uT_u+vT_v=Au^2+2Cuv+Bv^2+du+ev=2T_2+T_1$, and the requested expression is $Au^2/2+Cuv+Bv^2/2-f=T_2-T_0$. The coefficients may depend on other variables held fixed; that does not change the velocity-degree calculation.

**Independent check / limits:** Direct differentiation and the scaling proof agree, including the factor two on the mixed term.

**Common mistake:** Counting the mixed quadratic term as degree one.

<a name="section-7"></a>

## AM02-M06

**Positive kinetic energy with negative coupling**. [Question](am02-additional-mathematics-practice.md#section-7) · [AM02 Math B - Homogeneity and Kinetic Forms](am02-math-b-homogeneity-and-kinetic-forms.md) · AM01 Math 5 - Chain Rule and Coordinate Changes (not included; [edition scope](../../SOURCES.md#pending)).

We have $Q=A(u+Cv/A)^2+(B-C^2/A)v^2$. Both coefficients must be positive, so $AB-C^2>0$ is necessary and sufficient with $A>0$. Necessity follows by choosing $v\ne0,u=-Cv/A$. For $(2,2,-1)$ the remainder is $3/2>0$. For $(1,1,2)$ it is $-3$; $(u,v)=(-2,1)$ gives $Q=-3$. Positive entries alone do not establish positivity; negative off-diagonal entries do not imply negative energy.

**Independent check / limits:** Direct substitution gives the negative value; at determinant zero a nonzero null direction appears.

**Common mistake:** Judging a matrix by entry signs instead of the quadratic form.

<a name="section-8"></a>

## AM02-M07

**Arc length removes coordinate-dependent inertia**. [Question](am02-additional-mathematics-practice.md#section-8) · [AM02 Math B - Homogeneity and Kinetic Forms](am02-math-b-homogeneity-and-kinetic-forms.md) · AM01 Math 5 - Chain Rule and Coordinate Changes (not included; [edition scope](../../SOURCES.md#pending)).

Euler–Lagrange gives $m(h\ddot s+h'\dot s^2/2)=-V'(s)$. Since $\ddot\ell=\sqrt h\ddot s+h'\dot s^2/(2\sqrt h)$, division by $\sqrt h$ gives $m\ddot\ell=-V'/\sqrt h=-dV/d\ell$. The derivative $d\ell/ds=\sqrt h>0$ makes the transformation locally invertible and avoids division by zero. It also yields kinetic energy $m\dot\ell^2/2$. If $h=0$, the chosen parameterization is singular and this argument fails there.

**Independent check / limits:** For constant $h=h_0$, $\ell=\sqrt{h_0}s+\text{constant}$ and the result is ordinary rescaling.

**Common mistake:** Treating the extra $h'$ term as a new physical force.

<a name="section-9"></a>

## AM02-M08

**When a velocity-linear term matters**. [Question](am02-additional-mathematics-practice.md#section-9) · [AM02 Math B - Homogeneity and Kinetic Forms](am02-math-b-homogeneity-and-kinetic-forms.md) · AM01 Math 5 - Chain Rule and Coordinate Changes (not included; [edition scope](../../SOURCES.md#pending)).

Momentum is $p=A\dot q+B$ and energy is $E=A\dot q^2/2+C$. Product differentiation gives
$$A\ddot q+\tfrac12A_q\dot q^2+A_t\dot q+B_t+C_q=0.$$
For $B(q)$, its contribution is $d[\int B(q)dq]/dt$ on an interval. For $B=\gamma t$, the equation is $m\ddot q+\gamma=0$. Although $\gamma t\dot q=d(\gamma tq)/dt-\gamma q$, removing the full time derivative leaves a potential term $-\gamma q$ in $L$; the acceleration is real in this specified model. Dropping only the velocity-linear term loses the force.

**Independent check / limits:** Direct derivatives verify the equation; for $\gamma=0$ the example becomes free motion.

**Common mistake:** Assuming every velocity-linear term can be discarded even with time-dependent coefficient.

<a name="section-10"></a>

## AM02-M09

**Two vector potentials, one curl**. [Question](am02-additional-mathematics-practice.md#section-10) · [AM02 Math C - Curl Circulation and Gauge](am02-math-c-curl-circulation-and-gauge.md) · AM01 Math 5 - Chain Rule and Coordinate Changes (not included; [edition scope](../../SOURCES.md#pending)).

Both curls equal $(0,0,B)$. Their difference $(By/2,Bx/2,0)$ is $\nabla(Bxy/2)$. For symmetric gauge the tangential component is $Ba/2$, giving $B\pi a^2$. In Landau gauge, $x=a\cos\theta$ and $dy=a\cos\theta\,d\theta$, so the circulation is $Ba^2\int_0^{2\pi}\cos^2\theta\,d\theta=B\pi a^2$. Their difference is the closed-path integral of a single-valued gradient and vanishes.

**Independent check / limits:** The two direct parameter integrations equal the magnetic flux; units are T m².

**Common mistake:** Treating Landau-gauge tangential component as constant.

<a name="section-11"></a>

## AM02-M10

**Check planar Stokes by four edges**. [Question](am02-additional-mathematics-practice.md#section-11) · [AM02 Math C - Curl Circulation and Gauge](am02-math-c-curl-circulation-and-gauge.md) · AM01 Math 5 - Chain Rule and Coordinate Changes (not included; [edition scope](../../SOURCES.md#pending)).

The bottom edge has $A_x=0$ and the left edge $A_y=0$. The right edge contributes $\int_0^b ca^3dy=ca^3b$. The top edge is traversed from $x=a$ to $0$, so it contributes $\int_a^0(-cb^3)dx=cab^3$. Total circulation is $cab(a^2+b^2)$. Independently,
$$\int_0^a\int_0^b3c(x^2+y^2)\,dy\,dx=c(a^3b+ab^3).$$
Equality follows from ordinary polynomial integration; no general theorem needs to be assumed.

**Independent check / limits:** Reversing orientation flips circulation and the corresponding surface normal. Both computations are exactly equal.

**Common mistake:** Traversing the top edge in the wrong direction.

<a name="section-12"></a>

## AM02-M11

**Gauge cancellation with mixed partials**. [Question](am02-additional-mathematics-practice.md#section-12) · [AM02 Math C - Curl Circulation and Gauge](am02-math-c-curl-circulation-and-gauge.md) · AM01 Math 5 - Chain Rule and Coordinate Changes (not included; [edition scope](../../SOURCES.md#pending)).

The additions are $\Delta\mathbf A=(2\gamma tx,0,0)$, $\Delta\phi=-\gamma x^2$, $\Delta\mathbf p=(2q\gamma tx,0,0)$ and $\Delta E_L=-q\gamma x^2$. Their electric-field change is $-\nabla(-\gamma x^2)-\partial_t(2\gamma tx,0,0)=(2\gamma x,0,0)-(2\gamma x,0,0)=0$. The added vector has zero curl. The Lagrangian increment is $q\gamma x^2+2q\gamma tx\dot x=q\,d(\gamma tx^2)/dt$, independently proving equation equivalence.

**Independent check / limits:** The derivative of the energy shift is generally nonzero although fields are unchanged. Units require $q\chi$ to be an action.

**Common mistake:** Confusing gauge-invariant fields with gauge-dependent canonical variables.

<a name="section-13"></a>

## AM02-M12

**Why magnetic coupling is not a removable derivative**. [Question](am02-additional-mathematics-practice.md#section-13) · [AM02 Math C - Curl Circulation and Gauge](am02-math-c-curl-circulation-and-gauge.md) · AM01 Math 5 - Chain Rule and Coordinate Changes (not included; [edition scope](../../SOURCES.md#pending)).

If $\chi_x=-y$ and $\chi_y=x$, then $\chi_{xy}=-1$ and $\chi_{yx}=1$, contradicting equality of mixed partials. Independently, circle circulation is $2\pi a^2\ne0$, while a single-valued gradient has zero closed circulation. On $y=0$, $d\mathbf r=(dx,0,0)$ and $\mathbf A=(0,x,0)$, so $\mathbf A\cdot d\mathbf r=0$. Its one-coordinate pullback is thus the derivative of a constant. Restricting allowed paths can remove the tangential effect while leaving a normal force that the constraint must supply. This anticipates X09 without declaring the full two-dimensional field exact.

**Independent check / limits:** The curl is $2\mathbf e_z$. The zero line pullback and nonzero circular circulation concern different allowed paths and are consistent.

**Common mistake:** Inferring full-space exactness from one constrained path.

[Section index](README.md) · [Home](../../README.md)
