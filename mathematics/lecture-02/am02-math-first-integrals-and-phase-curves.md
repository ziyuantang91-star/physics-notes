<a name="section-1"></a>

# AM02 Mathematics — First Integrals and Phase Curves

> **Edition scope:** original AI-assisted supplement or study material. Some prerequisite lessons are withheld for source review; their titles are plain text, not unavailable links. [Attribution and scope](../../SOURCES.md#pending).


> **Review status: unverified.** AI-assisted educational draft; human scientific review remains pending. [Sources and limitations](../../SOURCES.md).


**AI SUPPLEMENT for Unit 02.1.** The new task is to interpret a nonlinear motion law without a closed-form solution. This note assumes single-variable calculus and Lecture 01 chain rule. [AM01 Math 7 - Second Order Equations and Stability](../lecture-01/am01-math-7-second-order-equations-and-stability.md) already teaches linearization, harmonic solutions and exponential instability; those topics are referenced, not assigned again.

<a name="section-2"></a>

## 1. Turn a second-order equation into a pair of rates

For $\ddot q+f(q)=0$, define $v=\dot q$. A state is the ordered pair $(q,v)$, because position alone does not tell us which way the motion proceeds. The equation says
$$
\dot q=v,\qquad \dot v=-f(q).
$$
A **phase curve** is the path of $(q(t),v(t))$ in this two-dimensional state plane. It is not a spatial orbit. At a state $(q,v)$ the direction of motion is $(v,-f(q))$. In particular the curve moves toward increasing $q$ when $v>0$.

Where $v\ne0$, the chain rule gives $dv/dq=\dot v/\dot q=-f(q)/v$. Dividing by $v$ is invalid at a turning point. The time-based derivation below avoids that problem.

<a name="section-3"></a>

## 2. Derive a first integral without dividing by velocity

Suppose $f$ is continuous and has an antiderivative $W$, with $W'(q)=f(q)$. The ordinary chain rule gives
$$
\frac d{dt}\left[\frac12v^2+W(q)\right]
=v\dot v+W'(q)\dot q=v[-f(q)]+f(q)v=0.
$$
Thus $H=v^2/2+W(q)$ is constant along every twice-differentiable solution, including at $v=0$. A **first integral** is such a constant-along-solutions quantity. Its formula need not be free of explicit $t$ in other problems: for $\ddot q=a$, $\dot q-at$ is constant even though its expression contains $t$.

At a fixed $H=h$, permitted phase points satisfy
$$
v=\pm\sqrt{2[h-W(q)]},\qquad W(q)\le h.
$$
The zero-velocity points $W(q)=h$ are candidate turning points. If also $f(q)=0$, the point is an equilibrium and may instead be approached only in infinite time. Energy alone describes the geometric curve; the original differential equations determine direction and timing.

<a name="section-4"></a>

## 3. Apply it to the hoop and distinguish three regimes

For $q=\theta$ and $f(q)=\omega^2\sin q$, choose $W(q)=\omega^2(1-\cos q)$, so $H=\mathcal E/I$. With $\omega\ne0$, define dimensionless variables $u=v/|\omega|$ and $h=H/\omega^2$. Then
$$
h=\frac12u^2+1-\cos q.
$$
The effective potential has minimum 0 at $q=2k\pi$ and maximum 2 at $q=(2k+1)\pi$.

For $0<h<2$, solving $1-\cos A=h$ gives a finite turning amplitude $0<A<\pi$. Speeds vanish at $\pm A$ and switch sign there because $\dot v=-\omega^2\sin(\pm A)$ points back into the allowed region. For $h>2$, $v$ never vanishes, so its sign stays fixed and $q$ passes through all angular cells. The threshold $h=2$ is the **separatrix** between these behaviors, together with the unstable equilibrium points on its boundary.

At a turning point the phase-curve slope $dv/dq$ can be infinite while the time solution remains smooth: $\dot q=0$ and $\dot v\ne0$. This is a failure of using position as the independent variable there, not a physical singularity.

<a name="section-5"></a>

## 4. Separate variables carefully to obtain elapsed time

On a branch with specified sign and nonzero speed,
$$
dt=\frac{dq}{v(q)}.
$$
For example, the upward separatrix on $-\pi<q<\pi$ has
$$
v=2|\omega|\cos(q/2),
$$
because $1+\cos q=2\cos^2(q/2)$ and cosine is positive on that interval. Starting at $q=0$, its arrival time at $q$ is
$$
t(q)=\frac1{2|\omega|}\int_0^q\sec(s/2)\,ds
=\frac1{|\omega|}\ln[\sec(q/2)+\tan(q/2)].
$$
To check the antiderivative, differentiate $\ln(\sec z+\tan z)$: its derivative is $(\sec z\tan z+\sec^2z)/(\sec z+\tan z)=\sec z$; substitution $z=s/2$ supplies the factor 2.

For $q=\pi-\epsilon$ with small $\epsilon>0$, $\cos(q/2)=\sin(\epsilon/2)\sim\epsilon/2$ and $\sin(q/2)\sim1$. Hence $\sec(q/2)+\tan(q/2)\sim4/\epsilon$, so $t\sim|\omega|^{-1}\ln(4/\epsilon)\to\infty$. Reaching the top at zero speed in a finite time is not permitted by this separatrix solution.

<a name="section-6"></a>

## 5. Finite-amplitude period from an ordinary integral

For libration with turning amplitude $A\in(0,\pi)$, conservation gives
$$
v^2=2\omega^2(\cos q-\cos A).
$$
By symmetry, the period is four times the time from 0 to $A$ on the increasing branch:
$$
\mathcal T(A)=\frac4{|\omega|}\int_0^A\frac{dq}{\sqrt{2(\cos q-\cos A)}}.
$$
The speed vanishes at $A$, but this improper integral is finite for $A<\pi$. In fact $\cos q-\cos A\sim\sin A(A-q)$ there, so its integrand scales as $(A-q)^{-1/2}$, whose integral is finite. This differs from the logarithmic separatrix singularity.

A substitution makes the small-amplitude limit transparent. Let $k=\sin(A/2)$ and $\sin(q/2)=k\sin\psi$, with $0\le\psi\le\pi/2$. Then
$$
\cos q-\cos A=2k^2\cos^2\psi,\qquad
\frac12\cos(q/2)dq=k\cos\psi\,d\psi,
$$
$$
dq=\frac{2k\cos\psi}{\sqrt{1-k^2\sin^2\psi}}d\psi.
$$
Cancel the common positive factors in the interior and take endpoint limits:
$$
\boxed{\mathcal T(A)=\frac4{|\omega|}\int_0^{\pi/2}\frac{d\psi}{\sqrt{1-k^2\sin^2\psi}}.}
$$
For $0<k<1$, the integrand is greater than 1 on the interior and at most $1/\sqrt{1-k^2}$. Consequently
$$
\frac{2\pi}{|\omega|}<\mathcal T(A)\le
\frac{2\pi}{|\omega|\sqrt{1-k^2}}.
$$
As $A\to0$, $k\to0$ and these lower and upper bounds approach the same value $2\pi/|\omega|$. The exact finite-amplitude period is longer than the small-oscillation value. The integral is sometimes named an elliptic integral; no elliptic-function methods are needed or assumed here. As $A\to\pi$, the limiting integrand is $\sec\psi$ and the integral diverges, consistent with the separatrix calculation. One can justify divergence by integrating only to any fixed $b<\pi/2$ first, taking the limit there, and then taking $b\to\pi/2$.

<a name="section-7"></a>

## Practice and terminology

Complete [N1–N4](am02-mathematics-practice.md) as needed; [three-stage hints](am02-mathematics-hints.md) and [separate worked solutions](am02-mathematics-solutions.md) are available. These four problems support the new interpretation tools; they do not repeat the Lecture 01 pilot.

| 中文 | English | Distinction |
| --- | --- | --- |
| 运动积分 | first integral | Constant on a dynamical solution |
| 相平面／相曲线 | phase plane / phase curve | State space and a trajectory within it |
| 等值线 | level curve | Points satisfying a fixed value of a function |
| 转向点 | turning point | Zero speed; inspect acceleration too |
| 分界轨道 | separatrix | Threshold dividing libration and rotation |
| 求积 | quadrature | Expressing a solution or elapsed time by an integral |
| 反常积分 | improper integral | Integral evaluated through a limiting endpoint |

Return to AM02 Unit 02-1 - Bead on a Rotating Hoop (not included; [edition scope](../../SOURCES.md#pending)).

[Section index](README.md) · [Home](../../README.md)
