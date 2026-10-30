<a name="section-1"></a>

# AM02 Final Physics Solutions

> **Edition scope:** original AI-assisted supplement or study material. Some prerequisite lessons are withheld for source review; their titles are plain text, not unavailable links. This file is an excerpt: the retained question IDs and their full calculations are unchanged. [Attribution and scope](../../SOURCES.md#pending).


> **Review status: unverified.** AI-assisted educational draft; human scientific review remains pending. [Sources and limitations](../../SOURCES.md).


**AI SUPPLEMENT — solutions, not learner records.** The derivations and checks support review; human scientific acceptance remains pending. Verification code and its limits are recorded in internal review documentation (not included in this collection).

<a name="section-2"></a>

## AM02-F01

**Torque, drag and a prescribed radius**. [Question](am02-final-focused-physics-practice.md#section-2) · AM02 Unit 02-2 - Generalized Forces in Polar Coordinates (not included; [edition scope](../../SOURCES.md#pending)) · [AM02 Math A - Moving Bases and Vector Products](../../mathematics/lecture-02/am02-math-a-moving-bases-and-vector-products.md).

The tangential force is $F_\theta=\tau_0/r-br\dot\theta$, so
$$\dot\ell=\tau_0-(b/m)\ell,\quad
\ell(t)=\frac{m\tau_0}{b}+\left(mr_0^2\omega_0-\frac{m\tau_0}{b}\right)e^{-bt/m},\quad
\dot\theta=\frac{\ell(t)}{m(r_0+ut)^2}.$$
Multiply the linear equation by $e^{bt/m}$, integrate the derivative of $e^{bt/m}\ell$, and impose the initial value to obtain this result. Radial balance is $-mr\dot\theta^2=F_a-bu$, hence $F_a=bu-mr\dot\theta^2$, outward positive. Its power is $P_a=F_a u$. The complete power balance is
$$\dot T=F_a u+\tau_0\dot\theta-b(u^2+r^2\dot\theta^2).$$
This follows independently by dotting Cartesian force balance with velocity. An outward-moving actuator can absorb energy when its required force is inward.

**Independent check / limits:** As $b\to0$, $\ell=mr_0^2\omega_0+\tau_0t$. At $u=0$ actuator power vanishes. $F_a$ is N and $\tau_0\dot\theta$ is W.

**Common mistake:** Solving an exponential law for angular speed while ignoring changing radius; assigning torque to a radial force.

<a name="section-3"></a>

## AM02-F02

**A coupled release from rest**. [Question](am02-final-focused-physics-practice.md#section-3) · AM02 Unit 02-3 - Double Pendulum and Coupled Coordinates (not included; [edition scope](../../SOURCES.md#pending)) · [AM02 Math B - Homogeneity and Kinetic Forms](../../mathematics/lecture-02/am02-math-b-homogeneity-and-kinetic-forms.md).

At release, write $a_j=\ddot\phi_j(0)$. The two equations reduce to $2a_1+\cos\alpha\,a_2=-2g\sin\alpha/l$ and $a_2+\cos\alpha\,a_1=0$. Substitute $a_2=-\cos\alpha\,a_1$ into the first equation:
$$\ddot\phi_1(0)=-\frac{2g\sin\alpha}{l(1+\sin^2\alpha)},\quad
\ddot\phi_2(0)=\frac{2g\sin\alpha\cos\alpha}{l(1+\sin^2\alpha)}.$$
To first order these are $-2g\alpha/l$ and $+2g\alpha/l$. The lower mass's suspension point accelerates, so its absolute angle can accelerate although its own gravitational torque about that point is initially zero. A Newtonian check projects the lower-mass equation on its horizontal tangent: $l\ddot\phi_2+l\cos\alpha\ddot\phi_1=0$. The rod model avoids an untested nonnegative-string-tension assumption.

**Independent check / limits:** Substitute into both acceleration equations. At $\alpha=0$ both vanish; at $\alpha=\pi/2$, $a_1=-g/l$, $a_2=0$. Accelerations have s⁻² units.

**Common mistake:** Setting the lower acceleration to zero from its gravity torque alone; treating its angle as relative.

<a name="section-6"></a>

## AM02-F05

**A spring whose stiffness changes**. [Question](am02-final-focused-physics-practice.md#section-6) · AM02 Unit 02-5 - Generalized Energy and Conservation Laws (not included; [edition scope](../../SOURCES.md#pending)) · [AM02 Math B - Homogeneity and Kinetic Forms](../../mathematics/lecture-02/am02-math-b-homogeneity-and-kinetic-forms.md).

The equation is $m\ddot x+kx=-b\dot x$. Direct differentiation gives
$$\dot E=\dot x(m\ddot x+kx)+\tfrac12\dot kx^2=-b\dot x^2+\tfrac12\dot kx^2.$$
It also follows from $Q\dot x-L_t$. A finite stiffness step produces a force step, not a delta impulse. Position and velocity remain continuous, while
$$E_+-E_-=\tfrac12(k_+-k_-)x_*^2.$$
The stiffness-control apparatus supplies or extracts this energy. The result is the limit of a short smooth parameter change; integrating the exact energy balance gives the same jump. A discontinuous position or velocity would require different physical assumptions.

**Independent check / limits:** At $x_*=0$ the jump is zero. For constant $k$ and $b>0$, energy is nonincreasing. Stiffness times length squared has joule units.

**Common mistake:** Assuming energy continuity during parameter work; omitting the explicitly retained drag force.

<a name="section-7"></a>

## AM02-F06

**A free particle in an accelerating coordinate**. [Question](am02-final-focused-physics-practice.md#section-7) · AM02 Unit 02-5 - Generalized Energy and Conservation Laws (not included; [edition scope](../../SOURCES.md#pending)) · [AM02 Math B - Homogeneity and Kinetic Forms](../../mathematics/lecture-02/am02-math-b-homogeneity-and-kinetic-forms.md).

We obtain $p=m(\dot q+\dot a)=m\dot X$, constant, and
$$E_L=\tfrac12m\dot q^2-\tfrac12m\dot a^2,\qquad
\dot E_L=-m(\dot q+\dot a)\ddot a=-L_t.$$
Laboratory kinetic energy $m\dot X^2/2$ is constant. Subtract $dF/dt$ with $F=m\dot a q+\int^t m\dot a(s)^2/2\,ds$ to get
$$\widetilde L=\tfrac12m\dot q^2-m\ddot a q,\quad
\widetilde E=\tfrac12m\dot q^2+m\ddot a q=E_L+F_t.$$
Its equation is still $\ddot q=-\ddot a$ and $\dot{\widetilde E}=m\dddot a q=-\widetilde L_t$. Thus canonical energy changes with both coordinates and total-derivative choice, without physical work on the free particle. The partial $F_t$ is taken at fixed $q$.

**Independent check / limits:** For $a=ut$, both canonical energies are constant but differ; for constant frame acceleration $\widetilde E$ is conserved. The explicit trajectory $q=X_0+v_0t-a(t)$ verifies every relation.

**Common mistake:** Using total rather than partial $F_t$ in the energy shift; interpreting frame-induced energy change as work.

<a name="section-8"></a>

## AM02-F07

**Bead on a driven radial rod**. [Question](am02-final-focused-physics-practice.md#section-8) · AM02 Unit 02-6 - Non-Inertial Reference Frames (not included; [edition scope](../../SOURCES.md#pending)) · [AM02 Math A - Moving Bases and Vector Products](../../mathematics/lecture-02/am02-math-a-moving-bases-and-vector-products.md).

The reduced Lagrangian is $L=m(\dot r^2+\Omega^2r^2)/2$, giving $\ddot r=\Omega^2r$. For nonzero $\Omega$,
$$r=r_0\cosh(\Omega t)+(u_0/\Omega)\sinh(\Omega t).$$
Here $\cosh z=(e^z+e^{-z})/2$ and $\sinh z=(e^z-e^{-z})/2$; the two exponential solutions and initial data determine the expression. Newton's angular equation gives $N_\theta=2m\Omega\dot r$. Its power is $N_\theta\Omega r=2m\Omega^2r\dot r=\dot T_{\rm lab}$. The reduced constant is $E_L=m(\dot r^2-\Omega^2r^2)/2$. In the rotating frame, tangential reaction balances Coriolis force while centrifugal acceleration drives radial motion. The formula applies while $r>0$ and contact with the modeled rod persists.

**Independent check / limits:** For $\Omega\to0$, $r=r_0+u_0t$, with zero tangential reaction. Direct substitution checks the ODE and initial conditions; the reaction has force units.

**Common mistake:** Conserving laboratory kinetic energy because the guide is smooth; dropping the Coriolis reaction.

<a name="section-9"></a>

## AM02-F08

**Holding a bead in a changing rotating frame**. [Question](am02-final-focused-physics-practice.md#section-9) · AM02 Unit 02-6 - Non-Inertial Reference Frames (not included; [edition scope](../../SOURCES.md#pending)) · [AM02 Math A - Moving Bases and Vector Products](../../mathematics/lecture-02/am02-math-a-moving-bases-and-vector-products.md).

Inertial velocity and acceleration are
$$\mathbf v_I=a\Omega\mathbf e_\theta,\quad
\mathbf a_I=-a\Omega^2\mathbf e_r+a\dot\Omega\mathbf e_\theta.$$
Thus $F_r=-ma\Omega^2$, $F_\theta=ma\dot\Omega$. Equivalently these real forces balance centrifugal and Euler inertial forces; Coriolis is zero because relative velocity is zero. Laboratory power is $P=ma^2\Omega\dot\Omega=d(ma^2\Omega^2/2)/dt$. The holder can push or pull, so no unilateral force-sign restriction is imposed.

**Independent check / limits:** For constant $\Omega$ the centripetal force does no work. At $\Omega=0$ but $\dot\Omega\ne0$, tangential force is nonzero while instantaneous power is zero.

**Common mistake:** Omitting Euler force at relative rest; confusing actual and apparent forces.

<a name="section-10"></a>

## AM02-F09

**Crossed fields in a cyclic gauge**. [Question](am02-final-focused-physics-practice.md#section-10) · AM02 Unit 02-7 - Charged Particles and Electromagnetic Potentials (not included; [edition scope](../../SOURCES.md#pending)) · [AM02 Math C - Curl Circulation and Gauge](../../mathematics/lecture-02/am02-math-c-curl-circulation-and-gauge.md).

Euler–Lagrange gives $m\ddot x=qE_0+qB\dot y$, $m\ddot y=-qB\dot x$, and $p_y=m\dot y+qBx=0$. Define the signed frequency $\omega_c=qB/m$ and $u=E_0/B$. Eliminating $\dot y=-\omega_c x$ gives $\ddot x+\omega_c^2x=qE_0/m$. Solving this shifted oscillator with the initial data,
$$v_x=u\sin\omega_ct,\quad v_y=u(\cos\omega_ct-1),$$
$$x=\frac u{\omega_c}(1-\cos\omega_ct),\quad
y=\frac u{\omega_c}\sin\omega_ct-ut.$$
The average over a cyclotron period is $-u\mathbf e_y=\mathbf E\times\mathbf B/B^2$, independent of charge sign. The conserved energy is $T-qE_0x=0$. Explicitly $T=mu^2(1-\cos\omega_ct)$ and $qE_0u/\omega_c=mu^2$. Magnetic force does no work; electric work accounts for all kinetic-energy change.

**Independent check / limits:** All four initial data and both ODEs hold. At short times $x=qE_0t^2/(2m)+O(t^4)$. At $E_0=0$ the particle stays at rest.

**Common mistake:** Reversing the drift sign; confusing signed cyclotron frequency with drift direction.

<a name="section-11"></a>

## AM02-F10

**Time-dependent gauge of a pure magnetic field**. [Question](am02-final-focused-physics-practice.md#section-11) · AM02 Unit 02-7 - Charged Particles and Electromagnetic Potentials (not included; [edition scope](../../SOURCES.md#pending)) · [AM02 Math C - Curl Circulation and Gauge](../../mathematics/lecture-02/am02-math-c-curl-circulation-and-gauge.md).

The new potentials are
$$\mathbf A'=(-By/2+\lambda ty,Bx/2+\lambda tx,0),\quad \phi'=-\lambda xy.$$
Their curl is still $B\mathbf e_z$; the added curl is $\lambda t-\lambda t=0$. The electric field is $(\lambda y,\lambda x,0)-(\lambda y,\lambda x,0)=0$. Canonical momenta are
$$p'_x=mv_x-qBy/2+q\lambda ty,\quad p'_y=mv_y+qBx/2+q\lambda tx.$$
The energy is $E'_L=T-q\lambda xy$ and generally has rate $-q\lambda(yv_x+xv_y)$. The physical $T=E'_L+q\lambda xy$ remains constant. The coupling change is $q\lambda[xy+t(yv_x+xv_y)]=q\,d(\lambda txy)/dt$, so the motion equations are unchanged.

**Independent check / limits:** For $\lambda=0$ recover symmetric gauge. Both field components are independently unchanged. $q\chi_t$ has energy units.

**Common mistake:** Changing vector potential alone; mistaking time-dependent potentials for time-dependent physical fields.

<a name="section-12"></a>

## AM02-X01

**A movable wedge and two conservation laws**. [Question](am02-final-mixed-physics-practice.md#section-2) · AM02 Unit 02-4 - Cyclic Coordinates and Generalized Momentum (not included; [edition scope](../../SOURCES.md#pending)) · [AM02 Math B - Homogeneity and Kinetic Forms](../../mathematics/lecture-02/am02-math-b-homogeneity-and-kinetic-forms.md).

The Lagrangian is $L=(M+m)\dot X^2/2-m\cos\beta\,\dot X\dot s+m\dot s^2/2+mgs\sin\beta$. It follows by squaring $(\dot X-\dot s\cos\beta,-\dot s\sin\beta)$. Its equations give
$$(M+m)\ddot X=m\cos\beta\,\ddot s,\quad \ddot s-\cos\beta\,\ddot X=g\sin\beta.$$
Hence, with $D=M+m\sin^2\beta$,
$$\ddot s=\frac{(M+m)g\sin\beta}{D},\quad
\ddot X=\frac{mg\sin\beta\cos\beta}{D}.$$
Cyclic momentum $(M+m)\dot X-m\cos\beta\dot s=0$ is the total horizontal momentum here because there is no external horizontal force. The upward face normal is $(-\sin\beta,\cos\beta)$; block acceleration dotted with it is $-\ddot X\sin\beta$. Thus $N=m(g\cos\beta-\ddot X\sin\beta)=mMg\cos\beta/D>0$. Floor support is positive as well: $N_{\rm floor}=Mg+N\cos\beta$. Energy $T-mgs\sin\beta$ is constant, independently checked by multiplying the two equations by their velocities.

**Independent check / limits:** As $M\to\infty$, $\ddot X\to0$, $\ddot s\to g\sin\beta$, $N\to mg\cos\beta$. All denominators are positive for the stated masses.

**Common mistake:** Assigning the wedge horizontal force directly to the block without accounting for normal orientation.

<a name="section-16"></a>

## AM02-X05

**Central attraction with drag**. [Question](am02-final-mixed-physics-practice.md#section-6) · AM02 Unit 02-2 - Generalized Forces in Polar Coordinates (not included; [edition scope](../../SOURCES.md#pending)) · [AM02 Math A - Moving Bases and Vector Products](../../mathematics/lecture-02/am02-math-a-moving-bases-and-vector-products.md).

The polar equations are
$$m(\ddot r-r\dot\theta^2)=-\kappa/r^2-b\dot r,\quad
m(r\ddot\theta+2\dot r\dot\theta)=-br\dot\theta.$$
Thus $\ell=mr^2\dot\theta=\ell_0e^{-bt/m}$. Energy
$$E=\tfrac12m(\dot r^2+r^2\dot\theta^2)-\kappa/r$$
satisfies $\dot E=-b(\dot r^2+r^2\dot\theta^2)$ from force power, independently confirming the generalized-energy calculation. The coordinate accelerations are $\ddot r=\ell^2/(m^2r^3)-\kappa/(mr^2)-(b/m)\dot r$ and $\ddot\theta=-2\dot r\dot\theta/r-(b/m)\dot\theta$. An initially outward radial velocity remains outward for some short interval by continuity, while energy decreases. Therefore dissipation does not imply instantaneous inward motion. The model is restricted to $r>0$ and fails at a collision singularity.

**Independent check / limits:** For $b=0$, both energy and angular momentum are conserved; for $\ell_0=0$ the motion is radial as long as the polar description is regular. Energy rate is always nonpositive.

**Common mistake:** Double-counting the central potential force; inferring the sign of $\dot r$ from the sign of $\dot E$.

<a name="section-17"></a>

## AM02-X06

**An oscillator viewed from rotating axes**. [Question](am02-final-mixed-physics-practice.md#section-7) · AM02 Unit 02-6 - Non-Inertial Reference Frames (not included; [edition scope](../../SOURCES.md#pending)) · [AM02 Math A - Moving Bases and Vector Products](../../mathematics/lecture-02/am02-math-a-moving-bases-and-vector-products.md).

Let $\omega_0=\sqrt{k/m}$. Expansion of the inertial kinetic energy gives
$$L=\tfrac12m|\dot{\mathbf r}+\boldsymbol\Omega\times\mathbf r|^2-\tfrac12kr^2.$$
Euler–Lagrange or transformed Newton gives $m\ddot{\mathbf r}=-k\mathbf r-2m\boldsymbol\Omega\times\dot{\mathbf r}-m\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf r)$. In this plane it becomes $m\ddot{\mathbf r}+2m\boldsymbol\Omega\times\dot{\mathbf r}+(k-m\Omega^2)\mathbf r=0$. Its conserved energy is
$$E_L=\tfrac12m\dot r_{\rm vec}^2+\tfrac12(k-m\Omega^2)r^2,$$
where $\dot r_{\rm vec}^2=|\dot{\mathbf r}|^2$ includes both component velocities. It may be indefinite. Nevertheless the general inertial solution is $\mathbf R(t)=\mathbf a\cos\omega_0t+\mathbf b\sin\omega_0t$ for constant planar vectors set by arbitrary initial data. The rotating solution is
$$\mathbf r(t)=\mathsf R(-\Omega t)[\mathbf a\cos\omega_0t+\mathbf b\sin\omega_0t].$$
Orthogonal rotations preserve length, so every such motion is bounded. This includes all initial conditions because the coordinate/velocity transformation is invertible. The negative effective potential alone is not a stability test in the presence of velocity-dependent Coriolis terms; ignoring them falsely predicts exponential growth.

**Independent check / limits:** At $\Omega=0$ recover the ordinary oscillator. Rotation preserves the amplitude bound $|\mathbf r|\le|\mathbf a|+|\mathbf b|$. Direct differentiation verifies the rotating ODE.

**Common mistake:** Using the effective-potential curvature as a sufficient instability test while dropping gyroscopic velocity terms.

<a name="section-18"></a>

## AM02-X07

**Pendulum on a horizontally accelerating support**. [Question](am02-final-mixed-physics-practice.md#section-8) · AM02 Unit 02-6 - Non-Inertial Reference Frames (not included; [edition scope](../../SOURCES.md#pending)) · [AM02 Math A - Moving Bases and Vector Products](../../mathematics/lecture-02/am02-math-a-moving-bases-and-vector-products.md).

With position $l(\sin\theta,-\cos\theta)$, the translating-frame Lagrangian after total-derivative removal is
$$L=\tfrac12ml^2\dot\theta^2+mgl\cos\theta-mal\sin\theta.$$
Thus $l\ddot\theta+g\sin\theta+a\cos\theta=0$. Set $G=\sqrt{g^2+a^2}$, $\delta=\operatorname{atan2}(a,g)$; the stable equilibrium is $\theta_*=-\delta$ modulo $2\pi$, not the opposite extremum. With $\eta=\theta-\theta_*$,
$$\ddot\eta+(G/l)\sin\eta=0,\qquad \omega_{\rm small}=\sqrt{G/l}.$$
The effective force $m(-a,-g)$ dotted with the unit tangent $(\cos\theta,\sin\theta)$ gives $-m(a\cos\theta+g\sin\theta)$, verifying the equation independently. A string at stable equilibrium has positive tension $mG$; sufficiently small oscillations preserve tautness, whereas unrestricted large motions require checking tension.

**Independent check / limits:** At $a=0$, $\theta_*=0$ and $\omega=\sqrt{g/l}$. Reversing $a$ reverses the lean but not the frequency. $G$ is an acceleration, so $\sqrt{G/l}$ has frequency units.

**Common mistake:** Choosing the unstable equilibrium; omitting the support acceleration because axes do not rotate.

<a name="section-19"></a>

## AM02-X08

**Changing magnetic field and induced electric work**. [Question](am02-final-mixed-physics-practice.md#section-9) · AM02 Unit 02-7 - Charged Particles and Electromagnetic Potentials (not included; [edition scope](../../SOURCES.md#pending)) · [AM02 Math C - Curl Circulation and Gauge](../../mathematics/lecture-02/am02-math-c-curl-circulation-and-gauge.md).

The fields are $\mathbf B=B(t)\mathbf e_z$ and $\mathbf E=-(r\dot B/2)\mathbf e_\theta$. The Lagrangian is
$$L=\tfrac12m(\dot r^2+r^2\dot\theta^2)+\tfrac12qB(t)r^2\dot\theta.$$
It is cyclic in $\theta$, giving $C=mr^2\dot\theta+qB(t)r^2/2$. Direct torque balance gives
$$\dot\ell_z=-qBr\dot r-\tfrac12q\dot Br^2=-\frac d{dt}(qBr^2/2),$$
which checks the result. Its generalized energy is $T$, but explicit time dependence gives
$$\dot T=-L_t=-\tfrac12q\dot Br^2\dot\theta=q\mathbf E\cdot\mathbf v.$$
The magnetic force still does zero work; the induced electric field exchanges energy. A spatially uniform changing magnetic field and its linearly growing induced electric field are an idealization on a suitable region, not a globally finite-energy field-source model.

**Independent check / limits:** For constant $B$ recover the static-field angular law and constant speed. The electric field has units T m/s = V/m. At $\dot\theta=0$ instantaneous electric power vanishes but the tangential force need not.

**Common mistake:** Setting $\mathbf E=0$ because scalar potential is zero; forgetting the derivative of $B$ in angular momentum.

<a name="section-21"></a>

## AM02-X10

**Energy in a uniformly rotating angular coordinate**. [Question](am02-final-mixed-physics-practice.md#section-11) · AM02 Unit 02-5 - Generalized Energy and Conservation Laws (not included; [edition scope](../../SOURCES.md#pending)) · [AM02 Math B - Homogeneity and Kinetic Forms](../../mathematics/lecture-02/am02-math-b-homogeneity-and-kinetic-forms.md).

The transformed Lagrangian is
$$L'= \tfrac12m[\dot r^2+r^2(\dot\psi+\Omega)^2]-V(r).$$
It lacks both $\psi$ and explicit $t$, so $p_\psi=\ell=mr^2(\dot\psi+\Omega)$ is constant and
$$E_{\rm rot}=\tfrac12m\dot r^2+\tfrac12mr^2\dot\psi^2-\tfrac12mr^2\Omega^2+V=E-\Omega\ell.$$
The equality follows by expanding inertial $E=m[\dot r^2+r^2(\dot\psi+\Omega)^2]/2+V$ and subtracting $\Omega mr^2(\dot\psi+\Omega)$. Newton independently conserves $E$ by work and $\ell$ by central-force torque, so their constant linear combination is conserved. After adding $dF/dt$, new quantities obey $p''_\psi=p_\psi+F_\psi$ and $E''=E_{\rm rot}-F_t$. The conserved combinations are $p''_\psi-F_\psi$ and $E''+F_t$. Neither bare new coefficient need be constant if the gauge hides the cyclic/autonomous form. Smooth single-valued local $F$ and the same classical trajectory assumptions are understood.

**Independent check / limits:** For $\Omega=0$ the rotating energy equals $E$. The product $\Omega\ell$ has energy units. This is consistent with Unit 02.6's centrifugal effective potential.

**Common mistake:** Identifying rotating generalized energy with laboratory energy; taking $F_t$ along the trajectory rather than partially.

[Section index](README.md) · [Home](../../README.md)
