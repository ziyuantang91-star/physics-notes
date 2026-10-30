<a name="section-1"></a>

# AM01 Math 6 — Linear Algebra for Independent Constraints

> **Edition scope:** original AI-assisted supplement or study material. Some prerequisite lessons are withheld for source review; their titles are plain text, not unavailable links. [Attribution and scope](../../SOURCES.md#pending).


> **Review status: unverified.** AI-assisted educational draft; human scientific review remains pending. [Sources and limitations](../../SOURCES.md).


**AI SUPPLEMENT, motivated by P086–P095, P159–P176 and P238–P253; SC-04, SC-07–SC-09.** This is the one substantial new mathematics prerequisite added to the five pilot topics. It develops finite linear systems, independence, rank, null spaces and constraint normals as one connected technique. The original 27 mathematics exercises are optional reference, not a progression gate.

Prerequisites: differentials and dot products (not included; [edition scope](../../SOURCES.md#pending)) and coordinate changes (not included; [edition scope](../../SOURCES.md#pending)). We use ordinary finite sums, not infinite-series manipulations.

<a name="section-2"></a>

## 1. Why one equation need not remove one freedom

For three infinitesimal coordinate changes $(u,v,w)$, the equations $u+v+w=0$ and $2u+2v+2w=0$ express one restriction twice. Choosing $v,w$ determines $u=-v-w$: two free parameters remain. Adding $v-w=0$ leaves only $w$ free: $(u,v,w)=w(-2,1,1)$. Counting written equations would give the wrong answer in the first case.

A **linear combination** of vectors means multiply each vector by a scalar and add. Vectors are **independent** when the only combination giving zero has every coefficient zero. For example, $c_1(1,1,1)+c_2(0,1,-1)=0$ gives $c_1=0$ from the first component, then $c_2=0$. The extra row $(2,2,2)$ is dependent because it is twice the first row.

The **span** of vectors is the set of all their linear combinations. A **basis** is an independent list spanning the set. Its number of elements is the **dimension**. These definitions explain “independent directions”; the word does not mean mutually perpendicular.

<a name="section-3"></a>

## 2. Matrices are organized systems of equations

The array

$$
A=\begin{pmatrix}1&1&1\\0&1&-1\end{pmatrix},\quad
\mathbf u=\begin{pmatrix}u\\v\\w\end{pmatrix}
$$

encodes the two equations as $A\mathbf u=0$. By definition the $a$th component of $A\mathbf u$ is $\sum_j A_{aj}u_j$. A row is one equation; a column records the coefficients of one unknown.

Allowed **row operations** are swapping equations, multiplying an equation by a nonzero number, and adding a multiple of one equation to another. Each operation can be undone, so it preserves exactly the solution set. Repeatedly use a nonzero leading coefficient, a **pivot**, to eliminate that variable from other equations. This is Gaussian elimination; no mysterious matrix operation is required.

**Worked pure-mathematics example.** Solve

$$
u+v+w=0,\quad 2u+2v+2w=0,\quad v-w=0.
$$

Subtract twice the first equation from the second: it becomes $0=0$. The third gives $v=w$. Substitute into the first to get $u=-2w$. Thus the complete solution is $w(-2,1,1)$ for arbitrary real $w$. There are two pivots and one free variable. Every proposed solution can be checked in all three original equations.

<a name="section-4"></a>

## 3. Rank, null space and why the counts work

The **null space** $\ker A$ is the set of solutions of $A\mathbf u=0$. It is closed under addition and scalar multiplication, because $A(a\mathbf u+b\mathbf v)=aA\mathbf u+bA\mathbf v$ component by component.

The **rank** $r$ can be computed as the number of pivot rows after elimination. It is also the number of independent original rows: invertible row operations preserve their span, and nonzero echelon rows are independent because successive pivot columns force their coefficients to vanish one at a time.

For $n$ unknowns and $r$ pivots, elimination expresses each pivot variable uniquely in terms of the remaining $n-r$ free variables. Set one free variable to 1 and the others to 0 to construct $n-r$ null vectors. They are independent because their free-variable components are the ordinary coordinate unit vectors; every solution is their combination because its free-variable values specify it completely. Therefore

$$
\boxed{\dim\ker A=n-r.}
$$

This is the rank–nullity count in the form mechanics needs. The proof establishes both existence and independence of the free directions. An inhomogeneous system $A\mathbf u=\mathbf b$ is different: it may have no solution. If $\mathbf u_0$ is one solution, every solution is $\mathbf u_0+\mathbf w$ with $\mathbf w\in\ker A$, since subtracting two solutions gives $A\mathbf w=0$. Such a shifted set need not contain zero; it is called **affine**.

<a name="section-5"></a>

## 4. From nonlinear constraints to a Jacobian

Write $n$ Cartesian components as $X_1,\ldots,X_n$ and impose $k$ smooth equations $f_a(\mathbf X,t)=0$. At a fixed time, their first-order changes are

$$
\delta f_a=\sum_{j=1}^n\frac{\partial f_a}{\partial X_j}\delta X_j=0.
$$

Define the **constraint Jacobian** by $A_{aj}=\partial f_a/\partial X_j$. Each row is the gradient of one constraint. The linearized admissibility condition is $A\delta\mathbf X=0$. At a point where the rows have rank $k$, there are $n-k$ independent tangent directions.

**Worked geometry example.** For a bead on a spatial circle,

$$
f_1=x^2+y^2-R^2=0,\quad f_2=z=0,\quad R>0,
$$

$$
A=\begin{pmatrix}2x&2y&0\\0&0&1\end{pmatrix}.
$$

On the circle $(x,y)\ne(0,0)$, the rows are independent, so rank is 2 and dimension is $3-2=1$. A tangent vector is $(-y,x,0)$: its dot product with both rows is zero. The explicit map $(x,y,z)=(R\cos q,R\sin q,0)$ has derivative $(-R\sin q,R\cos q,0)$, confirming that this linear direction is realized by actual nearby positions.

<a name="section-6"></a>

### Why regularity is necessary

For $f=x^2+y^2=0$, the only real position is the origin. Its gradient is zero there, so the linear equation says $0=0$ and falsely allows every first-order direction if interpreted as actual configurational freedom. The failure is in using a singular linearization, not in row reduction. Similarly $f^2=0$ describes the same zero set as $f=0$ but has zero gradient on it; a poor equation can hide a regular physical surface. Use a regular representation when one exists.

<a name="section-7"></a>

### The local nonlinear step and its scope

The implicit function theorem says that if $f_a$ are continuously differentiable and a $k\times k$ Jacobian submatrix for selected dependent variables is invertible at the point, those variables can locally be expressed as differentiable functions of the other $n-k$ variables and time. A nonzero determinant means invertibility; for two variables $\det\begin{pmatrix}a&b\\c&d\end{pmatrix}=ad-bc$, as derived by elimination in Math 5. “Local” and “regular” are essential. A full proof of the general nonlinear theorem is outside this finite-linear-algebra lesson; every coordinate map used in the physics examples is explicitly given and checked, so it is not concealed as a calculation.

The one-equation mechanism can be understood with AP calculus. If $f_y(x_0,y_0)>0$, continuity makes $f_y>m>0$ in a small rectangle. For each nearby $x$, $f$ increases strictly with $y$, so there is at most one root. Choose upper and lower edges giving opposite signs at $x_0$; continuity preserves these signs for nearby $x$. The intermediate value theorem gives a root between them. If $|f_x|\le M$ there, the mean value theorem gives $|\Delta y|\le(M/m)|\Delta x|$ between nearby roots. In the differentiability expansion

$$
0=f_x\Delta x+f_y\Delta y+o\!\left(\sqrt{(\Delta x)^2+(\Delta y)^2}\right),
$$

the bound makes the remainder $o(|\Delta x|)$. Dividing by $\Delta x$ yields $dy/dx=-f_x/f_y$. This proves the graph derivative locally, rather than treating $df=0$ as unexplained algebra. For a circle's upper branch it gives $dy/dx=-x/y$; at $y=0$ another chart is needed.

<a name="section-8"></a>

## 5. Actual motion and virtual variations solve different systems

Differentiating a constraint along a trajectory gives

$$
A\dot{\mathbf X}+\mathbf f_t=0.
$$

At fixed time an admissible variation instead obeys $A\delta\mathbf X=0$. Thus actual velocities of a moving constraint form an affine set, while virtual variations form the associated homogeneous null space.

For the translating line $y-a(t)=0$, $A=(0,1)$, so $\dot y=\dot a$ but $\delta y=0$. You may change the bead's horizontal position at the same instant; you may not change the prescribed height of the entire guide. This is the exact algebra behind virtual displacement (not included; [edition scope](../../SOURCES.md#pending)), not a claim that a physical movement occurs in zero time.

<a name="section-9"></a>

## 6. Normals, ideal reactions and multipliers

For Cartesian coordinates, $\mathbf R=A^T\boldsymbol\lambda$ means $R_j=\sum_a\lambda_a A_{aj}$, where transpose interchanges rows and columns. Then

$$
\mathbf R\cdot\delta\mathbf X
=\sum_a\lambda_a\sum_jA_{aj}\delta X_j
=\boldsymbol\lambda\cdot(A\delta\mathbf X)=0.
$$

Every combination of constraint normals does zero work on every tangent variation. Conversely these are all vectors with that property. To see the dimension argument, first build an orthonormal list from a basis by subtracting projections and dividing by each nonzero remaining length. Projection onto a unit vector $\mathbf e$ is $(\mathbf v\cdot\mathbf e)\mathbf e$, because the remainder has zero dot product with $\mathbf e$. Extend an orthonormal basis of $\ker A$ to one of the ambient $n$-space by adding independent coordinate directions and the same subtraction procedure. A vector perpendicular to the $n-r$ null directions has only the remaining $r$ components. The row span already supplies $r$ such independent directions, so it is the entire perpendicular space. Hence

$$
\boxed{\mathbf R\cdot\delta\mathbf X=0\text{ for all }A\delta\mathbf X=0
\quad\Longleftrightarrow\quad \mathbf R=A^T\boldsymbol\lambda.}
$$

These $\lambda_a$ are **constraint multipliers**. They need not equal the physical tension: their units and numerical values depend on the chosen $f_a$. Multiplying a constraint equation by a nonzero constant rescales its multiplier inversely, leaving $\mathbf R$ unchanged. For generalized coordinates with different units, $Q_\alpha\delta q_\alpha$ is a work pairing; do not interpret a naive Euclidean angle between coordinate tuples as a physical angle. The Cartesian derivation avoids that confusion.

**Worked force example.** A bead on $x^2+y^2=R^2$ has ideal reaction $\mathbf R=\lambda(2x,2y)$. At $(R,0)$ it is horizontal. Tangent displacement is $(0,\delta y)$, so the reaction has zero virtual work whatever $\lambda$. Determining its magnitude requires dynamics, not geometry alone.

<a name="section-10"></a>

## Checkpoints and practice

- **MC1:** Why do multiplying a row by zero and squaring a constraint risk changing the rank argument?
- **MC2:** Can $A\dot{\mathbf X}=\mathbf b\ne0$ define a vector space? What is the difference of two allowed velocities?

Feedback is separate in AM01 Physics Checkpoint Feedback (not included; [edition scope](../../SOURCES.md#pending)). Attempt **N1–N8** in [AM01 New Mathematics Practice](am01-new-mathematics-practice.md) as needed for these new techniques; the original pilot exercise set remains optional. Three hints and complete solutions are stored separately.

Independently explain: what rank counts; why a null-space basis has $n-r$ members; what is assumed in translating this into nonlinear configuration dimension; why ideal reaction forces lie in constraint-normal directions. These are the mathematical foundations for degrees of freedom and D'Alembert's principle, not a claim of a full differential-geometry course.

[Section index](README.md) · [Home](../../README.md)
