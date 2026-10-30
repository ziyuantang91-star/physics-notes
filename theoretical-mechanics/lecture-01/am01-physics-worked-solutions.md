<a name="section-1"></a>

# Physics practice — Worked Solutions

> **Edition scope:** original AI-assisted supplement or study material. Some prerequisite lessons are withheld for source review; their titles are plain text, not unavailable links. This file is an excerpt: the retained question IDs and their full calculations are unchanged. [Attribution and scope](../../SOURCES.md#pending).


> **Review status: unverified.** AI-assisted educational draft; human scientific review remains pending. [Sources and limitations](../../SOURCES.md).


**Spoiler boundary:** open this note only when ready to inspect solutions. These are AI-generated worked solutions with separately recorded computational or alternative-derivation checks, not independent human scientific approval. Each problem remains in `status: unverified`.

<a name="section-12"></a>

## AM01-M01

**Rolling, a spring and the feasibility of static friction** · [Problem](am01-mixed-physics-practice.md#section-3)

The integrable constraint gives $\dot\theta=\dot x/R$. Thus
$$T=\tfrac12\left(m+\frac I{R^2}\right)\dot x^2,\qquad V=\tfrac12kx^2-mgx\sin\alpha.$$
Set $M_e=m+I/R^2$. The ideal rolling equation is
$$M_e\ddot x=mg\sin\alpha-kx,\qquad a=\frac{mg\sin\alpha-kx}{M_e}.$$
Translational Newton gives $ma=mg\sin\alpha-kx-f$, so
$$f=\frac I{R^2}a=\frac{I/R^2}{m+I/R^2}(mg\sin\alpha-kx).$$
The independent rotational equation $I(a/R)=fR$ agrees. If the spring dominates and $a<0$, then $f<0$: friction points downhill. Static friction opposes the impending slip tendency, not necessarily the center's velocity.

The normal force is $N=mg\cos\alpha$, since the straight incline is fixed and all other stated forces are along it. The local consistency condition is
$$|f|\le\mu_smg\cos\alpha.$$
If this fails, the no-slip constraint and reduced kinetic energy cannot be retained; sliding friction and an independent spin variable are needed. For ideal rolling on a fixed surface, the contact point's instantaneous velocity vanishes, so frictional power is zero even when $f\ne0$. Equivalently its translational power $-f\dot x$ and rotational power $fR\dot\theta$ cancel. Energy differentiation yields $\dot E=\dot x[M_e\ddot x+kx-mg\sin\alpha]=0$. For $I\to0$, $f\to0$ and the equation approaches a point mass under the same along-track forces.

**Independent check:** Translational and rotational Newton equations independently recover the same acceleration and friction; mechanical-energy balance and the $I\to0$ limit also agree.

**Common mistakes:** Assuming static friction always points uphill or opposite center velocity; using no-slip motion without checking the friction bound; omitting rotational kinetic energy.

**Review prerequisites:** AM01 Physics 1 - Constraints and Integrability (not included; [edition scope](../../SOURCES.md#pending)) · AM01 Physics 4 - DAlembert and the Kinetic Energy Equations (not included; [edition scope](../../SOURCES.md#pending)) · AM01 Physics 7 - Atwood Machine (not included; [edition scope](../../SOURCES.md#pending))

<a name="section-13"></a>

## AM01-M02

**An expanding vertical hoop and actuator power** · [Problem](am01-mixed-physics-practice.md#section-4)

Differentiating the map gives $\mathbf v=\dot R\mathbf e_r+R\dot\theta\mathbf e_\theta$, with $\mathbf e_r=(\sin\theta,-\cos\theta)$ and $\mathbf e_\theta=(\cos\theta,\sin\theta)$. Hence
$$L=\tfrac12m(\dot R^2+R^2\dot\theta^2)+mgR\cos\theta.$$
Since $L_{\dot\theta}=mR^2\dot\theta$ and $L_\theta=-mgR\sin\theta$,
$$R^2\ddot\theta+2R\dot R\dot\theta+gR\sin\theta=0.$$
The $2R\dot R\dot\theta$ term is essential. It also follows from tangential acceleration $R\ddot\theta+2\dot R\dot\theta$ under tangential gravity $-g\sin\theta$.

Let the outward reaction be $N\mathbf e_r$. Radial Newton gives $m(\ddot R-R\dot\theta^2)=mg\cos\theta+N$, so
$$N=m(\ddot R-R\dot\theta^2)-mg\cos\theta.$$
Virtual displacement $R\mathbf e_\theta\delta\theta$ is perpendicular to the reaction, yet actual power is $P_N=N\dot R$. Physical energy is
$$E=\tfrac12m(\dot R^2+R^2\dot\theta^2)-mgR\cos\theta.$$
Its time derivative is
$$m\dot R\ddot R+mR\dot R\dot\theta^2+mR^2\dot\theta\ddot\theta-mg\dot R\cos\theta+mgR\sin\theta\dot\theta.$$
Substitute the angular equation into the third term. The angular-gravity terms cancel, leaving $m\dot R\ddot R-mR\dot R\dot\theta^2-mg\dot R\cos\theta=N\dot R$.

The reduced generalized energy is instead
$$E_L=\dot\theta L_{\dot\theta}-L=\tfrac12mR^2\dot\theta^2-\tfrac12m\dot R^2-mgR\cos\theta.$$
Thus $E-E_L=m\dot R^2$. The prescribed radius is not varied in this one-coordinate system; its actuator can exchange energy. For constant $R$, the difference vanishes, support power is zero and the ordinary fixed-hoop energy is conserved. An inward signed reaction $N<0$ is normal for a rapidly moving bead; it is not an inconsistency for a threaded hoop.

**Independent check:** Both radial and tangential Newton projections are checked against the derived expressions, and direct mechanical-energy differentiation gives exactly the actuator power.

**Common mistakes:** Omitting the radial speed from kinetic energy; treating $R$ as both prescribed and independent; identifying reduced generalized energy with physical energy; rejecting inward reaction in a bilateral threaded model.

**Review prerequisites:** AM01 Physics 3 - Virtual Displacements and Ideal Constraints (not included; [edition scope](../../SOURCES.md#pending)) · AM01 Physics 4 - DAlembert and the Kinetic Energy Equations (not included; [edition scope](../../SOURCES.md#pending)) · AM01 Physics 5 - Lagrangians and Generalized Potentials (not included; [edition scope](../../SOURCES.md#pending))

<a name="section-14"></a>

## AM01-M03

**A vertically driven pendulum and effective gravity** · [Problem](am01-mixed-physics-practice.md#section-5)

The velocity is $(\ell\cos\theta\dot\theta,\dot a+\ell\sin\theta\dot\theta)$. Thus
$$L=\tfrac12m\ell^2\dot\theta^2+m\ell\dot a\sin\theta\dot\theta+\tfrac12m\dot a^2-mga+mg\ell\cos\theta.$$
Its velocity derivative is $m\ell^2\dot\theta+m\ell\dot a\sin\theta$. Differentiating in time gives $m\ell^2\ddot\theta+m\ell\ddot a\sin\theta+m\ell\dot a\cos\theta\dot\theta$. Its coordinate derivative is $m\ell\dot a\cos\theta\dot\theta-mg\ell\sin\theta$. Subtraction yields
$$\ell\ddot\theta+(g+\ddot a)\sin\theta=0.$$

Now $d(m\ell\dot a\cos\theta)/dt=m\ell\ddot a\cos\theta-m\ell\dot a\sin\theta\dot\theta$. Adding this full derivative cancels the cross term. Removing the remaining time-only $\tfrac12m\dot a^2-mga$ leaves
$$L_{\rm eq}=\tfrac12m\ell^2\dot\theta^2+m\ell(g+\ddot a)\cos\theta.$$
It gives the same equation.

For constant $A$ and $|\theta|\ll1$, $\sin\theta=\theta+O(\theta^3)$. If $g+A>0$, $\ddot\theta+[(g+A)/\ell]\theta=0$ has angular frequency $\sqrt{(g+A)/\ell}$. If $g+A=0$, the exact angular equation is $\ddot\theta=0$: there is no restoring torque, and a nonzero initial angular speed persists. If $g+A<0$, the linearized equation is $\ddot\theta-[(|g+A|)/\ell]\theta=0$, with growing and decaying exponential solutions, so the downward orientation is unstable.

The tangent unit vector is $(\cos\theta,\sin\theta)$. The actual acceleration dotted with it is $\ell\ddot\theta+\ddot a\sin\theta$. Projected gravity is $-g\sin\theta$, and the rod reaction is radial; Newton gives the same angular equation. The rigid rod was specified to avoid assuming a string can sustain compressive reaction during strong downward acceleration.

**Independent check:** Direct Euler–Lagrange calculation, total-derivative simplification and independent tangential Newton projection agree; the three small-angle regimes follow from explicitly stated Taylor linearization.

**Common mistakes:** Dropping a cross term without its companion acceleration term; reversing the upward pivot-acceleration sign; treating a rigid rod and a slack-capable string as interchangeable.

**Review prerequisites:** AM01 Physics 2 - Generalized Coordinates and Velocities (not included; [edition scope](../../SOURCES.md#pending)) · AM01 Physics 4 - DAlembert and the Kinetic Energy Equations (not included; [edition scope](../../SOURCES.md#pending)) · AM01 Physics 6 - Equivalent Lagrangians (not included; [edition scope](../../SOURCES.md#pending)) · [AM01 Math 7 - Second Order Equations and Stability](../../mathematics/lecture-01/am01-math-7-second-order-equations-and-stability.md)

<a name="section-15"></a>

## AM01-M04

**A sliding wedge, spring and conserved horizontal momentum** · [Problem](am01-mixed-physics-practice.md#section-6)

The total kinetic and potential energies are
$$T=\tfrac12(M+m)\dot X^2+m\cos\alpha\dot X\dot s+\tfrac12m\dot s^2,$$
$$V=\tfrac12ks^2-mgs\sin\alpha.$$
There is no external horizontal force; the spring forces between bead and wedge are internal to this model. With $L=T-V$,
$$P=L_{\dot X}=(M+m)\dot X+m\cos\alpha\dot s,\qquad \dot P=0,$$
$$m\ddot s+m\cos\alpha\ddot X+ks-mg\sin\alpha=0.$$
Differentiating the constant momentum gives $(M+m)\ddot X+m\cos\alpha\ddot s=0$. Substitute $\ddot X=-m\cos\alpha\ddot s/(M+m)$ into the second equation:
$$m_e\ddot s+ks-mg\sin\alpha=0,$$
$$m_e=m\left(1-\frac{m\cos^2\alpha}{M+m}\right)=\frac{m(M+m\sin^2\alpha)}{M+m}>0.$$
Thus $s_*=mg\sin\alpha/k$ and the exact ideal oscillation frequency about that equilibrium is $\omega=\sqrt{k/m_e}$, subject to the finite incline and maintained contact. Reconstruct
$$\dot X=\frac{P-m\cos\alpha\dot s}{M+m},\quad X(t)-X(0)=\frac{Pt-m\cos\alpha[s(t)-s(0)]}{M+m}.$$

As $M\to\infty$, $m_e\to m$ and wedge acceleration tends to zero, giving the fixed-incline oscillator. Substitution of the momentum expression into total kinetic energy gives $T=P^2/[2(M+m)]+m_e\dot s^2/2$, independently checking the positive effective inertia and energy balance. The reduction was obtained from the equations; it is not a blanket license to substitute conserved momenta into arbitrary Lagrangians before variation. The outward normal is $(\sin\alpha,\cos\alpha)$. Projecting the bead acceleration onto it gives $\ddot X\sin\alpha$, so the contact force is $N=m(g\cos\alpha+\ddot X\sin\alpha)=mg\cos\alpha-m^2\cos\alpha\sin\alpha\,\ddot s/(M+m)$. For an ordinary supporting incline require $N\ge0$; if the predicted motion violates this, the bead leaves the surface and the constrained solution ends. A captured slot would be a different bilateral model.

**Independent check:** The coupled Euler–Lagrange equations, direct total-horizontal-momentum balance, and kinetic-energy completion of the square give the same effective inertia.

**Common mistakes:** Setting wedge velocity to zero when $P=0$; missing the cross term; treating the spring anchor as external to the wedge system; reducing kinetic energy without checking the equations.

**Review prerequisites:** AM01 Physics 2 - Generalized Coordinates and Velocities (not included; [edition scope](../../SOURCES.md#pending)) · AM01 Physics 4 - DAlembert and the Kinetic Energy Equations (not included; [edition scope](../../SOURCES.md#pending)) · AM01 Physics 5 - Lagrangians and Generalized Potentials (not included; [edition scope](../../SOURCES.md#pending)) · [AM01 Math 7 - Second Order Equations and Stability](../../mathematics/lecture-01/am01-math-7-second-order-equations-and-stability.md)

<a name="section-16"></a>

## AM01-M05

**Spherical pendulum: a cyclic coordinate and a conical motion** · [Problem](am01-mixed-physics-practice.md#section-7)

The tangent lengths give
$$T=\tfrac12m\ell^2(\dot\theta^2+\sin^2\theta\dot\phi^2),\quad V=-mg\ell\cos\theta.$$
Euler–Lagrange yields
$$\ddot\theta-\sin\theta\cos\theta\dot\phi^2+\frac g\ell\sin\theta=0,$$
$$\frac d{dt}(m\ell^2\sin^2\theta\dot\phi)=0.$$
Set $J=m\ell^2\sin^2\theta\dot\phi$. Substituting $\dot\phi=J/(m\ell^2\sin^2\theta)$ into the polar equation gives
$$m\ell^2\ddot\theta=-\frac{dV_J}{d\theta},\quad V_J=\frac{J^2}{2m\ell^2\sin^2\theta}-mg\ell\cos\theta,$$
because $V_J'=-J^2\cos\theta/(m\ell^2\sin^3\theta)+mg\ell\sin\theta$. The energy becomes $E=m\ell^2\dot\theta^2/2+V_J$. Substitution into the energy and the already derived equation agrees; naive substitution of a conserved momentum into the original Lagrangian can give a wrong sign and is not used.

For nonvertical conical motion, $\sin\theta_0\ne0$ and $\ddot\theta=0$, so
$$\Omega^2\cos\theta_0=g/\ell.$$
Thus $0<\theta_0<\pi/2$ and $\Omega^2>g/\ell$ for a nonzero cone angle. Let positive tension $\tau$ be inward along the rod. Vertical acceleration is zero, so $\tau\cos\theta_0=mg$; horizontal centripetal motion requires $\tau\sin\theta_0=m\Omega^2\ell\sin\theta_0$. These give $\tau=m\ell\Omega^2=mg/\cos\theta_0$, checking the condition independently.

At fixed $J$, differentiate the effective potential again:
$$V_J''=\frac{J^2}{m\ell^2}\left(\frac1{\sin^2\theta}+\frac{3\cos^2\theta}{\sin^4\theta}\right)+mg\ell\cos\theta.$$
Using $J=m\ell^2\sin^2\theta_0\Omega$ and $g=\ell\Omega^2\cos\theta_0$ gives
$$V_J''(\theta_0)=m\ell^2\Omega^2(1+3\cos^2\theta_0)>0.$$
The polar equilibrium is locally stable at fixed $J$; small polar oscillations have squared frequency $\Omega^2(1+3\cos^2\theta_0)$. During such a free perturbation $\dot\phi$ changes as $1/\sin^2\theta$ to preserve $J$. Holding it fixed instead requires an applied azimuthal torque and corresponds to another system. The angular chart fails at the poles; this is why the domain was specified.

**Independent check:** The conical condition and tension are independently recovered from vertical and horizontal Newton equations; symbolic differentiation checks the effective potential and fixed-momentum stability curvature.

**Common mistakes:** Holding angular speed fixed while claiming angular momentum conservation; applying a polar chart at its poles; confusing conserved-momentum elimination with unconstrained substitution into the Lagrangian.

**Review prerequisites:** AM01 Physics 2 - Generalized Coordinates and Velocities (not included; [edition scope](../../SOURCES.md#pending)) · AM01 Physics 5 - Lagrangians and Generalized Potentials (not included; [edition scope](../../SOURCES.md#pending)) · [AM01 Math 6 - Linear Algebra for Constraints](../../mathematics/lecture-01/am01-math-6-linear-algebra-for-constraints.md) · [AM01 Math 7 - Second Order Equations and Stability](../../mathematics/lecture-01/am01-math-7-second-order-equations-and-stability.md)

<a name="section-17"></a>

## AM01-M06

**A time-dependent velocity potential and the missing force term** · [Problem](am01-mixed-physics-practice.md#section-8)

The momenta are $p_x=m\dot x-eBy/2$, $p_y=m\dot y+eBx/2$. Their time derivatives, minus the coordinate derivatives of $L$, give
$$m\ddot x=-kx+eB\dot y+\tfrac12e\dot B\,y,$$
$$m\ddot y=-ky-eB\dot x-\tfrac12e\dot B\,x.$$
The velocity-linear term cancels in $E_L$, so $E=T+V=m(\dot x^2+\dot y^2)/2+k(x^2+y^2)/2$. Directly dotting the forces with velocity yields
$$\dot E=\frac{e\dot B}{2}(y\dot x-x\dot y)=-L_t.$$
The $B$ terms cancel pairwise; the changing-field terms generally exchange energy with the prescribed external source.

Now
$$\frac{dF}{dt}=\frac e2[\dot Bxy+B\dot x y+Bx\dot y].$$
Hence the equivalent expression is
$$L'=\tfrac12m(\dot x^2+\dot y^2)+eB x\dot y+\tfrac12e\dot Bxy-\tfrac12k(x^2+y^2).$$
For $x$, $L'_{\dot x}=m\dot x$ and $L'_x=eB\dot y+e\dot By/2-kx$, recovering the first equation. For $y$, $L'_{\dot y}=m\dot y+eBx$, whose derivative is $m\ddot y+e\dot Bx+eB\dot x$; subtracting $L'_y=e\dot Bx/2-ky$ recovers the second. Omitting the explicit-time part of the gauge derivative would change the force.

The supplied time-dependent potential describes more than the instantaneous magnetic force $(eB\dot y,-eB\dot x)$: it includes the specified additional $\dot B$ force terms. In an electromagnetic interpretation these are associated with the induced electric field for this potential choice. No Maxwell-equation derivation is claimed here. When $\dot B=0$, energy is conserved and the constant-field model is recovered.

**Independent check:** Both Lagrangians are differentiated independently, and the energy rate is checked against the force-power sum and $-L_t$.

**Common mistakes:** Treating $B(t)$ as constant during total differentiation; omitting the scalar time-derivative term after a gauge change; claiming a time-varying magnetic-only force reproduces this Lagrangian.

**Review prerequisites:** AM01 Physics 5 - Lagrangians and Generalized Potentials (not included; [edition scope](../../SOURCES.md#pending)) · AM01 Physics 6 - Equivalent Lagrangians (not included; [edition scope](../../SOURCES.md#pending))

<a name="section-18"></a>

## AM01-M07

**Rotating hoop: equilibrium, stability and mechanical power** · [Problem](am01-mixed-physics-practice.md#section-9)

The map gives
$$L=\tfrac12mR^2\dot\theta^2+\tfrac12mR^2\Omega^2\sin^2\theta+mgR\cos\theta,$$
so
$$\ddot\theta=\sin\theta(\Omega^2\cos\theta-g/R).$$
With the effective potential stated in Hint 2, equilibria include bottom $\theta=0$ and top $\theta=\pi$. The curvatures are $V_{\rm eff}''(0)=mgR-mR^2\Omega^2$ and $V_{\rm eff}''(\pi)=-mgR-mR^2\Omega^2$. The top is unstable. The bottom is stable for $\Omega^2<g/R$ and unstable for $\Omega^2>g/R$.

At equality $\Omega^2=g/R$, expand $\sin^2\theta=\theta^2-\theta^4/3+O(\theta^6)$ and $\cos\theta=1-\theta^2/2+\theta^4/24+O(\theta^6)$. The quadratic term cancels and $V_{\rm eff}=\text{constant}+mgR\theta^4/8+O(\theta^6)$. The bottom remains a strict local minimum and is nonlinearly stable, but its linear small-oscillation frequency is zero; the ordinary quadratic test is inconclusive there.

For $\Omega^2>g/R$, two signed-angle positions $\theta=\pm\arccos[g/(R\Omega^2)]$ lie on opposite sides of the bottom and are distinct stable equilibria on the hoop. At either, $V_{\rm eff}''=mR^2\Omega^2\sin^2\theta>0$.

The autonomous reduced Lagrangian conserves
$$E_L=\tfrac12mR^2\dot\theta^2-\tfrac12mR^2\Omega^2\sin^2\theta-mgR\cos\theta.$$
Physical energy is instead $E=\tfrac12mR^2\dot\theta^2+\tfrac12mR^2\Omega^2\sin^2\theta-mgR\cos\theta$, so
$$\dot E=2mR^2\Omega^2\sin\theta\cos\theta\dot\theta.$$
For a temporarily independent azimuth $\phi$, the conjugate angular momentum is $p_\phi=mR^2\sin^2\theta\dot\phi$. Imposing $\dot\phi=\Omega$ requires torque $\tau_z=\dot p_\phi=2mR^2\Omega\sin\theta\cos\theta\dot\theta$. Its power $\Omega\tau_z$ matches $\dot E$. The ideal constraint has zero virtual work at fixed time but can exchange actual energy through its drive.

**Independent check:** Coordinate velocity expansion, the torque–power calculation and direct mechanical-energy differentiation agree; symbolic curvature and Taylor checks distinguish the critical case correctly.

**Common mistakes:** Equating an autonomous reduced energy with physical mechanical energy; declaring the critical bottom unstable solely because the quadratic term vanishes; forgetting the actuator or the second symmetric equilibrium.

**Review prerequisites:** AM01 Physics 2 - Generalized Coordinates and Velocities (not included; [edition scope](../../SOURCES.md#pending)) · AM01 Physics 5 - Lagrangians and Generalized Potentials (not included; [edition scope](../../SOURCES.md#pending)) · AM01 Physics 7 - Atwood Machine (not included; [edition scope](../../SOURCES.md#pending)) · [AM01 Math 7 - Second Order Equations and Stability](../../mathematics/lecture-01/am01-math-7-second-order-equations-and-stability.md)

<a name="section-19"></a>

## AM01-M08

**Massive pulley, braking torque and side tensions** · [Problem](am01-mixed-physics-practice.md#section-10)

Let $M_e=m_1+m_2+I/R^2$ and $\Delta m=m_1-m_2$. Up to a constant,
$$L=\tfrac12M_e\dot q^2+\Delta m\,gq,\quad Q^{\rm rem}=-\tau_b/R.$$
The equation gives
$$a=\ddot q=\frac{\Delta m\,g-\tau_b/R}{M_e}.$$
The individual mass equations give
$$\tau_1=m_1(g-a),\qquad \tau_2=m_2(g+a).$$
Their difference is $\tau_1-\tau_2=\Delta m\,g-(m_1+m_2)a$. Multiply by $R$ and subtract the brake torque. Using $M_ea=\Delta m\,g-\tau_b/R$ yields
$$(\tau_1-\tau_2)R-\tau_b=\frac IR a,$$
which is precisely the pulley equation $I\dot\omega$ with $\dot\omega=a/R$.

Physical energy $E=M_e\dot q^2/2-\Delta m\,gq$ satisfies
$$\dot E=\dot q(M_ea-\Delta m\,g)=-\frac{\tau_b}{R}\dot q<0$$
on the specified positive-velocity interval. The sign of acceleration can still be negative: braking may slow an initially positive motion. Require positive hanging lengths, no slip, and nonnegative tensions; strict tautness requires $-g<a<g$. The torque law was specified only for $\dot q>0$. At stopping, static brake behavior or a reversal law must be supplied; do not continue the same constant opposing-sign force through a reversal and call it dissipative. Taking $I\to0$ and $\tau_b\to0$ recovers the ideal source model.

**Independent check:** Both mass equations and the independently written pulley torque equation are satisfied; mechanical-energy differentiation matches brake power.

**Common mistakes:** Assuming equal tensions with pulley inertia or braking; forgetting the factor $1/R$ converting torque to generalized force; extrapolating a velocity-sign-dependent brake law through rest.

**Review prerequisites:** AM01 Physics 7 - Atwood Machine (not included; [edition scope](../../SOURCES.md#pending)) · AM01 Physics 4 - DAlembert and the Kinetic Energy Equations (not included; [edition scope](../../SOURCES.md#pending)) · AM01 Physics 5 - Lagrangians and Generalized Potentials (not included; [edition scope](../../SOURCES.md#pending))

<a name="section-20"></a>

## AM01-M09

**A time-dependent Lagrangian that deliberately adds damping** · [Problem](am01-mixed-physics-practice.md#section-11)

For $L_d$, the Euler–Lagrange expression is
$$e^{\gamma t}(m\ddot q+\gamma m\dot q+kq).$$
Since the exponential never vanishes, choose $\gamma=b/m$ to obtain the damped equation. This intentionally changes the dynamics relative to homogeneous $L_0$; it is not an allowed equivalence scaling of the undamped oscillator.

Physical energy $E=m\dot q^2/2+kq^2/2$ obeys $\dot E=\dot q(m\ddot q+kq)=-b\dot q^2$. The generalized energy is $E_{L_d}=e^{\gamma t}E$, whose derivative is
$$\frac d{dt}E_{L_d}=e^{\gamma t}(\gamma E-b\dot q^2)
=\gamma e^{\gamma t}(V-T)=-\frac{\partial L_d}{\partial t}.$$
It is generally not conserved and is not the physical mechanical energy.

The no-go calculation in Physics 5 concerned $Q=-U_q+dU_{\dot q}/dt=-b\dot q$ as an identity with no acceleration term for arbitrary $(q,\dot q,\ddot q,t)$ and physical $T=m\dot q^2/2$. Acceleration independence forced $U_{\dot q\dot q}=0$, giving no one-dimensional velocity term. Here the whole kinetic coefficient has been rescaled. If one writes $L_d=T-U$ using the original physical $T$, then $U=(1-e^{\gamma t})T+e^{\gamma t}V$ has $U_{\dot q\dot q}=m(1-e^{\gamma t})$, so its generalized-force expression includes acceleration. It is not the prohibited acceleration-free force identity, even though the final rescaled equation is dynamically the desired damped oscillator. Different representation requirements are being compared.

**Independent check:** The Euler–Lagrange expression and both energy-rate identities are verified independently by differentiation; the velocity Hessian exposes the precise assumption bypassed by the construction.

**Common mistakes:** Calling $L_d$ equivalent to the undamped $L_0$; interpreting $E_{L_d}$ as physical energy; overextending a limited generalized-potential result into a universal ban on dissipative Lagrangians.

**Review prerequisites:** AM01 Physics 5 - Lagrangians and Generalized Potentials (not included; [edition scope](../../SOURCES.md#pending)) · AM01 Physics 6 - Equivalent Lagrangians (not included; [edition scope](../../SOURCES.md#pending)) · [AM01 Math 7 - Second Order Equations and Stability](../../mathematics/lecture-01/am01-math-7-second-order-equations-and-stability.md)

<a name="section-21"></a>

## AM01-M10

**A moving coordinate system without a moving physical support** · [Problem](am01-mixed-physics-practice.md#section-12)

The transformed expression is
$$L=\tfrac12m(\dot q+u)^2-\tfrac12k(q+ut)^2.$$
Subtract $dF/dt$ with $F=muq+mu^2t/2$, obtaining
$$L_r=\tfrac12m\dot q^2-\tfrac12k(q+ut)^2.$$
The equation is $m\ddot q+k(q+ut)=0$. Since $\ddot x=\ddot q$ and $x=q+ut$, this is exactly the laboratory equation $m\ddot x+kx=0$.

The reduced generalized energy is $E_r=m\dot q^2/2+k(q+ut)^2/2$. Direct differentiation and the equation give
$$\dot E_r=ku(q+ut)=-\partial L_r/\partial t.$$
The physical laboratory energy is
$$E_{\rm lab}=\tfrac12m(\dot q+u)^2+\tfrac12k(q+ut)^2
=E_r+mu\dot q+\tfrac12mu^2.$$
Its derivative is $ku(q+ut)+mu\ddot q=0$. No physical spring support moves; the time dependence comes from the coordinate description, and the physical laboratory energy is conserved.

With $\omega=\sqrt{k/m}$, the laboratory initial data are $x(0)=q_0$ and $\dot x(0)=v_0+u$. Hence
$$q(t)=q_0\cos\omega t+\frac{v_0+u}{\omega}\sin\omega t-ut.$$
Differentiate to confirm $q(0)=q_0$, $\dot q(0)=v_0$ and $m\ddot q+k(q+ut)=0$. A genuinely moving spring support would be a different laboratory potential and could exchange physical energy; it must not be inferred from this coordinate change alone.

**Independent check:** Direct transformation of Newton equation, explicit solution substitution and both energy derivatives agree; the specified total derivative is checked identically.

**Common mistakes:** Treating a moving coordinate origin as a driven physical support; using $\dot q$ as laboratory velocity; dropping the cross term without tracking the total derivative; claiming physical energy loss from $\dot E_r\ne0$.

**Review prerequisites:** AM01 Physics 2 - Generalized Coordinates and Velocities (not included; [edition scope](../../SOURCES.md#pending)) · AM01 Physics 5 - Lagrangians and Generalized Potentials (not included; [edition scope](../../SOURCES.md#pending)) · AM01 Physics 6 - Equivalent Lagrangians (not included; [edition scope](../../SOURCES.md#pending)) · [AM01 Math 7 - Second Order Equations and Stability](../../mathematics/lecture-01/am01-math-7-second-order-equations-and-stability.md)

[Section index](README.md) · [Home](../../README.md)
