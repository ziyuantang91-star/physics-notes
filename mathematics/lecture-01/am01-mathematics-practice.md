<a name="section-1"></a>

# AM01 — Mathematics Practice by Topic

> **Edition scope:** original AI-assisted supplement or study material. Some prerequisite lessons are withheld for source review; their titles are plain text, not unavailable links. [Attribution and scope](../../SOURCES.md#pending).


> **Review status: unverified.** AI-assisted educational draft; human scientific review remains pending. [Sources and limitations](../../SOURCES.md).


**AI SUPPLEMENT — 27 original mathematics exercises.** These are not Morin or competition problems, not claimed lecture examples, and **do not count toward the deferred 10+10 formal physics sets**. Pure mathematics examples are dimensionless unless units are specified. No attempts or mastery have been recorded.

Use one topic immediately after its lesson. Write an independent attempt before opening a hint. There are three progressive hints per question in [AM01 Progressive Hints](am01-progressive-hints.md) and complete answers in [AM01 Mathematics Solutions](am01-mathematics-solutions.md). These are separate files so opening this question sheet does not expose answers. Estimated times are planning suggestions, not deadlines.

Levels: A foundational; B explanation/derivation; C physics-related mathematics; D advanced transfer. A mixed label describes the reasoning demanded, not a rigid difficulty quota.

<a name="section-2"></a>

## Topic A — Functions and partial derivatives

Prerequisites: AP limits, power/product rules, one-variable chain rule. Lesson: AM01 Math 1 - Functions and Partial Derivatives (not included; [edition scope](../../SOURCES.md#pending)). Source connection: P037–P043; P067–P079.

<a name="section-3"></a>

### AM01-A1

**Tests:** Partial-derivative definitions. **Level:** A — foundational. **Estimate:** 10 minutes. **Prerequisites:** AP limits, power/product rules, one-variable chain rule. **Source:** AI-generated original.

For $f(x,y)=x^3y+2y^2$, derive $f_x$ from the limit definition, compute $f_y$, and evaluate both at $(1,-1)$. State which variable is fixed in each derivative.

[Optional hints](am01-progressive-hints.md#section-2) · [Open solution only after attempting](am01-mathematics-solutions.md#section-2)

<a name="section-4"></a>

### AM01-A2

**Tests:** Domain and interior derivatives. **Level:** A/B — foundational and conceptual. **Estimate:** 10 minutes. **Prerequisites:** AP limits, power/product rules, one-variable chain rule. **Source:** AI-generated original.

Let $f(x,y)=\sqrt{9-x^2-y^2}$. State its real domain, find both partials at $(1,2)$, and explain why the interior formulas do not supply a finite ordinary two-sided partial derivative at $(3,0)$.

[Optional hints](am01-progressive-hints.md#section-3) · [Open solution only after attempting](am01-mathematics-solutions.md#section-3)

<a name="section-5"></a>

### AM01-A3

**Tests:** Product and one-variable chain rules on slices. **Level:** A — calculation with meaning. **Estimate:** 8 minutes. **Prerequisites:** AP limits, power/product rules, one-variable chain rule. **Source:** AI-generated original.

Compute the two partials of $f(x,y)=e^{xy}+\sin x\cos y$. Evaluate them at $(0,\pi/2)$ and explain the different factors contributed by the exponent $xy$.

[Optional hints](am01-progressive-hints.md#section-4) · [Open solution only after attempting](am01-mathematics-solutions.md#section-4)

<a name="section-6"></a>

### AM01-A4

**Tests:** Physical meaning and derivative units. **Level:** C — accessible physics mathematics. **Estimate:** 10 minutes. **Prerequisites:** AP limits, power/product rules, one-variable chain rule. **Source:** AI-generated original.

A local temperature model is $\Theta(x,y)=\Theta_0+\alpha x^2+\beta y$, with $\Theta$ in kelvin and $x,y$ in meters. Determine the units of $\alpha,\beta,\Theta_x,\Theta_y$. Find the partials. If $\alpha>0$, explain the sign of $\Theta_x$ for $x<0$, $x=0$, and $x>0$.

[Optional hints](am01-progressive-hints.md#section-5) · [Open solution only after attempting](am01-mathematics-solutions.md#section-5)

<a name="section-7"></a>

### AM01-A5

**Tests:** Partial derivative versus derivative along a path. **Level:** B/C — conceptual transfer. **Estimate:** 12 minutes. **Prerequisites:** AP limits, power/product rules, one-variable chain rule. **Source:** AI-generated original.

For $f(x,y)=xy^2$, compare $(\partial f/\partial x)_y$ at $(1,2)$ with $d[f(x,3x-1)]/dx$ at $x=1$. Compute the latter by substitution before differentiating, and explain why the answers can differ.

[Optional hints](am01-progressive-hints.md#section-6) · [Open solution only after attempting](am01-mathematics-solutions.md#section-6)

<a name="section-8"></a>

## Topic B — Mixed partials

Prerequisites: Math 1; second derivatives; mean value theorem for B3. Lesson: AM01 Math 2 - Mixed Partials and Smoothness (not included; [edition scope](../../SOURCES.md#pending)). Source connection: P044–P051.

<a name="section-9"></a>

### AM01-B1

**Tests:** Four second partials and order notation. **Level:** A — calculation. **Estimate:** 12 minutes. **Prerequisites:** Math 1; second derivatives; mean value theorem for B3. **Source:** AI-generated original.

For $f(x,y)=x^2e^y+xy^3$, find $f_{xx},f_{xy},f_{yx},f_{yy}$ using the convention $f_{xy}=\partial_y(\partial_xf)$. Verify mixed-partial equality and state a sufficient hypothesis.

[Optional hints](am01-progressive-hints.md#section-7) · [Open solution only after attempting](am01-mathematics-solutions.md#section-7)

<a name="section-10"></a>

### AM01-B2

**Tests:** Regularity on a restricted domain. **Level:** B — mathematical reasoning. **Estimate:** 10 minutes. **Prerequisites:** Math 1; second derivatives; mean value theorem for B3. **Source:** AI-generated original.

For $g(s,v)=s^2/v$ on $v>0$, compute $\partial_v(\partial_sg)$ and $\partial_s(\partial_vg)$. Explain whether their equality authorizes evaluating the formula at $v=0$.

[Optional hints](am01-progressive-hints.md#section-8) · [Open solution only after attempting](am01-mathematics-solutions.md#section-8)

<a name="section-11"></a>

### AM01-B3

**Tests:** Reconstructing the mixed-partial theorem. **Level:** B — proof. **Estimate:** 18 minutes. **Prerequisites:** Math 1; second derivatives; mean value theorem for B3. **Source:** AI-generated original.

Assume $f\in C^2$ near $(a,b)$. Starting from the rectangular difference $R=f(a+h,b+k)-f(a,b+k)-f(a+h,b)+f(a,b)$, reconstruct a proof that $f_{xy}(a,b)=f_{yx}(a,b)$. Identify precisely which step uses continuity.

[Optional hints](am01-progressive-hints.md#section-9) · [Open solution only after attempting](am01-mathematics-solutions.md#section-9)

<a name="section-12"></a>

### AM01-B4

**Tests:** Counterexample using limit definitions. **Level:** D — advanced transfer. **Estimate:** 20 minutes. **Prerequisites:** Math 1; second derivatives; mean value theorem for B3. **Source:** AI-generated original.

Define $f(x,y)=xy(x^2-4y^2)/(x^2+y^2)$ away from the origin and $f(0,0)=0$. Show that $f$ is continuous at the origin. Then compute $f_x(0,y)$, $f_y(x,0)$ and both mixed partials at the origin from definitions. Explain the result.

[Optional hints](am01-progressive-hints.md#section-10) · [Open solution only after attempting](am01-mathematics-solutions.md#section-10)

<a name="section-13"></a>

## Topic C — Differentials and gradients

Prerequisites: Math 1–3; linear approximation; elementary vector components. Lesson: AM01 Math 3 - Differentials and Gradients (not included; [edition scope](../../SOURCES.md#pending)). Source connection: P052–P057; connection P315–P324.

<a name="section-14"></a>

### AM01-C1

**Tests:** Differential versus exact finite change. **Level:** A/B — approximation. **Estimate:** 12 minutes. **Prerequisites:** Math 1–3; linear approximation; elementary vector components. **Source:** AI-generated original.

For $f(x,y)=xy+y^2$, use $(a,b)=(2,1)$ and increments $h=0.01$, $k=-0.02$. Compute $df$, the exact $\Delta f$, and the remainder. Explain how that remainder changes when both increments are halved.

[Optional hints](am01-progressive-hints.md#section-11) · [Open solution only after attempting](am01-mathematics-solutions.md#section-11)

<a name="section-15"></a>

### AM01-C2

**Tests:** Gradient and a directional derivative. **Level:** B — geometric reasoning. **Estimate:** 12 minutes. **Prerequisites:** Math 1–3; linear approximation; elementary vector components. **Source:** AI-generated original.

For $f(x,y)=\log(x^2+y^2)$, compute the gradient at $(3,4)$ and the directional derivative along $\mathbf u=(4,-3)/5$. Explain geometrically why that result is possible even though the gradient is nonzero. State the domain.

[Optional hints](am01-progressive-hints.md#section-12) · [Open solution only after attempting](am01-mathematics-solutions.md#section-12)

<a name="section-16"></a>

### AM01-C3

**Tests:** Dot product, angle and projection. **Level:** A/B — vector foundation. **Estimate:** 12 minutes. **Prerequisites:** Math 1–3; linear approximation; elementary vector components. **Source:** AI-generated original.

Let $\mathbf a=(2,-1)$ and $\mathbf b=(1,3)$. Compute their dot product, lengths, and the cosine of the angle between them. Find the signed component of $\mathbf a$ along the unit direction of $\mathbf b$, defining what “signed component” means.

[Optional hints](am01-progressive-hints.md#section-13) · [Open solution only after attempting](am01-mathematics-solutions.md#section-13)

<a name="section-17"></a>

### AM01-C4

**Tests:** Energy gradients and power. **Level:** C — physics-related mathematics. **Estimate:** 15 minutes. **Prerequisites:** Math 1–3; linear approximation; elementary vector components. **Source:** AI-generated original.

A conservative planar force has potential $V(x,y)=\alpha xy+\beta x^2$, with $x,y$ lengths and constants $\alpha,\beta$ in $\mathrm{J/m^2}$. Find $\mathbf F$. Along the prescribed path $x=vt$, $y=b$, for constant $v,b$, calculate $dV/dt$ directly and check $dV/dt=-\mathbf F\cdot\mathbf v$. Is the path being claimed to solve the unconstrained dynamics?

[Optional hints](am01-progressive-hints.md#section-14) · [Open solution only after attempting](am01-mathematics-solutions.md#section-14)

<a name="section-18"></a>

### AM01-C5

**Tests:** Differentials and uncertainty sensitivity. **Level:** C/D — applied approximation. **Estimate:** 15 minutes. **Prerequisites:** Math 1–3; linear approximation; elementary vector components. **Source:** AI-generated original.

Take the small-amplitude pendulum formula $P=2\pi\sqrt{\ell/g}$ as given, with $\ell,g>0$. Derive $dP/P$ in terms of $d\ell/\ell$ and $dg/g$. If the magnitudes of relative input errors are bounded by $1\%$ and $0.4\%$, estimate a first-order worst-case relative period error. Explain why this is not a statistical standard deviation or an exact bound for arbitrary finite errors.

[Optional hints](am01-progressive-hints.md#section-15) · [Open solution only after attempting](am01-mathematics-solutions.md#section-15)

<a name="section-19"></a>

### AM01-C6

**Tests:** Partials without differentiability. **Level:** D — conceptual counterexample. **Estimate:** 20 minutes. **Prerequisites:** Math 1–3; linear approximation; elementary vector components. **Source:** AI-generated original.

Define $f(x,y)=xy/\sqrt{x^2+y^2}$ off the origin and $f(0,0)=0$. Prove continuity at the origin, find both partials there, and decide whether $f$ is differentiable there using the remainder definition. Use the path $x=y=h>0$ if helpful.

[Optional hints](am01-progressive-hints.md#section-16) · [Open solution only after attempting](am01-mathematics-solutions.md#section-16)

<a name="section-20"></a>

## Topic D — Exactness and thermodynamics

Prerequisites: Math 1–4; single-variable integration; curve chain rule. Lesson: AM01 Math 4 - Exactness and Thermodynamics (not included; [edition scope](../../SOURCES.md#pending)). Source connection: P055–P066.

<a name="section-21"></a>

### AM01-D1

**Tests:** Constructing an exact potential. **Level:** B — derivation and calculation. **Estimate:** 15 minutes. **Prerequisites:** Math 1–4; single-variable integration; curve chain rule. **Source:** AI-generated original.

On $\mathbb R^2$, test the expression $(3x^2y+2x)\,dx+(x^3+4y^3)\,dy$ for exactness. Construct $f$ such that its differential is this expression and $f(0,0)=5$. Check both partials.

[Optional hints](am01-progressive-hints.md#section-17) · [Open solution only after attempting](am01-mathematics-solutions.md#section-17)

<a name="section-22"></a>

### AM01-D2

**Tests:** A nonexact expression and path dependence. **Level:** B/C — conceptual application. **Estimate:** 15 minutes. **Prerequisites:** Math 1–4; single-variable integration; curve chain rule. **Source:** AI-generated original.

Consider $\omega=y\,dx+2x\,dy$. Test exactness. Compute its integral from $(0,0)$ to $(1,1)$ along (i) a horizontal segment followed by a vertical segment and (ii) a vertical segment followed by a horizontal segment. Interpret the disagreement.

[Optional hints](am01-progressive-hints.md#section-18) · [Open solution only after attempting](am01-mathematics-solutions.md#section-18)

<a name="section-23"></a>

### AM01-D3

**Tests:** Recovering a missing coefficient. **Level:** B/D — inverse problem. **Estimate:** 15 minutes. **Prerequisites:** Math 1–4; single-variable integration; curve chain rule. **Source:** AI-generated original.

For which real constant $a$ is $(2xy+ay^2)\,dx+(x^2+6xy+\cos y)\,dy$ exact on the plane? Find a potential for that value and explain why your condition must hold for every $y$, not merely at $y=0$.

[Optional hints](am01-progressive-hints.md#section-19) · [Open solution only after attempting](am01-mathematics-solutions.md#section-19)

<a name="section-24"></a>

### AM01-D4

**Tests:** Global obstruction survives an exact addition. **Level:** D — topology and transfer. **Estimate:** 22 minutes. **Prerequisites:** Math 1–4; single-variable integration; curve chain rule. **Source:** AI-generated original.

On $D=\mathbb R^2\setminus\{0\}$, consider
$\omega=(2x-y/(x^2+y^2))\,dx+(2y+x/(x^2+y^2))\,dy$.
Check the cross-partials; integrate around a counterclockwise circle of radius $R>0$; decide if a global potential exists. Find a potential on $x>0$ and explain why adding the $2x,2y$ terms does not remove the obstruction.

[Optional hints](am01-progressive-hints.md#section-20) · [Open solution only after attempting](am01-mathematics-solutions.md#section-20)

<a name="section-25"></a>

### AM01-D5

**Tests:** Maxwell relation from a toy fundamental equation. **Level:** C — thermodynamic mathematics. **Estimate:** 18 minutes. **Prerequisites:** Math 1–4; single-variable integration; curve chain rule. **Source:** AI-generated original.

Let $U(S,V)=\kappa S^2/V+aV$ on a local equilibrium model with $S,V>0$, $\kappa>0$ and constants with consistent units. Using $dU=T\,dS-p\,dV$, determine $T,p$, the units of $\kappa,a$, and verify the Maxwell relation including fixed-variable subscripts. Do not infer a real substance or global stability from this algebra.

[Optional hints](am01-progressive-hints.md#section-21) · [Open solution only after attempting](am01-mathematics-solutions.md#section-21)

<a name="section-26"></a>

### AM01-D6

**Tests:** Reconstructing internal energy from responses. **Level:** D — synthesis. **Estimate:** 25 minutes. **Prerequisites:** Math 1–4; single-variable integration; curve chain rule. **Source:** AI-generated original.

In a local $(S,V)$ patch, suppose $T=\alpha S+\beta V$ and $p=p_0-\beta S+\gamma V$, with constant coefficients of appropriate units. Test consistency with $dU=T\,dS-p\,dV$ and reconstruct $U$ subject to $U(S_0,V_0)=U_0$. Identify the shared coefficient that the Maxwell relation constrains. Assume a patch with $T>0$; do not claim this specifies all stability conditions.

[Optional hints](am01-progressive-hints.md#section-22) · [Open solution only after attempting](am01-mathematics-solutions.md#section-22)

<a name="section-27"></a>

## Topic E — Chain rule and coordinate changes

Prerequisites: Math 1–5; trigonometry; product and chain rules. Lesson: AM01 Math 5 - Chain Rule and Coordinate Changes (not included; [edition scope](../../SOURCES.md#pending)). Source connection: P067–P080; bridge P081–P095.

<a name="section-28"></a>

### AM01-E1

**Tests:** Two-channel multivariable chain rule. **Level:** B — derivation and calculation. **Estimate:** 15 minutes. **Prerequisites:** Math 1–5; trigonometry; product and chain rules. **Source:** AI-generated original.

Let $Z(u,v)=u^2v$, $u=x+y$, $v=x-y$. Find $H_x|_y$ and $H_y|_x$ for $H=Z(u(x,y),v(x,y))$ by the chain rule, then verify by substitution and direct differentiation.

[Optional hints](am01-progressive-hints.md#section-23) · [Open solution only after attempting](am01-mathematics-solutions.md#section-23)

<a name="section-29"></a>

### AM01-E2

**Tests:** Held-fixed variables with explicit dependence. **Level:** B/D — conceptual transfer. **Estimate:** 18 minutes. **Prerequisites:** Math 1–5; trigonometry; product and chain rules. **Source:** AI-generated original.

Let $Z(x,v)=e^xv^2$ and $v=x^2+y$. Compute $(\partial Z/\partial x)_v$ and $(\partial H/\partial x)_y$ for $H(x,y)=Z(x,x^2+y)$. Evaluate both at $x=1,y=0$ and explain the difference.

[Optional hints](am01-progressive-hints.md#section-24) · [Open solution only after attempting](am01-mathematics-solutions.md#section-24)

<a name="section-30"></a>

### AM01-E3

**Tests:** Inverse map and Jacobian foundations. **Level:** B/D — coordinate reasoning. **Estimate:** 20 minutes. **Prerequisites:** Math 1–5; trigonometry; product and chain rules. **Source:** AI-generated original.

For $u=x+y$, $v=x-y$, find the inverse map, its differential equations, and both Jacobian determinants. Rewrite $f=x^2+y^2$ in terms of $u,v$, then recover $f_x$ by the chain rule. Contrast with the map $u=x+y$, $v=2x+2y$: why is it not a valid independent relabeling of a planar neighborhood?

[Optional hints](am01-progressive-hints.md#section-25) · [Open solution only after attempting](am01-mathematics-solutions.md#section-25)

<a name="section-31"></a>

### AM01-E4

**Tests:** Time-dependent coordinate map and kinetic energy. **Level:** C/D — physics application. **Estimate:** 25 minutes. **Prerequisites:** Math 1–5; trigonometry; product and chain rules. **Source:** AI-generated original.

A bead moves on a hoop of fixed radius $R>0$ whose center translates horizontally at constant speed $u$. With $x(t)=ut+R\cos\theta(t)$, $y(t)=R\sin\theta(t)$, derive $\dot x,\dot y$, $v^2$, and kinetic energy for constant mass $m$. Check the limits $u=0$ and $\dot\theta=0$. Is the laboratory velocity necessarily tangent to a circle centered at the hoop center at that instant?

[Optional hints](am01-progressive-hints.md#section-26) · [Open solution only after attempting](am01-mathematics-solutions.md#section-26)

<a name="section-32"></a>

### AM01-E5

**Tests:** Total time derivative versus explicit partial. **Level:** B/C — source-error diagnosis. **Estimate:** 15 minutes. **Prerequisites:** Math 1–5; trigonometry; product and chain rules. **Source:** AI-generated original.

For $F(q,t)=tq^2+\sin t$, derive $dF(q(t),t)/dt$ and compare it with $(\partial F/\partial t)_q$. Then set $q(t)=t^2$ and verify by direct composition. In the nondimensional mathematical example, evaluate at $t=1$. Explain the relevance to P362.

[Optional hints](am01-progressive-hints.md#section-27) · [Open solution only after attempting](am01-mathematics-solutions.md#section-27)

<a name="section-33"></a>

### AM01-E6

**Tests:** Moving constraint and regularity. **Level:** C/D — bridge to the next unit. **Estimate:** 25 minutes. **Prerequisites:** Math 1–5; trigonometry; product and chain rules. **Source:** AI-generated original.

A planar point satisfies $x(t)^2+y(t)^2=R(t)^2$, where $R(t)>0$ is known and differentiable. Derive the velocity condition. Express the radial velocity $\mathbf v\cdot(x,y)/R$ and explain when the motion is tangent to the instantaneous circle. At a fixed time, how many independent configuration coordinates remain? Explain why you cannot extend the same regular constraint-counting argument to the equation $x^2+y^2=0$.

[Optional hints](am01-progressive-hints.md#section-28) · [Open solution only after attempting](am01-mathematics-solutions.md#section-28)

[Section index](README.md) · [Home](../../README.md)
