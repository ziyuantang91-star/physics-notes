<a name="section-1"></a>

# AM01 Math 7 — Second-Order Equations and Local Stability

> **Edition scope:** original AI-assisted supplement or study material. Some prerequisite lessons are withheld for source review; their titles are plain text, not unavailable links. [Attribution and scope](../../SOURCES.md#pending).


> **Review status: unverified.** AI-assisted educational draft; human scientific review remains pending. [Sources and limitations](../../SOURCES.md).


**AI SUPPLEMENT:** the lecture produces second-order dynamical equations in P307–P309 and solves constant acceleration in P381–P383. The oscillator and stability analyses used in the mixed practice are additional applications. AP Calculus BC supplies differentiation, integration and Taylor approximation, but does not by itself establish familiarity with second-order initial-value problems. This note supplies that foundation before it is used. It does not develop normal-mode theory or complex-valued differential equations.

Prerequisites: ordinary derivatives and integrals; partial derivatives (not included; [edition scope](../../SOURCES.md#pending)) and first-order changes (not included; [edition scope](../../SOURCES.md#pending)) for linearization. Physical links: oscillator and energy (not included; [edition scope](../../SOURCES.md#pending)), constant acceleration (not included; [edition scope](../../SOURCES.md#pending)).

<a name="section-2"></a>

## 1. What information a second-order equation determines

An equation $\ddot q=f(q,\dot q,t)$ determines acceleration from the current state. It does not, by itself, select a unique trajectory: initial position $q(t_0)=q_0$ and velocity $\dot q(t_0)=v_0$ are also needed. We will prove completeness of the solution forms actually used below rather than assume every trial function finds every solution.

For constant acceleration $a$, integrate once to obtain $\dot q=v_0+a(t-t_0)$ and again to obtain $q=q_0+v_0(t-t_0)+a(t-t_0)^2/2$. The two integration constants are fixed by the two initial data. Differentiating the result verifies both the differential equation and those data. Its time of validity still depends on the physical model: a collision or slackening rope can end that interval.

<a name="section-3"></a>

## 2. Derive and completely specify harmonic motion

Consider

$$
\ddot\eta+\omega^2\eta=0,\qquad \omega>0.
$$

The derivative rules for sine and cosine show that both $\cos\omega\tau$ and $\sin\omega\tau$, with $\tau=t-t_0$, have second derivative $-\omega^2$ times themselves. Linearity then shows any combination $A\cos\omega\tau+B\sin\omega\tau$ is a solution. Its initial values are $\eta(0)=A$ and $\dot\eta(0)=\omega B$, so

$$
\boxed{\eta(t)=\eta_0\cos\omega\tau+\frac{v_0}{\omega}\sin\omega\tau.}
$$

Why does this include every solution for those data? Suppose another twice-differentiable solution exists and subtract the displayed one. The difference $z$ obeys $\ddot z+\omega^2z=0$ and has $z(t_0)=\dot z(t_0)=0$. Multiply the equation by $\dot z$:

$$
\frac d{dt}\left(\frac12\dot z^2+\frac12\omega^2z^2\right)=0.
$$

The quantity in parentheses is initially zero, hence always zero. Both terms are nonnegative, so $z=\dot z=0$. The candidate is the unique solution on the interval. This is an energy-based uniqueness proof specific to the equation, not an unexplained appeal to a general differential-equation theorem.

The angular frequency $\omega$ has units inverse time and the period is $2\pi/\omega$. A convenient amplitude is $A_{\rm amp}=\sqrt{\eta_0^2+(v_0/\omega)^2}$, because coefficients of a sine/cosine combination determine its maximum magnitude. This is also immediate from the conserved quantity: $\dot\eta^2+\omega^2\eta^2=\omega^2A_{\rm amp}^2$.

<a name="section-4"></a>

## 3. Constant forcing means a displaced equilibrium

For $m\ddot q+kq=F_0$ with $m,k>0$ and constant $F_0$, set $q_*=F_0/k$ and $\eta=q-q_*$. Since $q_*$ is constant, $\ddot\eta=\ddot q$, and substitution gives $m\ddot\eta+k\eta=0$. Thus

$$
q(t)=q_*+(q_0-q_*)\cos\omega\tau+\frac{v_0}{\omega}\sin\omega\tau,
\qquad \omega=\sqrt{k/m}.
$$

**Worked mathematics example:** $\ddot q+4q=8$, $q(0)=1$, $\dot q(0)=2$. The equilibrium is 2, so

$$
q(t)=2-\cos2t+\sin2t.
$$

Differentiating twice yields $\ddot q=4\cos2t-4\sin2t$; adding $4q$ gives 8. Initial position is $2-1=1$ and initial derivative is 2. No small-displacement approximation was used: the equation was already linear. In a nonlinear system the corresponding result is only a local approximation unless proved otherwise.

<a name="section-5"></a>

## 4. Exponential growth and what “unstable” means

For $\ddot\eta-\kappa^2\eta=0$, $\kappa>0$, direct differentiation gives candidate solutions $e^{\kappa\tau}$ and $e^{-\kappa\tau}$. To derive completeness without complex numbers, define $w=\dot\eta-\kappa\eta$. Then

$$
\dot w=\ddot\eta-\kappa\dot\eta=-\kappa(\dot\eta-\kappa\eta)=-\kappa w.
$$

Multiplying by $e^{\kappa\tau}$ gives $d(e^{\kappa\tau}w)/dt=0$, so $w=C e^{-\kappa\tau}$. Now $\dot\eta-\kappa\eta=C e^{-\kappa\tau}$. Multiply by $e^{-\kappa\tau}$ and integrate:

$$
\frac d{dt}(e^{-\kappa\tau}\eta)=C e^{-2\kappa\tau}
\quad\Longrightarrow\quad \eta=Ae^{\kappa\tau}+Be^{-\kappa\tau}.
$$

Both constants follow from $A+B=\eta_0$ and $\kappa(A-B)=v_0$:

$$
A=\frac12(\eta_0+v_0/\kappa),\qquad B=\frac12(\eta_0-v_0/\kappa).
$$

Generic arbitrarily small initial disturbances have $A\ne0$ and eventually grow. A finely chosen initial condition with $A=0$ decays, but that does not make the equilibrium stable: stability requires control of **all sufficiently small** state disturbances. If the equation is only a linearization, exponential growth predicts departure from the small-neighborhood regime, not an infinitely growing physically exact trajectory.

For $\ddot\eta=0$, solutions are $\eta_0+v_0\tau$. Vanishing linear stiffness removes a linear restoring term; it does not alone settle the nonlinear stability of the original system.

<a name="section-6"></a>

## 5. Derive local linearization from the nonlinear equation

Suppose a one-coordinate conservative model has

$$
L=\frac12 A(q)\dot q^2-V(q),\qquad A(q)>0.
$$

Here $A$ is an inertia coefficient, not a new matrix. Differentiate:

$$
L_{\dot q}=A\dot q,\qquad \frac d{dt}L_{\dot q}=A\ddot q+A'\dot q^2,
\quad L_q=\frac12A'\dot q^2-V',
$$

so

$$
A(q)\ddot q+\frac12A'(q)\dot q^2+V'(q)=0.
$$

A resting equilibrium $q_*$ satisfies $V'(q_*)=0$. Put $q=q_*+\varepsilon\eta$, $\dot q=\varepsilon\dot\eta$, $\ddot q=\varepsilon\ddot\eta$. Taylor expansion gives $A(q)=A(q_*)+O(\varepsilon)$ and $V'(q)=\varepsilon V''(q_*)\eta+O(\varepsilon^2)$, while the velocity-squared term is $O(\varepsilon^2)$. Keeping the first-order terms and dividing by $\varepsilon$ yields

$$
\boxed{A(q_*)\ddot\eta+V''(q_*)\eta=0.}
$$

For $V''(q_*)>0$, the linearized angular frequency is $\sqrt{V''(q_*)/A(q_*)}$. For negative curvature there is an exponential growing direction with rate $\sqrt{-V''(q_*)/A(q_*)}$. Dimensions agree because $[V'']=\mathrm{energy}/[q]^2$ and $[A]=\mathrm{energy}\,\mathrm{time}^2/[q]^2$.

This derivation assumes smooth coefficients, a genuine regular equilibrium and sufficiently small disturbances for the neglected terms to remain small. For a reduced effective potential at **fixed conserved momentum**, hold that momentum fixed when differentiating. For a system driven at fixed angular speed, hold the prescribed speed fixed instead. These are different physical restrictions, as the spherical-pendulum and rotating-hoop problems demonstrate.

<a name="section-7"></a>

## 6. Positive, negative and zero curvature are different cases

In a fixed one-coordinate conservative model, $E=A(q)\dot q^2/2+V(q)$ is conserved. If $q_*$ is an isolated strict local minimum, sufficiently small initial energy above $V(q_*)$ cannot cross a nearby potential barrier. Positivity of $A$ then bounds both position and velocity locally. This supplies a physical energy proof of local stability, stronger than merely finding sinusoidal solutions of a linear approximation.

A local maximum with $V''<0$ is unstable: the linearized exponential describes the initial departure, and the local force points away. If $V''=0$, inspect higher-order terms. For $V=\lambda\eta^4/4$ with $\lambda>0$, zero is still a strict minimum and the energy argument gives nonlinear stability even though the linear equation has no restoring term. For $V=-\lambda\eta^4/4$ the force drives a displaced particle away. The same zero quadratic coefficient can occur in both cases.

A zero linear frequency is therefore not enough to label an equilibrium stable or unstable. It means the quadratic approximation is insufficient. For an expanding hoop or other prescribed time-dependent geometry, ordinary mechanical energy may not be conserved, so the fixed-potential energy argument cannot be transplanted without checking the model.

<a name="section-8"></a>

## 7. Damping: what is needed for this lecture's exercises

The mixed set asks you to derive, rather than explicitly solve in all regimes, $m\ddot q+b\dot q+kq=0$. Multiplying by $\dot q$ gives

$$
\frac d{dt}\left(\frac12m\dot q^2+\frac12kq^2\right)=-b\dot q^2\le0\quad(b\ge0).
$$

This proves that the stated physical energy cannot increase. It does not require complex roots. A full classification into underdamped, critically damped and overdamped solutions is not used in the assigned questions and is not silently assumed. The integrating-factor Lagrangian construction in M09 uses only the product rule; it is a change in dynamical description, not a new ODE solution technique.

<a name="section-9"></a>

## Practice and self-check

Attempt **N9–N14** in [AM01 New Mathematics Practice](am01-new-mathematics-practice.md) if these methods are unfamiliar. Use [three progressive hints per question](am01-new-mathematics-hints.md) and [separate solutions](am01-new-mathematics-solutions.md). They are additional mathematics practice, not part of either formal physics set.

Before the transfer problems, be able to (1) determine the two constants from position and velocity, (2) verify a proposed solution, (3) derive a linearized equation by tracking orders of smallness, and (4) explain why zero curvature requires more information. Return to [Theoretical Mechanics Lecture 01 Dashboard](../../theoretical-mechanics/lecture-01/README.md).

[Section index](README.md) · [Home](../../README.md)
