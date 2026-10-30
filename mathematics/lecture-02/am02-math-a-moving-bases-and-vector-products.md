<a name="section-1"></a>

# AM02 Math A — Moving Bases and Vector Products

> **Edition scope:** original AI-assisted supplement or study material. Some prerequisite lessons are withheld for source review; their titles are plain text, not unavailable links. [Attribution and scope](../../SOURCES.md#pending).


> **Review status: unverified.** AI-assisted educational draft; human scientific review remains pending. [Sources and limitations](../../SOURCES.md).


**AI SUPPLEMENT**, needed for Units 02.2, 02.3, 02.6 and 02.7 (source motivation P043–P050, P304–P332). AP BC supplies ordinary differentiation; Lecture 01 supplies dot products and partial derivatives. We add cross products and differentiation of a moving basis, without requiring tensors or Euler angles.

<a name="section-2"></a>

## 1. A basis is part of the function

A vector $\mathbf u=u_x\mathbf e_x+u_y\mathbf e_y$ has components and directions. Fixed Cartesian basis vectors have zero derivative. In polar coordinates $\mathbf e_r=(\cos\theta,\sin\theta)$ and $\mathbf e_\theta=(-\sin\theta,\cos\theta)$ change with $\theta$. Component differentiation gives $\dot{\mathbf e}_r=\dot\theta\mathbf e_\theta$ and $\dot{\mathbf e}_\theta=-\dot\theta\mathbf e_r$. Consequently
$$
\frac d{dt}(u_r\mathbf e_r+u_\theta\mathbf e_\theta)
=(\dot u_r-\dot\theta u_\theta)\mathbf e_r+(\dot u_\theta+\dot\theta u_r)\mathbf e_\theta.
$$
Apply this first to $\mathbf r=r\mathbf e_r$ and then its velocity to obtain the polar acceleration. The product rule already known from calculus supplies every term. A constant magnitude is not a constant vector: $R\mathbf e_r(\omega t)$ has derivative $R\omega\mathbf e_\theta$.

<a name="section-3"></a>

## 2. Define the cross product by components

In a right-handed orthonormal basis,
$$
\mathbf a\times\mathbf b=(a_yb_z-a_zb_y,\ a_zb_x-a_xb_z,\ a_xb_y-a_yb_x).
$$
It is bilinear and antisymmetric because each component is a difference of two bilinear products. Direct dotting shows $\mathbf a\cdot(\mathbf a\times\mathbf b)=\mathbf b\cdot(\mathbf a\times\mathbf b)=0$: paired terms cancel. For $\mathbf a=a\mathbf e_x$ and $\mathbf b=b(\cos\gamma\mathbf e_x+\sin\gamma\mathbf e_y)$, the result is $ab\sin\gamma\mathbf e_z$. Thus the magnitude is parallelogram area and the direction follows the right-hand rule. The sign encodes orientation, essential for Lorentz and Coriolis forces.

Expanding the six terms of $\mathbf a\cdot(\mathbf b\times\mathbf c)$ gives
$$
a_xb_yc_z+a_yb_zc_x+a_zb_xc_y-a_xb_zc_y-a_yb_xc_z-a_zb_yc_x.
$$
Cyclic relabeling leaves these terms unchanged; swapping two vectors changes sign. Therefore $\mathbf v\cdot(\boldsymbol\Omega\times\mathbf r)=\mathbf r\cdot(\mathbf v\times\boldsymbol\Omega)$, not $\mathbf r\cdot(\boldsymbol\Omega\times\mathbf v)$.

For the double cross product, expand its $x$ component:
$$
[\mathbf a\times(\mathbf b\times\mathbf c)]_x
=a_y(b_xc_y-b_yc_x)-a_z(b_zc_x-b_xc_z)
=b_x(\mathbf a\cdot\mathbf c)-c_x(\mathbf a\cdot\mathbf b).
$$
The inserted $a_xb_xc_x$ terms cancel; the $y,z$ expansions have the same pattern. Hence
$$
\boxed{\mathbf a\times(\mathbf b\times\mathbf c)=\mathbf b(\mathbf a\cdot\mathbf c)-\mathbf c(\mathbf a\cdot\mathbf b).}
$$
This proof explains the parentheses: cross products are not associative. Squaring the component definition and grouping terms also gives $|\mathbf a\times\mathbf b|^2=a^2b^2-(\mathbf a\cdot\mathbf b)^2$.

<a name="section-4"></a>

## 3. Rotation and the transport theorem

A small rotation $d\alpha$ around $z$ changes $(x,y,z)$ to $(x-y\,d\alpha,y+x\,d\alpha,z)$ to first order, by the sine/cosine rotation formula. The increment is $d\alpha\,\mathbf e_z\times\mathbf r$. The same geometric statement holds around any unit axis $\mathbf n$: choose a right-handed basis with that axis as $z$ and rotate back. Thus a rigid rotating basis satisfies $\dot{\mathbf e}'_i=\boldsymbol\Omega\times\mathbf e'_i$.

For $\mathbf u=\sum_i u_i\mathbf e'_i$, the product rule yields
$$
\left(\frac{d\mathbf u}{dt}\right)_I
=\sum_i\dot u_i\mathbf e'_i+\sum_i u_i\boldsymbol\Omega\times\mathbf e'_i
=\boxed{\left(\frac{D\mathbf u}{dt}\right)_R+\boldsymbol\Omega\times\mathbf u.}
$$
$D/dt$ changes only the components in rotating axes. The result assumes a differentiable rigid orthonormal frame; arbitrary deforming bases require additional terms. Applying it twice to position produces the two Coriolis terms in Unit 02.6.

**Worked check:** a vector fixed in inertial space has zero inertial derivative, so $D\mathbf u/dt=-\boldsymbol\Omega\times\mathbf u$. Its components rotate oppositely to the frame. Its length remains fixed because $D(u^2)/dt=-2\mathbf u\cdot(\boldsymbol\Omega\times\mathbf u)=0$.

<a name="section-5"></a>

## 4. Vector-gradient notation is three ordinary derivatives

For a scalar $f(x,y,z)$, $\nabla f=(f_x,f_y,f_z)$. Hold $\mathbf v,\boldsymbol\Omega$ fixed when differentiating $L$ with respect to $\mathbf r$. The scalar triple product immediately gives
$$
\nabla_{\mathbf r}[\mathbf v\cdot(\boldsymbol\Omega\times\mathbf r)]=\mathbf v\times\boldsymbol\Omega.
$$
Similarly use $|\boldsymbol\Omega\times\mathbf r|^2=\Omega^2r^2-(\boldsymbol\Omega\cdot\mathbf r)^2$ and the component chain rule to obtain
$$
\nabla_{\mathbf r}\tfrac12|\boldsymbol\Omega\times\mathbf r|^2
=\Omega^2\mathbf r-(\boldsymbol\Omega\cdot\mathbf r)\boldsymbol\Omega.
$$
For $\boldsymbol\Omega=\Omega\mathbf e_z$, the result is $(\Omega^2x,\Omega^2y,0)$, correctly perpendicular to the axis. It has acceleration units if $\mathbf r$ is a length.

**Independent check:** explain why cross-product order reverses the sign of Coriolis force. Then attempt M01–M04 in [AM02 Additional Mathematics Practice](am02-additional-mathematics-practice.md), with separate [hints](am02-additional-mathematics-hints.md) and [solutions](am02-additional-mathematics-solutions.md).

基矢 — basis vector; 叉积 — cross product; 标量三重积 — scalar triple product; 运输定理 — transport theorem.

[Section index](README.md) · [Home](../../README.md)
