<a name="section-1"></a>

# Morin — Laws, Applications and Mathematical Techniques

> **Edition scope:** original AI-assisted supplement or study material. Some prerequisite lessons are withheld for source review; their titles are plain text, not unavailable links. [Attribution and scope](../SOURCES.md#pending).


> **Review status: unverified.** AI-assisted educational draft; human scientific review remains pending. [Sources and limitations](../SOURCES.md).


> **AI synthesis with source anchors**
> The source headings and page starts come from the verified whole-book index. The summaries and optional mathematical bridges below are AI explanations, not a claim that every later derivation has been taught or approved. **Study focus:** Chapter 2, with Chapter 1 as optional reference.

[Bibliographic source](../SOURCES.md#morin) · [Conceptual network](morin-conceptual-network.md) · [Prerequisite map](morin-mathematical-prerequisites.md) · [Current chapter](README.md)

<a name="section-2"></a>

## Physical laws and applications

| Law or modeling principle | Source anchor, printed / PDF | Typical application | Assumption or limitation |
| --- | --- | --- | --- |
| Static force balance and contact laws | §2.1, 22 / 40 | Suspensions, frictional contacts, ropes | Zero acceleration is not alone proof of rest; contact laws restrict reactions |
| Static moment balance | §2.2, 27 / 45 | Supports, levers, ladders, tipping | Use the same origin for all moments; distinguish pins and clamps |
| Newtonian dynamics | §3.1, 51 / 70 | Equations of motion | Inertial-frame formulation; system and mass accounting must be explicit |
| Linear restoring-force model | §4.2, 105 / 124 | Harmonic motion and spring models | Linear response and small-deformation domain |
| Energy conservation and work | §5.1, 138 / 157 | Speed changes and turning points | Distinguish mechanical energy from total energy and account for external/dissipative work |
| Newtonian gravitation | §5.4, 152 / 171 | Orbits and gravitational fields | Point masses or suitable symmetry reductions; not uniform at arbitrary scales |
| Momentum balance/conservation | §5.5, 156 / 175 | Collisions, recoil, variable-mass accounting | Closed-system conservation and open-system balance are different statements |
| Euler–Lagrange equations | §6.1, 218 / 237 | Constrained and generalized-coordinate dynamics | Requires an appropriate Lagrangian and treatment of nonconservative forces |
| Stationary action and symmetry | §§6.2, 6.6, 221, 236 / 240, 255 | Alternative formulation and conserved quantities | Stationary does not mean globally minimal |
| Central-force angular momentum | §7.1, 281 / 300 | Planar orbital motion | Torque about the force center vanishes; choice of origin matters |
| Rotational torque and angular momentum | §8.4, 322 / 341 | Extended-body rotation | A general vector treatment differs from a scalar fixed-axis model |
| Inertia tensor and principal axes | §§9.2–9.3, 376, 383 / 395, 402 | Three-dimensional rigid-body dynamics | Angular velocity and angular momentum need not be parallel |
| Forces in accelerating frames | §10.2, 460 / 479 | Translating/rotating observers | Add terms appropriate to the frame; fictitious forces are not new interactions |
| Lorentz transformations and invariant interval | §§11.4, 11.6, 523, 533 / 542, 552 | Comparing events and clocks | Define events, frames and simultaneity consistently |
| Relativistic energy and momentum | §12.1, 584 / 603 | High-speed collisions and decays | Newtonian expressions are limiting approximations |
| Four-vector covariance | §§13.1–13.3, 634–637 / 653–656 | Frame-independent organization of physical laws | Spacetime's invariant form is not an ordinary Euclidean norm |
| Equivalence principle and proper-time reasoning | §§14.1, 14.4, 649, 656 / 668, 675 | Introductory gravity/clock problems | Local equivalence does not remove tidal effects over a finite region |

Use the [index](../SOURCES.md#morin) for clickable exact PDF destinations. These are navigation-level summaries, not substitute chapter lessons.

<a name="section-3"></a>

## Mathematical technique index

| Technique | What it helps you do | Source starting points |
| --- | --- | --- |
| Dimensional consistency | Reject incompatible relations and identify parameter groups | §1.2, p. 4/PDF 22 |
| Limits and expansions | Test domains and approximate controlled regimes | §1.3, p. 7/PDF 25; A.1, p. 675/PDF 694 |
| Numerical initial-value evolution | Approximate trajectories and assess step-size effects | §1.4, p. 11/PDF 29 |
| Projections and dot products | Resolve forces and scalar work | §2.1; B.1, p. 679/PDF 698 |
| Cross products and moment arms | Track torque direction and magnitude | §2.2; B.2, p. 681/PDF 700 |
| Independent linear equations | Separate determined, redundant and underdetermined constraints | §1.1; Problem 2.13, p. 33/PDF 51 |
| Differential elements and boundary conditions | Model distributed tension or mass | §2.1 pp. 26–27/PDF 44–45; §3.3, p. 60/PDF 79 |
| Integration of moments | Locate a resultant or center of mass | §2.2 p. 28/PDF 46; §8.3, p. 318/PDF 337 |
| Separable and linear ODEs | Solve motion laws under stated conditions | §3.3; §4.1, p. 101/PDF 120 |
| Normal modes and eigenvectors | Simplify coupled oscillations | §4.5, p. 115/PDF 134; Appendix E, p. 696/PDF 715 |
| Partial versus total derivatives | Track multivariable dependencies and paths | B.3, p. 682/PDF 701; §6.1 |
| Gradient, divergence and curl | Describe spatial fields and conservative-force conditions | B.4–B.6, pp. 684–689/PDF 703–708; §5.3, p. 148/PDF 167 |
| Variations and stationary functionals | Derive dynamical equations from an action | §6.2, p. 221/PDF 240 |
| Polar coordinates and conic geometry | Use symmetry in central-force problems | §3.5, p. 68/PDF 87; §7.4, p. 287/PDF 306 |
| Tensor/matrix diagonalization | Choose principal axes of a rigid body | §§9.2–9.3; Appendices D/E |
| Linear spacetime transformations and hyperbolic functions | Relate frames and compose boosts | §§11.4, 11.9, pp. 523, 543/PDF 542, 562 |

<a name="section-4"></a>

## Optional calculus bridge

These are short tools for the selected problems, not a requirement to complete Chapter 1. For a smooth graph $y(x)$, a small displacement satisfies $ds^2=dx^2+dy^2$, so $ds=\sqrt{1+y'^2}\,dx$ when $x$ increases. A line density $\lambda$ then gives $dm=\lambda ds$. Check what “per unit length” refers to before integrating.

For a parameter-dependent integral $J(a)=\int_a^\infty f(x,a)dx$ with sufficient convergence and differentiability,
$$J'(a)=-f(a,a)+\int_a^\infty\frac{\partial f}{\partial a}(x,a)dx.$$
The first term accounts for the changing lower limit; the second for changes throughout the integrand. Differentiating can lose a constant constraint, so verify a candidate solution in the original integral. This is a method explanation, not a substitution of the values from the assigned stick problem.

Hyperbolic functions are defined by $\cosh z=(e^z+e^{-z})/2$ and $\sinh z=(e^z-e^{-z})/2$. Thus $\cosh^2z-\sinh^2z=1$, $d\cosh z/dz=\sinh z$ and $d\sinh z/dz=\cosh z$. Their arguments must be dimensionless. A numerical root is evidence only when its residual, domain and uniqueness or branch selection are checked.

<a name="section-5"></a>

## Optional elasticity and stability bridge

An ideal linear spring has restoring force $-kx$ and potential $kx^2/2$ relative to its unstretched state. A compression-only support can instead be modeled by $R=k\delta$ when $\delta\ge0$, and $R=0$ when the body separates. Solve an assumed active-contact system and then test every reaction and gap; a negative contact force invalidates that active set.

In one coordinate $q$ with positive constant inertia parameter $I_q$, an equilibrium satisfies $U'(q_0)=0$. Expanding the force $-U'(q)$ near $q_0$ gives $I_q\ddot\eta\approx-U''(q_0)\eta$, where $\eta=q-q_0$. Positive curvature gives small harmonic oscillations with $\omega^2=U''(q_0)/I_q$; negative curvature gives local instability. Zero curvature requires higher-order analysis. This generic bridge supplies future mathematics without giving a specific assignment's equilibrium result.

<a name="section-6"></a>

## Optional frames and circular motion bridge

In a nonrotating frame accelerating with $\mathbf A$, relative acceleration satisfies $m\mathbf a_{\rm rel}=\sum\mathbf F_{\rm real}-m\mathbf A$. A body stationary relative to that frame has zero relative acceleration, but generally nonzero inertial-frame acceleration. State which equation you are using.

For uniform circular motion of radius $r$ and angular speed $\Omega$, speed is $\Omega r$ and inward acceleration is $\Omega^2r$. A rotating distributed object has different local accelerations at different radii. Integrate force over the actual subsystem; a stationary shape in rotating coordinates is not inertial-frame statics. Chapter 10 supplies the full rotating-frame formulation later.

<a name="section-7"></a>

## Optional inference and uncertainty bridge

Equilibrium often constrains integrals of a distribution. One total-force measurement does not ordinarily determine the full function that produced it. If two physically different models predict the same observed data, those data alone do not identify which model is correct. This connects directly to [scientific review-writing evidence assessment](../scientific-writing/review-writing-lesson-1-from-question-to-evidence.md).

First-order uncertainty propagation uses derivatives of a specified measurement model and a covariance assumption. It does not validate the model itself, and independent inputs cannot be assumed when systematic calibration errors are shared. Ask for a focused derivation rather than treating the formula as an automatic label of reliability.

Human scientific review: pending. Detailed future chapter notes have not been generated.

[Section index](README.md) · [Home](../README.md)
