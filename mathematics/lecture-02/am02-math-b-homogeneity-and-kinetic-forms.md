<a name="section-1"></a>

# AM02 Math B — Homogeneity and Kinetic Forms

> **Edition scope:** original AI-assisted supplement or study material. Some prerequisite lessons are withheld for source review; their titles are plain text, not unavailable links. [Attribution and scope](../../SOURCES.md#pending).


> **Review status: unverified.** AI-assisted educational draft; human scientific review remains pending. [Sources and limitations](../../SOURCES.md).


**AI SUPPLEMENT**, motivated by P076–P080 and P240–P265. Reuse [AM01 Math 6 - Linear Algebra for Constraints](../lecture-01/am01-math-6-linear-algebra-for-constraints.md) for matrices and linear systems. This note adds homogeneous functions, positive quadratic kinetic forms and a one-coordinate path metric; it does not repeat basic elimination or introduce normal-mode theory.

<a name="section-2"></a>

## 1. Degree means scaling selected variables

Hold $q,t$ fixed. A function $f(\mathbf v)$ is homogeneous of degree $k$ when $f(\lambda\mathbf v)=\lambda^kf(\mathbf v)$ for positive $\lambda$ in its domain. Examples are $av_x+bv_y$ (degree 1) and $av_x^2+2cv_xv_y+bv_y^2$ (degree 2), even if coefficients depend on $q,t$. A constant in $\mathbf v$ has degree 0. A sum of different degrees is not homogeneous.

Differentiate the scaling equation with respect to $\lambda$ at $\lambda=1$. The multivariable chain rule gives
$$
\sum_i v_i\frac{\partial f}{\partial v_i}=kf.
$$
This proves Euler's homogeneous-function identity for differentiable $f$ on a domain allowing such scaling. It is not a new dynamical law. Applied separately to $T_0,T_1,T_2$, it gives $\sum\dot q_iT_{\dot q_i}=T_1+2T_2$.

**Worked cross-term check:** for $f=av_1^2/2+cv_1v_2+bv_2^2/2$, the derivatives are $av_1+cv_2$ and $cv_1+bv_2$. Multiplying by the respective velocities and adding gives $av_1^2+2cv_1v_2+bv_2^2=2f$. The mixed term must contribute twice.

<a name="section-3"></a>

## 2. Why a mass matrix can contain negative entries

For $2T=A u^2+2Cuv+Bv^2$ with $A>0$, complete the square:
$$
2T=A(u+Cv/A)^2+(B-C^2/A)v^2.
$$
Thus $T>0$ for every nonzero $(u,v)$ precisely when $AB-C^2>0$. Necessity follows by choosing $u=-Cv/A$; sufficiency follows from the two positive squares. Individual entries need not be positive. For example $A=B=2,C=-1$ is positive definite, while $A=B=1,C=2$ is indefinite despite positive entries.

For a general point-mass coordinate map, $M_{ij}=\sum_am_a\mathbf r_{a,q_i}\cdot\mathbf r_{a,q_j}$. For a vector of coordinate rates $\mathbf w$,
$$
\mathbf w^TM\mathbf w=\sum_am_a\left|\sum_i\mathbf r_{a,q_i}w_i\right|^2\ge0.
$$
It is strictly positive for nonzero $\mathbf w$ if the tangent map has independent columns. If a nonzero coordinate rate causes no physical displacement, the coordinates are redundant or singular. Positivity of this form has no implication that unilateral contact remains active.

For the double pendulum, $A=(m_1+m_2)l_1^2$, $B=m_2l_2^2$, $C=m_2l_1l_2\cos\Delta$. Then $AB-C^2=m_2l_1^2l_2^2(m_1+m_2\sin^2\Delta)>0$. This guarantees unique instantaneous accelerations from the two linear acceleration equations. It does not solve the nonlinear trajectory.

<a name="section-4"></a>

## 3. Coordinate-dependent inertia is geometry

For a fixed path $\mathbf r=\mathbf r(s)$ with regular parameter $s$, speed is $|\mathbf r'(s)|\dot s$ and $T=mh(s)\dot s^2/2$, where $h=\mathbf r'\cdot\mathbf r'>0$. The kinetic equation gives
$$
h\ddot s+\tfrac12h'\dot s^2=-\frac1mV'(s).
$$
To understand the extra term, introduce local arc length $\ell(s)=\int^s\sqrt{h(u)}du$. Then
$$
\dot\ell=\sqrt h\dot s,\qquad
\ddot\ell=\sqrt h\ddot s+\frac{h'}{2\sqrt h}\dot s^2.
$$
The equation becomes $m\ddot\ell=-dV/d\ell$, ordinary tangent Newton dynamics. The extra term is a coordinate effect, not a new force. Arc length is monotone where $h>0$ and so provides a valid local coordinate.

For the conical spiral, $h=1+a^2+a^2b^2z^2$. From rest, conservation gives $\dot z=-\sqrt{2g(z_0-z)/h(z)}$ on the downward branch. The time to $z_1<z_0$ is
$$
t=\int_{z_1}^{z_0}\sqrt{\frac{h(z)}{2g(z_0-z)}}\,dz.
$$
The endpoint singularity is integrable, as AP BC shows from $\int_0^\epsilon u^{-1/2}du=2\sqrt\epsilon$. A finite travel time need not have an elementary antiderivative.

<a name="section-5"></a>

## 4. General velocity-linear terms

For one coordinate $L=A(q,t)\dot q^2/2+B(q,t)\dot q-C(q,t)$,
$$
p=A\dot q+B,\qquad E_L=A\dot q^2/2+C.
$$
The equation is
$$
A\ddot q+\tfrac12A_q\dot q^2+A_t\dot q+B_t+C_q=0.
$$
To derive it, differentiate $p$: $\dot p=A\ddot q+A_q\dot q^2+A_t\dot q+B_q\dot q+B_t$, then subtract $L_q=A_q\dot q^2/2+B_q\dot q-C_q$. The $B_q\dot q$ terms cancel. If $B$ depends only on $q$ on an interval, $B\dot q=d[\int B(q)dq]/dt$ is removable; if $B$ depends on time, the residual $B_t$ need not vanish. In multiple dimensions a velocity-linear term is not generally a total derivative; curl diagnoses that obstruction in Math C.

**Independent check:** a quadratic kinetic form can be positive even with a negative off-diagonal coefficient. Explain by a square completion, then attempt M05–M08 in [AM02 Additional Mathematics Practice](am02-additional-mathematics-practice.md). [Hints](am02-additional-mathematics-hints.md) and [solutions](am02-additional-mathematics-solutions.md) remain separate.

齐次性 — homogeneity; 二次型 — quadratic form; 正定 — positive definite; 弧长 — arc length.

[Section index](README.md) · [Home](../../README.md)
