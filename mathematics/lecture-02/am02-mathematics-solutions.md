<a name="section-1"></a>

# AM02 — Mathematics Worked Solutions

> **Edition scope:** original AI-assisted supplement or study material. Some prerequisite lessons are withheld for source review; their titles are plain text, not unavailable links. [Attribution and scope](../../SOURCES.md#pending).


> **Review status: unverified.** AI-assisted educational draft; human scientific review remains pending. [Sources and limitations](../../SOURCES.md).


**Spoiler boundary:** full worked solutions follow. “Independent check” means an alternative calculation or symbolic/numerical verification, not a second human reviewer or demonstrated learner mastery.

<a name="section-2"></a>

## AM02-N1

**Construct a first integral from a nonlinear equation** · [Question](am02-mathematics-practice.md#section-2)

$$
\frac d{d\tau}\left[\frac12q'^2+\frac32q^2+\frac14q^4\right]
=q'(q''+3q+q^3)=0.
$$
Thus $H=7/4$ for the initial data. At zero, $q'^2/2=7/4$, so the speed is $\sqrt{7/2}$. Initially $q''=-4$, selecting negative $q'$ at the first passage. Turning points satisfy $q^4+6q^2-7=0$. Put $z=q^2\ge0$: $(z-1)(z+7)=0$, hence $q=\pm1$. The potential increases strictly with $|q|$ away from zero, so the orbit stays between these two points. Differentiation verifies the integral even at the initial zero velocity.

**Independent check:** Differentiate the proposed integral and solve the turning polynomial exactly.

**Common mistakes:** Dividing by zero at the initial point; reporting both velocity signs without choosing the first passage.

**Review prerequisites:** [AM02 Math - First Integrals and Phase Curves](am02-math-first-integrals-and-phase-curves.md)

<a name="section-3"></a>

## AM02-N2

**A phase ellipse is not a spatial orbit** · [Question](am02-mathematics-practice.md#section-3)

Conservation gives $v^2+\kappa^2q^2=\kappa^2A^2$, or $q^2/A^2+v^2/(\kappa A)^2=1$. With $q$ horizontal and $v$ vertical, the path starts downwards at the rightmost point and traverses the ellipse clockwise. Where $v\ne0$, $dv/dq=-\kappa^2q/v$. It is undefined at $(\pm A,0)$, the vertical-tangent turning points. Yet $q=A\cos\kappa t$ and $v=-A\kappa\sin\kappa t$ have derivatives of all orders there. For example at $t=0$, $\dot q=0$ but $\dot v=-\kappa^2A$ is finite. The state space uses one coordinate and its speed, not two spatial directions. Direct differentiation verifies both rate equations and the initial conditions.

**Independent check:** Substitute the explicit harmonic solution into the ellipse and both first-order rates.

**Common mistakes:** Calling a vertical phase tangent infinite acceleration; choosing the direction from the ellipse alone.

**Review prerequisites:** [AM02 Math - First Integrals and Phase Curves](am02-math-first-integrals-and-phase-curves.md) · [AM01 Math 7 - Second Order Equations and Stability](../lecture-01/am01-math-7-second-order-equations-and-stability.md)

<a name="section-4"></a>

## AM02-N3

**An infinite-time approach with finite distance** · [Question](am02-mathematics-practice.md#section-4)

The initial level is $H=2\omega^2$. Therefore $v^2=2\omega^2(1+\cos q)=4\omega^2\cos^2(q/2)$. Continuity and the positive initial velocity select $v=2\omega\cos(q/2)$ until the asymptotic top. Integrating gives
$$
t(q)=\frac1\omega\ln[\sec(q/2)+\tan(q/2)].
$$
At zero this is zero. Its derivative is $1/[2\omega\cos(q/2)]$, which checks both the integration and the initial speed. At $q=\pi-\epsilon$, the logarithm's argument is asymptotic to $4/\epsilon$, so $t\sim\omega^{-1}\ln(4/\epsilon)\to\infty$. The reciprocal speed becomes nonintegrable near the endpoint; finite distance alone does not constrain how fast the particle slows. The conclusion concerns this nonstationary trajectory; $q=\pi,v=0$ is separately an exact stationary solution.

**Independent check:** Check the derivative of the time formula, initial data, energy identity and endpoint asymptotic.

**Common mistakes:** Taking the endpoint velocity to zero and then declaring arrival; confusing the stationary solution with the approaching trajectory.

**Review prerequisites:** [AM02 Math - First Integrals and Phase Curves](am02-math-first-integrals-and-phase-curves.md)

<a name="section-5"></a>

## AM02-N4

**Bound the nonlinear period without special functions** · [Question](am02-mathematics-practice.md#section-5)

Four symmetric quarter passages give
$$
\mathcal T=\frac4\omega\int_0^A\frac{dq}{\sqrt{2(\cos q-\cos A)}}.
$$
Under $\sin(q/2)=k\sin\psi$, the numerator is $dq=2k\cos\psi\,d\psi/\sqrt{1-k^2\sin^2\psi}$ and the denominator is $2k\cos\psi$. Hence
$$
\mathcal T=\frac4\omega\int_0^{\pi/2}(1-k^2\sin^2\psi)^{-1/2}d\psi.
$$
For $k=1/2$, the integrand is between 1 and $2/\sqrt3$, giving $2\pi/\omega<\mathcal T<4\pi/(\sqrt3\omega)$. Both bounds are strict for this nonzero amplitude because neither extreme holds throughout the interval. For general $A\to0$, the non-strict bounds $2\pi/\omega\le\mathcal T\le2\pi/[\omega\sqrt{1-k^2}]$ squeeze the period to $2\pi/\omega$. For every finite $0<A<\pi$, the integrand exceeds 1 on a nonzero interval, so the exact period is larger. Numerical quadrature gives $\omega\mathcal T\approx6.7430$, between $6.2832$ and $7.2552$, but the inequalities were proved without relying on that decimal.

**Independent check:** Check the substitution algebra and evaluate the bounded integral numerically as a separate check.

**Common mistakes:** Setting the integrand equal to its limiting value for finite amplitude; assuming an endpoint speed of zero makes every period infinite.

**Review prerequisites:** [AM02 Math - First Integrals and Phase Curves](am02-math-first-integrals-and-phase-curves.md)

[Section index](README.md) · [Home](../../README.md)
