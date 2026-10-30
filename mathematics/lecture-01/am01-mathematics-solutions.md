<a name="section-1"></a>

# AM01 — Mathematics Solutions

> **Edition scope:** original AI-assisted supplement or study material. Some prerequisite lessons are withheld for source review; their titles are plain text, not unavailable links. [Attribution and scope](../../SOURCES.md#pending).


> **Review status: unverified.** AI-assisted educational draft; human scientific review remains pending. [Sources and limitations](../../SOURCES.md).


**Answer-bearing file. AI SUPPLEMENT; human scientific review pending.** Try the questions first. These are original worked solutions; valid alternative approaches are welcome. “Checked” describes the stated algebraic or conceptual check, not a learner outcome or source-video verification.

[Questions](am01-mathematics-practice.md) · [Hints](am01-progressive-hints.md) · internal review documentation (not included in this collection)

<a name="section-2"></a>

## AM01-A1

**Concept:** Partial-derivative definitions. **Prerequisite:** AM01 Math 1 - Functions and Partial Derivatives (not included; [edition scope](../../SOURCES.md#pending)).

Holding $y$ fixed,
$$
\frac{f(x+h,y)-f(x,y)}h=y(3x^2+3xh+h^2).
$$
Thus $f_x=3x^2y$. Holding $x$ fixed gives $f_y=x^3+4y$. At $(1,-1)$ these are $-3$ and $-3$. Their equality at this point is accidental; for example at $(1,0)$ they are $0$ and $1$. The computation distinguishes an evaluated number from the full derivative function.

**Common mistakes:** Differentiating $y$ with respect to $x$ in a partial derivative; substituting the base point before taking the limit.

**Check:** Polynomial expansion and direct differentiation agree.

[Return to question](am01-mathematics-practice.md#section-3)

<a name="section-3"></a>

## AM01-A2

**Concept:** Domain and interior derivatives. **Prerequisite:** AM01 Math 1 - Functions and Partial Derivatives (not included; [edition scope](../../SOURCES.md#pending)).

The real domain is the closed disk $x^2+y^2\leq9$. At interior points,
$$
f_x=-\frac{x}{\sqrt{9-x^2-y^2}},\qquad
f_y=-\frac{y}{\sqrt{9-x^2-y^2}}.
$$
At $(1,2)$ the denominator is $2$, so $f_x=-1/2$ and $f_y=-1$. At $(3,0)$ the two-sided $x$ neighborhood is absent. The left difference quotient is $\sqrt{-6h-h^2}/h$ for $h<0$, which diverges to $-\infty$ as $h\uparrow0$. For $y\ne0$ with $x=3$, the formula is not real at all. Therefore the standard interior derivative definition cannot simply be applied at this boundary point.

**Common mistakes:** Using a zero denominator as a finite derivative; confusing the closed domain with an open differentiability region.

**Check:** Boundary behavior checked directly from the difference quotient.

[Return to question](am01-mathematics-practice.md#section-4)

<a name="section-4"></a>

## AM01-A3

**Concept:** Product and one-variable chain rules on slices. **Prerequisite:** AM01 Math 1 - Functions and Partial Derivatives (not included; [edition scope](../../SOURCES.md#pending)).

At fixed $y$, $f_x=y e^{xy}+\cos x\cos y$. At fixed $x$, $f_y=x e^{xy}-\sin x\sin y$. The values are $\pi/2$ and $0$. In one slice the exponent changes at rate $y$, and in the other at rate $x$: these factors are consequences of the declared independent input, not interchangeable labels.

**Common mistakes:** Omitting the inner-derivative factor or the minus sign from differentiating cosine.

**Check:** Expressions checked by symbolic differentiation.

[Return to question](am01-mathematics-practice.md#section-5)

<a name="section-5"></a>

## AM01-A4

**Concept:** Physical meaning and derivative units. **Prerequisite:** AM01 Math 1 - Functions and Partial Derivatives (not included; [edition scope](../../SOURCES.md#pending)).

Dimensional consistency requires $[\alpha]=\mathrm{K/m^2}$ and $[\beta]=\mathrm{K/m}$. The derivatives are $\Theta_x=2\alpha x$ and $\Theta_y=\beta$, both in $\mathrm{K/m}$. If $\alpha>0$, $\Theta_x$ is negative on the negative-$x$ side, zero at zero, and positive on the positive-$x$ side. A zero slope at the origin does not mean the field is constant: the quadratic dependence remains. This is a local mathematical temperature profile, not a claim that an arbitrary such field solves a heat equation.

**Common mistakes:** Assigning $\alpha$ units of kelvin without the length factor; interpreting a derivative as the temperature itself.

**Check:** Units checked term by term and signs checked against the parabola.

[Return to question](am01-mathematics-practice.md#section-6)

<a name="section-6"></a>

## AM01-A5

**Concept:** Partial derivative versus derivative along a path. **Prerequisite:** AM01 Math 1 - Functions and Partial Derivatives (not included; [edition scope](../../SOURCES.md#pending)).

The partial derivative is $f_x=y^2$, giving $4$. Along the path, $g(x)=x(3x-1)^2$, so
$$
g'(x)=(3x-1)^2+6x(3x-1),\qquad g'(1)=4+12=16.
$$
The extra $12$ arises because $y$ changes with $x$. Later the multivariable rule gives the same decomposition $f_x+f_y\,dy/dx=4+(2xy)3=16$. The point is identical but the permitted neighboring states differ.

**Common mistakes:** Treating a derived variable as fixed along a prescribed path; thinking different derivatives at the same point contradict each other.

**Check:** Direct substitution and the later chain-rule decomposition agree.

[Return to question](am01-mathematics-practice.md#section-7)

<a name="section-7"></a>

## AM01-B1

**Concept:** Four second partials and order notation. **Prerequisite:** AM01 Math 2 - Mixed Partials and Smoothness (not included; [edition scope](../../SOURCES.md#pending)).

First $f_x=2xe^y+y^3$, $f_y=x^2e^y+3xy^2$. Therefore
$$
f_{xx}=2e^y,\quad f_{xy}=2xe^y+3y^2,\quad
f_{yx}=2xe^y+3y^2,\quad f_{yy}=x^2e^y+6xy.
$$
The two mixed derivatives agree. The function is $C^2$ on an open neighborhood of every point, which is sufficient; equality of the pure second derivatives is neither required nor generally true.

**Common mistakes:** Taking $f_{xx}$ instead of $f_{xy}$; asserting equality of all four derivatives.

**Check:** All four expressions checked symbolically.

[Return to question](am01-mathematics-practice.md#section-9)

<a name="section-8"></a>

## AM01-B2

**Concept:** Regularity on a restricted domain. **Prerequisite:** AM01 Math 2 - Mixed Partials and Smoothness (not included; [edition scope](../../SOURCES.md#pending)).

We have $g_s=2s/v$, $g_v=-s^2/v^2$. Hence both mixed derivatives are $-2s/v^2$. The rational function is smooth on the open half-plane $v>0$, so the theorem applies there. At $v=0$ it is undefined; no extension or derivative at that boundary has been supplied. Equality on an open domain gives no license to substitute an excluded point.

**Common mistakes:** Extending a theorem through a singularity solely because two expressions match.

**Check:** Both derivative orders checked symbolically; the domain restriction checked separately.

[Return to question](am01-mathematics-practice.md#section-10)

<a name="section-9"></a>

## AM01-B3

**Concept:** Reconstructing the mixed-partial theorem. **Prerequisite:** AM01 Math 2 - Mixed Partials and Smoothness (not included; [edition scope](../../SOURCES.md#pending)).

For nonzero sufficiently small $h,k$, the rectangle lies inside the smooth neighborhood. The mean value theorem applied to $g$ gives
$R=h[f_x(\xi,b+k)-f_x(\xi,b)]=hk f_{xy}(\xi,\eta)$.
The reverse order, applied to $j(y)=f(a+h,y)-f(a,y)$, gives
$R=k[f_y(a+h,\widetilde\eta)-f_y(a,\widetilde\eta)]=hk f_{yx}(\widetilde\xi,\widetilde\eta)$.
All intermediate points lie in the rectangle. Divide by $hk$ and let $(h,k)\to(0,0)$. Continuity of each mixed derivative makes its value at the intermediate point tend to its value at $(a,b)$, so the two limits agree. Without continuity, existence of the two pointwise mixed derivatives alone does not justify those limits.

**Common mistakes:** Using equality of mixed partials inside the proof that is supposed to establish it; omitting the neighborhood and continuity steps.

**Check:** Logical proof checked using two applications of the ordinary mean value theorem in each order; no symbolic calculation substitutes for this argument.

[Return to question](am01-mathematics-practice.md#section-11)

<a name="section-10"></a>

## AM01-B4

**Concept:** Counterexample using limit definitions. **Prerequisite:** AM01 Math 2 - Mixed Partials and Smoothness (not included; [edition scope](../../SOURCES.md#pending)).

The bound $|f|\leq4|xy|\leq2(x^2+y^2)$ implies $f\to0$ at the origin. For $y\ne0$,
$$
f_x(0,y)=\lim_{h\to0}y\frac{h^2-4y^2}{h^2+y^2}=-4y.
$$
At $y=0$ this derivative is zero. Similarly $f_y(x,0)=x$ for all $x$, including zero by its definition. Thus $f_{xy}(0,0)=-4$ and $f_{yx}(0,0)=1$. Both exist and differ, so the $C^2$ hypothesis fails near the origin despite continuity of $f$. This is a failure of an assumption, not a counterexample to the correctly stated theorem.

**Common mistakes:** Substituting $(0,0)$ into a rational derivative formula; treating continuity of $f$ as continuity of its second derivatives.

**Check:** Axis limits checked symbolically and the continuity estimate checked analytically.

[Return to question](am01-mathematics-practice.md#section-12)

<a name="section-11"></a>

## AM01-C1

**Concept:** Differential versus exact finite change. **Prerequisite:** AM01 Math 3 - Differentials and Gradients (not included; [edition scope](../../SOURCES.md#pending)).

At the base point $f_x=1$ and $f_y=4$, hence $df=h+4k=-0.07$. Exact expansion gives
$$
\Delta f=h+4k+hk+k^2.
$$
The remainder is $hk+k^2=-0.0002+0.0004=0.0002$, so $\Delta f=-0.0698$. Halving $h,k$ halves $df$ and divides the remainder by four, because both remainder terms are homogeneous of degree two. A differential is a linear approximation to a finite change, not an equality with that change.

**Common mistakes:** Dropping the remainder while claiming an exact finite answer; confusing the base value of $f_x=y$ with $x+y$.

**Check:** Exact rational arithmetic and direct expansion checked.

[Return to question](am01-mathematics-practice.md#section-14)

<a name="section-12"></a>

## AM01-C2

**Concept:** Gradient and a directional derivative. **Prerequisite:** AM01 Math 3 - Differentials and Gradients (not included; [edition scope](../../SOURCES.md#pending)).

The domain is the punctured plane. $\nabla f=(2x,2y)/(x^2+y^2)$, so at $(3,4)$ it is $(6/25,8/25)$. The direction is unit length since $\sqrt{4^2+(-3)^2}/5=1$. Its derivative is
$$
(6/25)(4/5)+(8/25)(-3/5)=0.
$$
The direction is tangent to the constant-radius circle, while the gradient points radially. This is a first-order statement at the point: walking in a straight tangent line eventually changes radius at second order. A zero directional derivative does not make the whole gradient zero.

**Common mistakes:** Failing to normalize the direction when interpreting change per unit distance; claiming constant values along the whole straight tangent line.

**Check:** Dot product checked exactly; geometric interpretation compared to the circular contours.

[Return to question](am01-mathematics-practice.md#section-15)

<a name="section-13"></a>

## AM01-C3

**Concept:** Dot product, angle and projection. **Prerequisite:** AM01 Math 3 - Differentials and Gradients (not included; [edition scope](../../SOURCES.md#pending)).

$\mathbf a\cdot\mathbf b=2-3=-1$, $\|\mathbf a\|=\sqrt5$, and $\|\mathbf b\|=\sqrt{10}$. Hence $\cos\theta=-1/\sqrt{50}$, so the angle is obtuse. A signed component along $\widehat{\mathbf b}$ means the coefficient measured along that oriented unit axis; it is
$\mathbf a\cdot\widehat{\mathbf b}=-1/\sqrt{10}$.
The projection vector is this component times $\widehat{\mathbf b}$, namely $-\mathbf b/10$. Its difference from $\mathbf a$ has zero dot product with $\mathbf b$, an independent orthogonality check.

**Common mistakes:** Confusing the scalar projection with a vector; dividing by $\|\mathbf b\|^2$ when asked for the scalar component.

**Check:** Projection remainder checked to be perpendicular to $\mathbf b$.

[Return to question](am01-mathematics-practice.md#section-16)

<a name="section-14"></a>

## AM01-C4

**Concept:** Energy gradients and power. **Prerequisite:** AM01 Math 3 - Differentials and Gradients (not included; [edition scope](../../SOURCES.md#pending)).

$\mathbf F=-(\alpha y+2\beta x,\alpha x)$. Along the path,
$V(t)=\alpha vbt+\beta v^2t^2$, so
$$
\frac{dV}{dt}=\alpha vb+2\beta v^2t.
$$
The force power is $[-\alpha b-2\beta vt]v+[-\alpha vt]0$, the negative of that rate. Units are $\mathrm{J/s}$. This identity holds on the prescribed path and does not prove the path satisfies Newton's law for this force alone. Additional forces may be needed to maintain it; the identity concerns work by the specified conservative force.

**Common mistakes:** Claiming a kinematically prescribed path automatically solves dynamics; omitting the force minus sign or counting a perpendicular component as power.

**Check:** Direct composition and gradient-based power give opposite rates as required.

[Return to question](am01-mathematics-practice.md#section-17)

<a name="section-15"></a>

## AM01-C5

**Concept:** Differentials and uncertainty sensitivity. **Prerequisite:** AM01 Math 3 - Differentials and Gradients (not included; [edition scope](../../SOURCES.md#pending)).

$P_\ell=P/(2\ell)$ and $P_g=-P/(2g)$, hence
$$
\frac{dP}{P}=\frac12\frac{d\ell}{\ell}-\frac12\frac{dg}{g}.
$$
The first-order worst-case estimate is $\tfrac12(1\%+0.4\%)=0.7\%$. Opposite-signed relative errors make the contributions reinforce. This linear estimate omits higher-order terms. Statistical propagation would require a probabilistic model and correlations, neither supplied here. The physical period law itself assumes small oscillations, a point bob and an ideal fixed-length pendulum; the exercise tests sensitivity calculus, not its dynamical derivation.

**Common mistakes:** Adding errors algebraically while claiming a worst case; replacing a bound by an independent-Gaussian rule without assumptions.

**Check:** Partial derivatives checked; dimensions and the exact ratio $\sqrt{(1+\epsilon_\ell)/(1+\epsilon_g)}$ support the first-order expansion.

[Return to question](am01-mathematics-practice.md#section-18)

<a name="section-16"></a>

## AM01-C6

**Concept:** Partials without differentiability. **Prerequisite:** AM01 Math 3 - Differentials and Gradients (not included; [edition scope](../../SOURCES.md#pending)).

Let $\rho=\sqrt{x^2+y^2}$. The bound $|f|\leq\rho/2$ proves continuity. Since $f(h,0)=f(0,k)=0$, both partials at the origin equal zero. Differentiability would then require $f(h,k)/\sqrt{h^2+k^2}\to0$. Along $h=k>0$,
$$
f(h,h)=h/\sqrt2,\qquad
\frac{f(h,h)}{\sqrt{h^2+h^2}}=\frac12.
$$
The ratio does not tend to zero. The function is continuous and has both partial derivatives, but is not differentiable at the origin. Axis tests miss behavior in other directions.

**Common mistakes:** Inferring differentiability from two axis derivatives or from continuity; using $h^2$ instead of $\sqrt{h^2}=|h|$.

**Check:** The continuity bound and diagonal remainder ratio were checked separately.

[Return to question](am01-mathematics-practice.md#section-19)

<a name="section-17"></a>

## AM01-D1

**Concept:** Constructing an exact potential. **Prerequisite:** AM01 Math 4 - Exactness and Thermodynamics (not included; [edition scope](../../SOURCES.md#pending)).

$P_y=3x^2=Q_x$ on the simply connected plane, and both coefficients are smooth. Integrating $P$ gives $f=x^3y+x^2+C(y)$. Matching $f_y=x^3+C'(y)$ to $Q$ requires $C'=4y^3$, so $C=y^4+C_0$. The initial value fixes $C_0=5$:
$$
f=x^3y+x^2+y^4+5.
$$
Differentiating in $x$ and $y$ reproduces the two input coefficients. The constant sets the potential level and has no effect on its differential.

**Common mistakes:** Using a constant rather than $C(y)$ after integrating only in $x$; forgetting the specified base value.

**Check:** Both derivatives and the base value checked symbolically.

[Return to question](am01-mathematics-practice.md#section-21)

<a name="section-18"></a>

## AM01-D2

**Concept:** A nonexact expression and path dependence. **Prerequisite:** AM01 Math 4 - Exactness and Thermodynamics (not included; [edition scope](../../SOURCES.md#pending)).

$P_y=1$, $Q_x=2$, so the expression is not exact on any open region. Along route (i), the horizontal leg at $y=0$ gives zero and the vertical leg at $x=1$ gives $\int_0^1 2\,dy=2$. Along route (ii), the vertical leg at $x=0$ gives zero and the horizontal leg at $y=1$ gives $\int_0^1 1\,dx=1$. A single-valued potential would give the same endpoint difference for both routes. Their disagreement supplies a second independent obstruction. The loop formed by route (i) followed by the reverse of route (ii) has integral $1$.

**Common mistakes:** Counting both $dx$ and $dy$ as nonzero on every segment; adding the two routes instead of reversing one to form a loop.

**Check:** Segment integrals checked directly and compared to the cross-partial mismatch.

[Return to question](am01-mathematics-practice.md#section-22)

<a name="section-19"></a>

## AM01-D3

**Concept:** Recovering a missing coefficient. **Prerequisite:** AM01 Math 4 - Exactness and Thermodynamics (not included; [edition scope](../../SOURCES.md#pending)).

Exactness requires $2x+2ay=2x+6y$ for every $(x,y)$, hence $a=3$. At $y=0$ the equality would hold for any $a$, so a single-point check cannot establish exactness on an open set. For $a=3$,
$$
f=x^2y+3xy^2+C(y),\qquad f_y=x^2+6xy+C'(y).
$$
Thus $C'=\cos y$, giving $f=x^2y+3xy^2+\sin y+C_0$. Both partials verify the result.

**Common mistakes:** Checking only a special line and inferring an identity on the whole domain.

**Check:** Coefficient identity solved and the resulting potential differentiated independently.

[Return to question](am01-mathematics-practice.md#section-23)

<a name="section-20"></a>

## AM01-D4

**Concept:** Global obstruction survives an exact addition. **Prerequisite:** AM01 Math 4 - Exactness and Thermodynamics (not included; [edition scope](../../SOURCES.md#pending)).

The derivatives satisfy
$P_y=(y^2-x^2)/(x^2+y^2)^2=Q_x$.
On the circle the radial part $2x\dot x+2y\dot y$ is zero, whereas the angular part is $1$. Therefore $\oint\omega=2\pi$, independent of $R$. A global potential is impossible because a closed-loop endpoint difference must vanish. On $x>0$,
$$
f=x^2+y^2+\arctan(y/x)+C
$$
has exactly the required partials. The added $d(x^2+y^2)$ has zero circulation on every closed path, so it cannot cancel the angular circulation. This is a domain obstruction despite perfect local smoothness.

**Common mistakes:** Assuming any added polynomial fixes topology; writing a globally single-valued polar angle without a branch.

**Check:** Cross-partials, local potential derivatives and radius-independent circle integral checked.

[Return to question](am01-mathematics-practice.md#section-24)

<a name="section-21"></a>

## AM01-D5

**Concept:** Maxwell relation from a toy fundamental equation. **Prerequisite:** AM01 Math 4 - Exactness and Thermodynamics (not included; [edition scope](../../SOURCES.md#pending)).

Coefficient comparison gives
$$
T=\frac{2\kappa S}{V},\qquad
p=\frac{\kappa S^2}{V^2}-a.
$$
Thus
$$
\left(\frac{\partial T}{\partial V}\right)_S=-\frac{2\kappa S}{V^2}
=-\left(\frac{\partial p}{\partial S}\right)_V.
$$
Since $[S]=\mathrm{J/K}$, $[U]=\mathrm J$, $[V]=\mathrm{m^3}$, we need $[\kappa]=\mathrm{K^2m^3/J}$ and $[a]=\mathrm{J/m^3}$. The relation's two sides have units $\mathrm{K/m^3}$. Smoothness holds on $V>0$. This is a consistency check of the assumed equilibrium fundamental relation, not a measurement or complete stability analysis.

**Common mistakes:** Taking $p=U_V$; omitting the volume restriction or treating a toy equation as experimental data.

**Check:** The two mixed derivatives and units were checked independently.

[Return to question](am01-mathematics-practice.md#section-25)

<a name="section-22"></a>

## AM01-D6

**Concept:** Reconstructing internal energy from responses. **Prerequisite:** AM01 Math 4 - Exactness and Thermodynamics (not included; [edition scope](../../SOURCES.md#pending)).

The consistency test is $T_V=\beta=-p_S$, so it passes. Integrating $U_S=T$ gives $U=\alpha S^2/2+\beta SV+C(V)$. Matching $U_V=-p=-p_0+\beta S-\gamma V$ yields $C'=-p_0-\gamma V$ and
$$
U=\frac{\alpha}{2}S^2+\beta SV-p_0V-\frac{\gamma}{2}V^2+C_0.
$$
With $G(S,V)$ denoting the displayed expression without $C_0$, the uniquely normalized result is $U=U_0+G(S,V)-G(S_0,V_0)$. The coefficient of $V$ in $T$ must equal minus the coefficient of $S$ in $p$. For units, $[\alpha]=\mathrm{K^2/J}$, $[\beta]=\mathrm{K/m^3}$, $[p_0]=\mathrm{J/m^3}$, $[\gamma]=\mathrm{J/m^6}$. This guarantees differential consistency on the patch; extra thermodynamic assumptions remain separate.

**Common mistakes:** Forgetting that the coefficient of $dV$ is $-p$; treating differential consistency as proof of stability.

**Check:** Reconstructed first derivatives and the reference normalization checked symbolically.

[Return to question](am01-mathematics-practice.md#section-26)

<a name="section-23"></a>

## AM01-E1

**Concept:** Two-channel multivariable chain rule. **Prerequisite:** AM01 Math 5 - Chain Rule and Coordinate Changes (not included; [edition scope](../../SOURCES.md#pending)).

The chain rule gives $H_x=2uv+u^2$ and $H_y=2uv-u^2$. In $x,y$ variables,
$$
H_x=(x+y)(3x-y),\qquad H_y=(x+y)(x-3y).
$$
Direct differentiation of $(x+y)^2(x-y)$ gives the same expressions. The minus sign in $H_y$ records that increasing $y$ at fixed $x$ increases $u$ but decreases $v$; losing that sign changes the physical meaning of the variation.

**Common mistakes:** Using $v_y=1$; forgetting one of the two channels.

**Check:** Composed and direct differentiation checked for both inputs.

[Return to question](am01-mathematics-practice.md#section-28)

<a name="section-24"></a>

## AM01-E2

**Concept:** Held-fixed variables with explicit dependence. **Prerequisite:** AM01 Math 5 - Chain Rule and Coordinate Changes (not included; [edition scope](../../SOURCES.md#pending)).

At fixed $v$, $Z_x=e^xv^2$. Along fixed $y$,
$$
H_x=e^xv^2+(2e^xv)(2x)=e^x(v^2+4xv),\qquad v=x^2+y.
$$
At the specified point the results are $e$ and $5e$. Direct differentiation of $e^x(x^2+y)^2$ confirms the composite result. In the first experiment $v$ is held fixed; in the second $v$ changes because $x^2$ changes. The identical phrase “differentiate in $x$” does not define the same operation without its fixed-variable declaration.

**Common mistakes:** Omitting the explicit term or the indirect term; substituting $v=1$ before differentiating the composite.

**Check:** Composite and expanded routes checked symbolically.

[Return to question](am01-mathematics-practice.md#section-29)

<a name="section-25"></a>

## AM01-E3

**Concept:** Inverse map and Jacobian foundations. **Prerequisite:** AM01 Math 5 - Chain Rule and Coordinate Changes (not included; [edition scope](../../SOURCES.md#pending)).

The inverse is $x=(u+v)/2$, $y=(u-v)/2$, hence $dx=(du+dv)/2$, $dy=(du-dv)/2$. The forward Jacobian determinant is $-2$; the inverse determinant is $-1/2$, consistent with their product $1$. Substitution yields $f=(u^2+v^2)/2$. Thus $f_x=f_u u_x+f_v v_x=u+v=2x$, matching the original function. The second map has determinant zero and outputs restricted to $v=2u$; for example $(1,0)$ and $(0,1)$ have identical outputs. No inverse can recover those separate points from the same labels.

**Common mistakes:** Assuming two output names imply two independent coordinates; confusing a global inverse demonstrated by algebra with a theorem inferred only from a determinant.

**Check:** Both compositions, differential matrices and the gradient recovery checked.

[Return to question](am01-mathematics-practice.md#section-30)

<a name="section-26"></a>

## AM01-E4

**Concept:** Time-dependent coordinate map and kinetic energy. **Prerequisite:** AM01 Math 5 - Chain Rule and Coordinate Changes (not included; [edition scope](../../SOURCES.md#pending)).

Differentiating gives $\dot x=u-R\sin\theta\,\dot\theta$, $\dot y=R\cos\theta\,\dot\theta$. Therefore
$$
v^2=u^2-2uR\sin\theta\,\dot\theta+R^2\dot\theta^2,\quad
T_{\mathrm{kin}}=\frac m2\left(u^2-2uR\sin\theta\,\dot\theta+R^2\dot\theta^2\right).
$$
With $u=0$, this becomes ordinary circular kinetic energy. With $\dot\theta=0$, the bead translates with the hoop and $v^2=u^2$. The radial vector is $R(\cos\theta,\sin\theta)$; its dot product with laboratory velocity is $Ru\cos\theta$, not generally zero. Subtracting center velocity $(u,0)$ leaves a tangent vector. Every term in $v^2$ has velocity-squared units.

**Common mistakes:** Dropping the explicit-time contribution; discarding the cross term; using the fixed-hoop tangency condition in the lab frame.

**Check:** Expanded component squares, radial dot product and limiting cases checked symbolically.

[Return to question](am01-mathematics-practice.md#section-31)

<a name="section-27"></a>

## AM01-E5

**Concept:** Total time derivative versus explicit partial. **Prerequisite:** AM01 Math 5 - Chain Rule and Coordinate Changes (not included; [edition scope](../../SOURCES.md#pending)).

The total derivative is
$$
\frac{dF}{dt}=2tq\dot q+q^2+\cos t,
$$
while the explicit partial is $F_t|_q=q^2+\cos t$. With $q=t^2$ and $\dot q=2t$, the total is $5t^4+\cos t$, agreeing with differentiating $t^5+\sin t$. At $t=1$ the total is $5+\cos1$ and the fixed-$q$ partial is $1+\cos1$. The extra $4$ comes from the changing coordinate. P362's apparent $dt/dt=0$ would incorrectly erase the direct contribution; the correct value is one. No claim is made about whether the underlying audio or ASR caused that passage.

**Common mistakes:** Dropping $F_t$; confusing fixed-$q$ partial differentiation with differentiating along $q(t)$.

**Check:** Direct composition checked against the multivariable formula.

[Return to question](am01-mathematics-practice.md#section-32)

<a name="section-28"></a>

## AM01-E6

**Concept:** Moving constraint and regularity. **Prerequisite:** AM01 Math 5 - Chain Rule and Coordinate Changes (not included; [edition scope](../../SOURCES.md#pending)).

Differentiation gives $2x\dot x+2y\dot y=2R\dot R$. Therefore
$$
\mathbf v\cdot\frac{(x,y)}R=\frac{x\dot x+y\dot y}R=\dot R.
$$
The lab velocity is tangent precisely when this radial component is zero, which here means $\dot R=0$. The tangential component remains unrestricted by this kinematic condition alone. At fixed time and $R>0$, one regular equality restricts two planar coordinates to one local freedom, an angle. For $R=0$, the only real solution is $(0,0)$, an isolated point. Its gradient is zero, so the linearized equation would be $0=0$ and cannot reveal the actual restriction. This singular equation violates the regularity hypothesis; naive “two minus one” counting is invalid.

**Common mistakes:** Forgetting that $R$ depends on time; inferring that one scalar velocity relation determines the whole trajectory; subtracting constraints at singular points.

**Check:** Constraint differentiated directly, radial decomposition checked, and the zero-radius set solved independently.

[Return to question](am01-mathematics-practice.md#section-33)

[Section index](README.md) · [Home](../../README.md)
