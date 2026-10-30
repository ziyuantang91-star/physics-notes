<a name="section-1"></a>

# Chapter 2 — Solutions

> **Edition scope:** original AI-assisted supplement or study material. Some prerequisite lessons are withheld for source review; their titles are plain text, not unavailable links. [Attribution and scope](../SOURCES.md#pending).


> **Review status: unverified.** AI-assisted educational draft; human scientific review remains pending. [Sources and limitations](../SOURCES.md).

> **Answer-bearing page**
> These are AI-worked solutions checked mathematically, for the original mixed questions. Human scientific approval is still pending. Do not open this page before choosing to see a solution. No content here implies the learner has solved a question.

[Return to chapter dashboard](README.md)

<a name="section-2"></a>

## C02-M01 — An upright rod with a torsional spring

Write $A=mgL/2$. Gravity gives $+A\sin\phi$, so $I\ddot\phi=A\sin\phi-\kappa\phi$. The upright equilibrium is linearly stable for $\kappa>A$, with
$$\omega^2=(\kappa-A)/I.$$
It is unstable for $\kappa<A$. Near threshold below, solve $0=(A-\kappa)\phi-A\phi^3/6+\cdots$ to obtain
$$\phi_*\approx\pm\sqrt{6(1-\kappa/A)}.$$
The small-tilt requirement is $0<1-\kappa/A\ll1$. The derivative of net torque at these roots is approximately $-2(A-\kappa)<0$, so the nearby branches are stable. The potential is $U=A\cos\phi+\kappa\phi^2/2$. At $\kappa=A$, its expansion is $U=A+A\phi^4/24+O(\phi^6)$: upright remains locally stable nonlinearly, but has no nonzero amplitude-independent harmonic frequency. A linear test alone is inconclusive there. Derivatives, expansion and small-root behavior were checked. Original AI problem; no official rating or solution exists.

**Common mistakes:** Calling every equilibrium stable; reversing the gravitational torque near upright; declaring the exact threshold unstable merely because the harmonic frequency vanishes.

**Concept notes:** Morin Section 2-2 - Balancing Torques (not included; [edition scope](../SOURCES.md#pending)) · [Morin Laws and Mathematical Techniques](morin-laws-and-mathematical-techniques.md).

**Verification status:** Independently derived and checked in the scope documented in internal review documentation (not included in this collection). Human review pending.

<a name="section-3"></a>

## C02-M02 — Resolve three-support indeterminacy with elasticity

With all contacts active, $R_-=k(z-\psi L)$, $R_0=kz$, $R_+=k(z+\psi L)$. Balance gives $3kz=P$ and $2k\psi L^2=Pa$. Thus
$$R_-=P/3-Pa/(2L),\quad R_0=P/3,\quad R_+=P/3+Pa/(2L).$$
This is admissible for $a\le2L/3$. Beyond that, set $R_-=0$. Force and moment balance give
$$R_+=Pa/L,\qquad R_0=P(1-a/L).$$
Compatibility then gives $z=R_0/k$, $\psi=(R_+-R_0)/(kL)$, so the missing contact's displacement is $\delta(-L)=P(2-3a/L)/k\le0$, confirming separation. Both branches match at $a=2L/3$. At $a=L$, the center reaction is zero and the edge configuration is marginal. Small-deflection validity requires displacements and slopes small enough for the linear geometry. Unlike C02-F07, specified spring stiffness and compatibility select a load distribution. The deliberate conceptual connection is not an accidental duplicate.

**Common mistakes:** Keeping a negative compression-only reaction; solving a rigid three-support system without the spring law; failing to test the released contact.

**Concept notes:** Morin Section 2-2 - Balancing Torques (not included; [edition scope](../SOURCES.md#pending)) · [Morin Laws and Mathematical Techniques](morin-laws-and-mathematical-techniques.md).

**Verification status:** Independently derived and checked in the scope documented in internal review documentation (not included in this collection). Human review pending.

<a name="section-4"></a>

## C02-M03 — Sliding or tipping on an accelerating platform

Platform-frame force balance yields $f=mA$ rightward and $N=mg$. Let $x_N$ be the normal resultant's horizontal position measured rightward from the base midpoint. Taking moments about the center gives $x_Nmg+h\,mA=0$, hence
$$x_N=-hA/g.$$
The rear edge is $x=-b$, so contact requires $A\le bg/h$. Friction requires $A\le\mu_sg$. Therefore
$$A_{\max}=g\min(\mu_s,b/h).$$
Sliding occurs first if $\mu_s<b/h$; tipping first if $\mu_s>b/h$; equal thresholds indicate simultaneous incipient limits in this ideal model. At a threshold the static solution is marginal; dynamics afterward is outside the question. An inertial-frame route gives the same result with net horizontal force $mA$ and zero angular acceleration. Moment and inequality checks passed.

**Common mistakes:** Using zero net real force in the accelerating frame; forcing the normal through the base midpoint; checking friction but ignoring tipping.

**Concept notes:** Morin Section 2-1 - Balancing Forces (not included; [edition scope](../SOURCES.md#pending)) · Morin Section 2-2 - Balancing Torques (not included; [edition scope](../SOURCES.md#pending)) · [Morin Laws and Mathematical Techniques](morin-laws-and-mathematical-techniques.md).

**Verification status:** Independently derived and checked in the scope documented in internal review documentation (not included in this collection). Human review pending.

<a name="section-5"></a>

## C02-M04 — A capstan holding and lowering a load

The high-side tension is $mg$. Static feasibility gives $H\ge mg e^{-\mu_s\Theta}$, so the minimum holding force is that lower bound. Strength requires $mg\le T_b$; an operator bound gives $mg\le H_{\max}e^{\mu_s\Theta}$. Thus
$$m_{\max}=\min(T_b,H_{\max}e^{\mu_s\Theta})/g.$$
For steady lowering, integration of the supplied sliding law yields $H_k=mg e^{-\mu_k\Theta}$. Gravity supplies power $mgv$; the operator absorbs $H_kv$. The pole is stationary, while the rope slides over it, so mechanical dissipation at the contact is
$$\dot Q=(mg-H_k)v=mgv(1-e^{-\mu_k\Theta}).$$
This is nonnegative and vanishes for zero kinetic friction or zero wrap. It does not imply friction heats the system in the stationary holding case, where there is no slip. Rope strength is still required during lowering. The model ignores temperature dependence, rope elasticity and structural limits of the pole.

**Common mistakes:** Using μs in a sliding law; forgetting the high-side strength limit; counting the operator as supplying rather than absorbing power during payout.

**Concept notes:** Morin Section 2-1 - Balancing Forces (not included; [edition scope](../SOURCES.md#pending)) · [Morin Laws and Mathematical Techniques](morin-laws-and-mathematical-techniques.md).

**Verification status:** Independently derived and checked in the scope documented in internal review documentation (not included in this collection). Human review pending.

<a name="section-6"></a>

## C02-M05 — Infer a distributed load from two force sensors

Integration gives $Q=q_0L(1+\beta/2)$ and moment about the left end $M_0=q_0L^2(1/2+\beta/3)$. Consequently
$$R_R=q_0L(1/2+\beta/3),\quad R_L=q_0L(1/2+\beta/6),$$
$$\bar x=L\frac{R_R}{R_L+R_R}.$$
Solving the two linear coefficient relations,
$$q_0=\frac{4R_L-2R_R}{L},\qquad
\beta=\frac{6(R_R-R_L)}{4R_L-2R_R}.$$
For positive readings, $\beta\ge-1$ and $q_0>0$ imply $1/2\le R_R/R_L<2$. The upper endpoint is only a limit of the stated positive-intercept family. Values outside this interval do not fit the model, even though other nonnegative load distributions may fit them.
With $S=R_L+R_R$,
$$\sigma_{\bar x}^2\approx\frac{L^2}{S^4}(R_R^2\sigma_L^2+R_L^2\sigma_R^2).$$
Correlated errors need a covariance term; a nearly singular inversion for $q_0,\beta$ should not be confused with validation of the assumed linear load. Integrals, inversion and derivatives were independently checked.

**Common mistakes:** Treating q as pressure rather than force per length without a width conversion; using the midpoint for a nonuniform load; ignoring correlations or the admissible reaction ratio.

**Concept notes:** Morin Section 2-2 - Balancing Torques (not included; [edition scope](../SOURCES.md#pending)) · [Morin Laws and Mathematical Techniques](morin-laws-and-mathematical-techniques.md).

**Verification status:** Independently derived and checked in the scope documented in internal review documentation (not included in this collection). Human review pending.

<a name="section-7"></a>

## C02-M06 — A radial tether in circular orbital motion

Take inward as positive separately for each body. The inner mass feels gravity inward and tension outward; the outer mass feels both inward. Thus
$$\frac{GMm}{(R-\ell)^2}-T=m\Omega^2(R-\ell),$$
$$\frac{GMm}{(R+\ell)^2}+T=m\Omega^2(R+\ell).$$
Adding gives
$$\Omega^2=\frac{GM(R^2+\ell^2)}{R(R^2-\ell^2)^2}.$$
Substitution yields the positive tension
$$T=\frac{GMm\ell(3R^2+\ell^2)}{R(R^2-\ell^2)^2}.$$
With $\epsilon=\ell/R$, the controlled expansion is $T=(GMm/R^2)[3\epsilon+7\epsilon^3+O(\epsilon^5)]$, so the leading term is $3GMm\ell/R^3$. The average of the two gravitational fields is not exactly $GM/R^2$, so imposing the point-particle rate would violate the sum of the two equations. Both equations and the dimensionless series were checked. This establishes existence of the specified rotating configuration, not its dynamical stability.

**Common mistakes:** Setting the midpoint rate to the point-particle value before balancing both masses; giving tension the same radial sign on both; calling a rotating configuration static in an inertial frame.

**Concept notes:** Morin Section 2-1 - Balancing Forces (not included; [edition scope](../SOURCES.md#pending)) · [Morin Laws and Mathematical Techniques](morin-laws-and-mathematical-techniques.md).

**Verification status:** Independently derived and checked in the scope documented in internal review documentation (not included in this collection). Human review pending.

<a name="section-8"></a>

## C02-M07 — A frictional loading path is not fixed by equilibrium alone

Write $F=\mu mg$. On loading, $x=0$ for $0\le P\le F$, then $x=(P-F)/k$ up to $x_m=(P_{\max}-F)/k$. During unloading the block first sticks at $x_m$ until $P=P_{\max}-2F$, since the friction must change from $-F$ to $+F$. It then slides left with
$$x=(P+F)/k.$$
At $P=0$, $x_r=F/k$. Total sliding distance is $x_m+(x_m-x_r)$, giving
$$Q_f=\frac{F(2P_{\max}-3F)}{k}.$$
The final stored spring energy is $F^2/(2k)$, so this is not a closed configuration-space cycle. As an independent check, $\int P\,dx$ over both moving branches equals $Q_f+F^2/(2k)$. The condition $P_{\max}>2F$ ensures reverse sliding occurs before force reaches zero; other ranges require different branches. A quasistatic process can dissipate energy even with negligible inertia.

**Common mistakes:** Using the friction equality during a sticking interval; assuming force return implies zero displacement; equating net input work with heat while ignoring stored spring energy.

**Concept notes:** Morin Section 2-1 - Balancing Forces (not included; [edition scope](../SOURCES.md#pending)) · [Morin Laws and Mathematical Techniques](morin-laws-and-mathematical-techniques.md).

**Verification status:** Independently derived and checked in the scope documented in internal review documentation (not included in this collection). Human review pending.

<a name="section-9"></a>

## C02-M08 — Infer a nonuniform hanging rope from tension data

The lower payload has $m_0=T_0/g$. Local balance gives $\rho(y)=T'(y)/g=(A+2By)/g$. Nonnegativity on the interval requires $A\ge0$ and $A+2BL\ge0$, since the density is linear. Rope mass is $(AL+BL^2)/g$. For nonzero total mass, the combined center is
$$y_{\mathrm{CM}}=\frac{AL^2/2+2BL^3/3}{T_0+AL+BL^2}.$$
The payload contributes mass to the denominator but zero first moment at $y=0$. A single top tension fixes only the combined weight. Even with known payload, profiles $\rho_1=m_r/L$ and $\rho_2=2m_ry/L^2$ both have rope mass $m_r$ but different distributions and centers. The measured full quadratic profile contains more information than its top value; exact differentiation can be sensitive to noise for real data. Derivatives, masses and moments were checked.

**Common mistakes:** Ignoring the lower payload; confusing A and B units; assuming a single integrated measurement determines a spatial profile.

**Concept notes:** Morin Section 2-1 - Balancing Forces (not included; [edition scope](../SOURCES.md#pending)) · Morin Section 2-2 - Balancing Torques (not included; [edition scope](../SOURCES.md#pending)) · [Morin Laws and Mathematical Techniques](morin-laws-and-mathematical-techniques.md).

**Verification status:** Independently derived and checked in the scope documented in internal review documentation (not included in this collection). Human review pending.

<a name="section-10"></a>

## C02-M09 — A ladder with uncertain position, angle and horizontal loading

Define $A(a)=W/2+Pa/L$ and $c=1-s/L\ge0$. Torque about the foot gives
$$N_w=A(a)\cot\theta+Hs/L.$$
Vertical balance gives $N_f=W+P$, and horizontal balance gives signed rightward friction
$$f=N_w-H=A(a)\cot\theta-cH.$$
The wall normal is positive for positive $W$ and the stated angle range, so wall contact is admissible. Since cotangent decreases on this interval and all inputs are independent,
$$f_{\max}=A(a_+)\cot\theta_-,\qquad
f_{\min}=A(a_-)\cot\theta_+-cH_+.$$
Every combination is feasible exactly when
$$\boxed{\max\{A(a_+)\cot\theta_-,\ cH_+-A(a_-)\cot\theta_+\}\le\mu_0(W+P).}$$
The first entry is positive, so it already dominates any nonpositive second entry. This checks both friction directions. Restricting uncertainty correlations could change the extremal combinations; those were explicitly assumed independent. Beam buckling, dynamics and finite contact details remain outside the model. Endpoint enumeration was checked numerically against interior samples.

**Common mistakes:** Testing only the largest H; assuming floor friction always points toward the wall; confusing s/L with vertical height fraction without accounting for sinθ.

**Concept notes:** Morin Section 2-1 - Balancing Forces (not included; [edition scope](../SOURCES.md#pending)) · Morin Section 2-2 - Balancing Torques (not included; [edition scope](../SOURCES.md#pending)) · [Morin Laws and Mathematical Techniques](morin-laws-and-mathematical-techniques.md).

**Verification status:** Independently derived and checked in the scope documented in internal review documentation (not included in this collection). Human review pending.

<a name="section-11"></a>

## C02-M10 — Stress in a uniformly rotating rod

For the outer segment, radial force balance at an instant gives
$$T(r)=\int_r^L\rho S\Omega^2x\,dx=\frac{\rho S\Omega^2}{2}(L^2-r^2).$$
Its free-end boundary value is zero, and the largest tension is at the pin. The pin force magnitude is $T(0)=\rho S\Omega^2L^2/2=M\Omega^2L/2$, equal to the whole rod's mass times its center-of-mass acceleration. The stress constraint gives
$$\Omega\le\sqrt{\frac{2\sigma_a}{\rho L^2}}.$$
Cross-sectional area cancels only under the homogeneous, axial-stress model. Kinetic energy is
$$K=\frac12\int_0^L\Omega^2x^2\rho S\,dx=\frac{\rho S\Omega^2L^3}{6}=\frac{M\Omega^2L^2}{6}.$$
This agrees with $I=ML^2/3$ and $K=I\Omega^2/2$. A free-body balance with zero real net force would be wrong in the inertial frame; a rotating-frame derivation must include its corresponding inertial force. Integrals, boundary conditions and dimensional limits were checked.

**Common mistakes:** Applying zero real net force to a rotating segment; treating every element as having the same centripetal acceleration; confusing volume density ρ with linear density ρS.

**Concept notes:** Morin Section 2-1 - Balancing Forces (not included; [edition scope](../SOURCES.md#pending)) · [Morin Laws and Mathematical Techniques](morin-laws-and-mathematical-techniques.md).

**Verification status:** Independently derived and checked in the scope documented in internal review documentation (not included in this collection). Human review pending.

[Section index](README.md) · [Home](../README.md)
