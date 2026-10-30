<a name="section-1"></a>

# AM02 Math C — Curl, Circulation and Gauge

> **Edition scope:** original AI-assisted supplement or study material. Some prerequisite lessons are withheld for source review; their titles are plain text, not unavailable links. [Attribution and scope](../../SOURCES.md#pending).


> **Review status: unverified.** AI-assisted educational draft; human scientific review remains pending. [Sources and limitations](../../SOURCES.md).


**AI SUPPLEMENT**, needed for P358–P381 and Unit 02.7. Reuse AM01 Math 2 - Mixed Partials and Smoothness (not included; [edition scope](../../SOURCES.md#pending)) and AM01 Math 4 - Exactness and Thermodynamics (not included; [edition scope](../../SOURCES.md#pending)). We develop the circulation calculation actually needed, rather than assume a full vector-calculus course.

<a name="section-2"></a>

## 1. A line integral is a one-variable integral along a path

For a differentiable path $\mathbf r(s)$, $s_0\le s\le s_1$, define
$$
\int_C\mathbf A\cdot d\mathbf r=\int_{s_0}^{s_1}\mathbf A(\mathbf r(s))\cdot\mathbf r'(s)\,ds.
$$
The dot product selects the component along the infinitesimal displacement. Reversing orientation changes sign. A circle of radius $a$, traversed counterclockwise viewed from $+z$, has $\mathbf r(\theta)=(a\cos\theta,a\sin\theta,0)$ and $d\mathbf r=a\mathbf e_\theta d\theta$. For $\mathbf A=Ba\mathbf e_\theta/2$ on that circle, the integral is $B\pi a^2$.

<a name="section-3"></a>

## 2. Curl is local circulation per oriented area

Take a small rectangle in the $xy$ plane, counterclockwise viewed from $+z$. Contributions of the horizontal edges differ by $-\partial_y A_x\,dx\,dy$ to leading order. Contributions of the vertical edges differ by $+\partial_x A_y\,dx\,dy$. Hence
$$
\oint\mathbf A\cdot d\mathbf r=(\partial_xA_y-\partial_yA_x)dx\,dy+\text{higher-order terms}.
$$
Define the three components by analogous oriented rectangles:
$$
\nabla\times\mathbf A=(\partial_yA_z-\partial_zA_y,\ \partial_zA_x-\partial_xA_z,\ \partial_xA_y-\partial_yA_x).
$$
This gives $\mathbf B$ in electromagnetism. $\mathbf B$ has units T when $\mathbf A$ has T m. A curl-free field has zero local circulation; global topology can still matter on a punctured domain.

For a finite planar rectangle $[a,b]\times[c,d]$, the fundamental theorem of calculus gives exactly
$$
\oint\mathbf A\cdot d\mathbf r
=\int_a^b\!\int_c^d(\partial_xA_y-\partial_yA_x)\,dy\,dx.
$$
One can verify this by integrating each partial derivative and collecting the four boundary integrals. For a smooth region tiled by small rectangles, shared edges cancel with opposite orientations, leaving the outer boundary. The limiting area integral gives the planar version of Stokes' theorem under appropriate smoothness. This is a derivation of the planar case used here, not a proof of the full theorem on arbitrary curved surfaces. For the uniform-$B$ circle, direct parameter integration and area $\pi a^2$ already suffice.

<a name="section-4"></a>

## 3. Why gradients have zero curl

For a $C^2$ scalar $\chi$, the $z$ component of $\nabla\times\nabla\chi$ is $\partial_x\partial_y\chi-\partial_y\partial_x\chi=0$. The other two vanish identically by the same mixed-partial theorem. Along a path, the chain rule gives
$$
\int_C\nabla\chi\cdot d\mathbf r=\chi(\mathbf r_1)-\chi(\mathbf r_0)
$$
when $\chi$ is single-valued on the path; closed-path circulation is zero. Thus $\mathbf A\mapsto\mathbf A+\nabla\chi$ leaves the magnetic field and closed circulation unchanged. Smoothness and domain assumptions are part of the claim.

For time-dependent $\chi$, changing only $\mathbf A$ would change $\mathbf E$. Simultaneously set $\phi'=\phi-\chi_t$. Then
$$
-\nabla\phi'-\partial_t\mathbf A'=-\nabla\phi+\nabla\chi_t-\partial_t\mathbf A-\partial_t\nabla\chi=\mathbf E.
$$
Commuting derivatives is justified by $C^2$ regularity. This is a mathematical gauge transformation, not a physical field change.

<a name="section-5"></a>

## 4. Worked potentials and a limit of the method

The symmetric gauge $\mathbf A_S=(-By/2,Bx/2,0)$ and Landau gauge $\mathbf A_L=(0,Bx,0)$ have the same curl $(0,0,B)$. Their difference is $(By/2,Bx/2,0)=\nabla(Bxy/2)$. The magnetic coupling difference is $qB(y\dot x+x\dot y)/2=q\,d(Bxy/2)/dt$; equivalence of equations follows directly from Lecture 01.

By contrast $\mathbf A=(-y,x,0)$ is not the gradient of a smooth scalar on an open planar region because its curl is $2\mathbf e_z$, whereas any such gradient has zero curl. Therefore the velocity-linear term $q\mathbf A\cdot\mathbf v$ cannot be discarded as a total derivative on that region. In one coordinate any smooth $A(q)\dot q$ is locally removable; multiple independent coordinates introduce this new obstruction.

**Independent check:** explain why equality of curl does not fix a unique vector potential. Attempt M09–M12 in [AM02 Additional Mathematics Practice](am02-additional-mathematics-practice.md), then use [hints](am02-additional-mathematics-hints.md) and [solutions](am02-additional-mathematics-solutions.md).

环流 — circulation; 磁通量 — magnetic flux; 旋度 — curl; 单值函数 — single-valued function; 规范 — gauge.

[Section index](README.md) · [Home](../../README.md)
