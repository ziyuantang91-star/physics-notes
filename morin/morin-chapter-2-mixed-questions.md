<a name="section-1"></a>

# Chapter 2 — Ten Mixed Questions

> **Edition scope:** original AI-assisted supplement or study material. Some prerequisite lessons are withheld for source review; their titles are plain text, not unavailable links. [Attribution and scope](../SOURCES.md#pending).


> **Review status: unverified.** AI-assisted educational draft; human scientific review remains pending. [Sources and limitations](../SOURCES.md).

**Prepared for study; not evidence of completion.** Exactly ten questions appear in this set. Multipart tasks count as one coherent question each. Difficulty and time estimates below are AI educational judgments, not official ratings or imposed quotas. Formative checkpoints in lessons and the review-writing exercise are separate.

The question view contains no embedded hints or solutions. Ask in chat for `C02-… Hint 1`, a solution assessment, or a complete solution. The chapter dashboard has a separately labeled assistance area if you deliberately choose to open it in Obsidian. Existing Obsidian files are not a secure spoiler barrier: search and link previews can reveal their contents.

[Chapter dashboard](README.md)

These ten are **original AI-created questions**, not BPhO/F=ma/USAPhO questions. They were chosen to make the additional physical inputs explicit while integrating statics with later concepts. Optional tutoring can unpack any supplied prerequisite. No source quota or difficulty cap was applied.

<a name="section-2"></a>

## C02-M01 — An upright rod with a torsional spring

A uniform rod of mass $m$ and length $L$ is hinged at its lower end. Its tilt $\phi$ is measured from the upward vertical. A torsional spring applies torque $-\kappa\phi$ with $\kappa>0$. The hinge is frictionless. Work near $\phi=0$ with no stops. Determine the stability of the upright equilibrium, the small-oscillation frequency when it is linearly stable, and the leading nonzero equilibrium tilts when $\kappa$ is just below the stability threshold. Classify those nearby equilibria.

**Supplied future input:** $I=mL^2/3$ about the hinge, $I\ddot\phi=\tau$, $\tau=-dU/d\phi$, and $\sin\phi=\phi-\phi^3/6+\cdots$. Include the threshold case explicitly.

**Source:** Original AI question, 2026-10-19; all additional model laws are stated above.

**Prerequisites:** Current torque; future Chapters 4–6 and 8: small oscillations, energy curvature, inertia. All dynamical inputs needed are supplied; no prior completion assumed.

**Assessment:** Modeling: conservative rotational system; reasoning: stability versus equilibrium; mathematics: Taylor expansion + linear ODE; principles: torque, elasticity, energy and inertia; insight: a zero linear coefficient needs a higher-order test; estimated 45–75 min.

**Concept notes:** Morin Section 2-2 - Balancing Torques (not included; [edition scope](../SOURCES.md#pending)) · [Morin Laws and Mathematical Techniques](morin-laws-and-mathematical-techniques.md).

**Attempt status:** Unattempted in this record.

<a name="section-3"></a>

## C02-M02 — Resolve three-support indeterminacy with elasticity

A weightless rigid beam lies above three identical vertical compression-only springs of stiffness $k$ at $x=-L,0,L$. Their unloaded tops are level. A downward point load $P>0$ acts at $x=a$, where $0\le a\le L$. Assume small deflections: the beam's downward displacement is $\delta(x)=z+\psi x$. An active spring supplies $R=k\delta$ if $\delta\ge0$ and no force if the beam lifts away. Determine the reactions throughout the full range of $a$, including any contact-state transition. Explain how compatibility supplies the information missing in C02-F07.

**Source:** Original AI question, 2026-10-19; all additional model laws are stated above.

**Prerequisites:** Current torque/force; supplied Hooke law and rigid-beam displacement compatibility, a future Chapter 4 connection.

**Assessment:** Modeling: unilateral elastic contacts; reasoning: piecewise active sets; mathematics: linear system + inequalities; principles: statics, elasticity and geometry; insight: solve then test every assumed contact; estimated 45–75 min.

**Concept notes:** Morin Section 2-2 - Balancing Torques (not included; [edition scope](../SOURCES.md#pending)) · [Morin Laws and Mathematical Techniques](morin-laws-and-mathematical-techniques.md).

**Attempt status:** Unattempted in this record.

<a name="section-4"></a>

## C02-M03 — Sliding or tipping on an accelerating platform

A uniform rectangular block of mass $m$ has base width $2b$ and height $2h$. It remains at rest relative to a platform accelerating horizontally rightward with constant acceleration $A\ge0$. The base has coefficient $\mu_s$. Determine the required friction, normal reaction and position of the resultant normal force relative to the base midpoint. Find the greatest acceleration compatible with no sliding or tipping, and distinguish which failure occurs first.

**Supplied future input:** in the translating platform frame, include a fictitious force $-mA\hat x$ at the center of mass. The frame does not rotate. Contact pressure must be nonnegative and its resultant must lie within the base.

**Source:** Original AI question, 2026-10-19; all additional model laws are stated above.

**Prerequisites:** Current statics/contact; future Chapter 10 translating-frame force (supplied). The block is not static in the inertial ground frame.

**Assessment:** Modeling: frame choice and distributed contact; reasoning: competing failure criteria; mathematics: moments + inequalities; principles: acceleration, friction and tipping; insight: the normal resultant can move within the footprint; estimated 30–55 min.

**Concept notes:** Morin Section 2-1 - Balancing Forces (not included; [edition scope](../SOURCES.md#pending)) · Morin Section 2-2 - Balancing Torques (not included; [edition scope](../SOURCES.md#pending)) · [Morin Laws and Mathematical Techniques](morin-laws-and-mathematical-techniques.md).

**Attempt status:** Unattempted in this record.

<a name="section-5"></a>

## C02-M04 — A capstan holding and lowering a load

A massless flexible rope wraps a fixed pole through angle $\Theta>0$. One end supports a hanging mass $m$; an operator controls the other end. Ignore rope weight and any other friction. The rope's allowable tension is $T_b$. Find the minimum holding force for a stationary load with coefficient $\mu_s$, and the largest load mass compatible with a maximum operator force $H_{\max}$ and the rope strength. Then suppose the mass is lowered at constant speed $v>0$, with kinetic coefficient $\mu_k$. Determine the operator tension and the rate of energy dissipated at the pole.

**Supplied future input:** during steady sliding toward the load, the tension along the wrap satisfies $dT=\mu_kT\,d\phi$ when integrated toward the high-tension side. Mechanical power of a collinear force is $Fv$.

**Source:** Original AI question, 2026-10-19; all additional model laws are stated above.

**Prerequisites:** Current rope friction; future Chapters 3 and 5: kinetic friction and power, supplied. Operator absorbs mechanical energy during controlled payout.

**Assessment:** Modeling: static versus sliding contact; reasoning: strength plus friction and energy; mathematics: exponential bound; principles: force, friction, work rate; insight: do not use the static coefficient for dissipation; estimated 35–60 min.

**Concept notes:** Morin Section 2-1 - Balancing Forces (not included; [edition scope](../SOURCES.md#pending)) · [Morin Laws and Mathematical Techniques](morin-laws-and-mathematical-techniques.md).

**Attempt status:** Unattempted in this record.

<a name="section-6"></a>

## C02-M05 — Infer a distributed load from two force sensors

A weightless beam spans $0\le x\le L$ and rests on two vertical force sensors at its ends. It carries downward line load $q(x)=q_0(1+\beta x/L)$, with $q_0>0$ in N/m and $\beta\ge-1$. Find both sensor reactions and the resultant load location. Invert the measurements $(R_L,R_R)$ to obtain $q_0,\beta$ and determine which reaction ratios can arise in this model. Finally, for independent small reaction uncertainties $\sigma_L,\sigma_R$, derive the first-order uncertainty of the inferred resultant location. Treat $L$ as exact.

**Supplied mathematics:** for independent small uncertainties, $\sigma_f^2\approx(\partial f/\partial R_L)^2\sigma_L^2+(\partial f/\partial R_R)^2\sigma_R^2$.

**Source:** Original AI question, 2026-10-19; all additional model laws are stated above.

**Prerequisites:** Current torque/center of load; calculus and inverse modeling; supplied uncertainty propagation. Not an experiment or a claim about actual sensors.

**Assessment:** Modeling: distributed load and measurement model; reasoning: identifiability and admissible inputs; mathematics: integration, inversion, partial derivatives; principles: force, torque and uncertainty; insight: not every pair of readings fits the assumed load family; estimated 45–75 min.

**Concept notes:** Morin Section 2-2 - Balancing Torques (not included; [edition scope](../SOURCES.md#pending)) · [Morin Laws and Mathematical Techniques](morin-laws-and-mathematical-techniques.md).

**Attempt status:** Unattempted in this record.

<a name="section-7"></a>

## C02-M06 — A radial tether in circular orbital motion

Two equal point masses $m$ are joined by a massless rigid tensile member of length $2\ell$, oriented radially around a much larger central mass $M$. Their radii are $R-\ell$ and $R+\ell$, with $0<\ell<R$. The assembly rotates uniformly at angular rate $\Omega$, with its midpoint at fixed radius $R$. Ignore other forces and the pair's mutual gravity. Determine $\Omega$ required for this configuration and the internal tension. Obtain the leading tension for $\ell/R\ll1$ and explain why the point-particle value $\Omega^2=GM/R^3$ cannot be imposed exactly for finite separation.

**Supplied future input:** each mass needs inward acceleration $\Omega^2r$; central gravity has magnitude $GMm/r^2$.

**Source:** Original AI question, 2026-10-19; all additional model laws are stated above.

**Prerequisites:** Current subsystem forces; future Chapters 3, 7 and 10: circular motion and gravity (supplied); optional small-parameter expansion.

**Assessment:** Modeling: two bodies in a nonuniform field; reasoning: shared angular rate and internal forces; mathematics: rational equations + asymptotic expansion; principles: gravity, circular acceleration and tension; insight: the assembly midpoint is not exactly a test particle; estimated 50–85 min.

**Concept notes:** Morin Section 2-1 - Balancing Forces (not included; [edition scope](../SOURCES.md#pending)) · [Morin Laws and Mathematical Techniques](morin-laws-and-mathematical-techniques.md).

**Attempt status:** Unattempted in this record.

<a name="section-8"></a>

## C02-M07 — A frictional loading path is not fixed by equilibrium alone

A block of mass $m$ on a horizontal rough surface is attached to a horizontal spring of stiffness $k$, whose force is $-kx$ when the block has rightward displacement $x$ from its unstretched position. Take both static and kinetic friction coefficients to be the same $\mu>0$. Starting from $x=0,P=0$, increase a rightward applied force $P$ quasistatically to $P_{\max}>2\mu mg$, then decrease it quasistatically back to zero. Find the loading/unloading displacement branches, the residual displacement and total frictional energy dissipated. Explain whether returning P to zero closes a cycle in configuration space.

**Supplied future input:** spring energy is $kx^2/2$; sliding dissipation is friction magnitude times total sliding distance. Neglect inertia except during vanishingly small transitions.

**Source:** Original AI question, 2026-10-19; all additional model laws are stated above.

**Prerequisites:** Current friction inequalities; supplied spring law and energy; future Chapters 4–5. Loading history is prescribed to remove static ambiguity.

**Assessment:** Modeling: stick–slip path; reasoning: history dependence and energy accounting; mathematics: piecewise linear relations; principles: elasticity, friction and work; insight: a closed force history need not be a closed displacement cycle; estimated 45–80 min.

**Concept notes:** Morin Section 2-1 - Balancing Forces (not included; [edition scope](../SOURCES.md#pending)) · [Morin Laws and Mathematical Techniques](morin-laws-and-mathematical-techniques.md).

**Attempt status:** Unattempted in this record.

<a name="section-9"></a>

## C02-M08 — Infer a nonuniform hanging rope from tension data

A static vertical rope extends from $y=0$ to $y=L$, where y is height above its lower end. A point payload may hang from that lower end. In uniform gravity the measured tension model is $T(y)=T_0+Ay+By^2$, with $T_0\ge0$. Determine the payload mass, linear density, total rope mass, and center of mass of rope plus payload. State the conditions on A and B for nonnegative density. Would a single top-tension measurement uniquely determine the density profile? Demonstrate your answer with two different nonnegative profiles having the same rope mass.

The expression is a hypothetical exact teaching model, not experimental data.

**Source:** Original AI question, 2026-10-19; all additional model laws are stated above.

**Prerequisites:** Current distributed balance; derivatives/integrals and center of mass. Intentional extension of C02-F01 to inverse inference and variable density.

**Assessment:** Modeling: distributed mass plus boundary payload; reasoning: local versus global information; mathematics: differentiation + moments; principles: force balance and center of mass; insight: one integral measurement cannot fix a function; estimated 40–65 min.

**Concept notes:** Morin Section 2-1 - Balancing Forces (not included; [edition scope](../SOURCES.md#pending)) · Morin Section 2-2 - Balancing Torques (not included; [edition scope](../SOURCES.md#pending)) · [Morin Laws and Mathematical Techniques](morin-laws-and-mathematical-techniques.md).

**Attempt status:** Unattempted in this record.

<a name="section-10"></a>

## C02-M09 — A ladder with uncertain position, angle and horizontal loading

A uniform ladder of length L and weight W leans against a frictionless wall. A point load of fixed weight P sits a distance a along the ladder from its foot. A horizontal rightward force H, directed toward the wall, acts at distance s along the ladder, where 0≤s≤L. The floor friction coefficient is uncertain but at least μ₀>0. Independent uncertainties are a∈[a₋,a₊]⊂[0,L], θ∈[θ₋,θ₊]⊂(0,π/2), and H∈[0,H₊]. Derive a necessary and sufficient inequality within this ideal model that guarantees equilibrium for every combination in these ranges. Include both possible directions of floor friction and the wall-contact test.

**Source:** Original AI question, 2026-10-19; all additional model laws are stated above.

**Prerequisites:** Current ladder force/torque; interval reasoning and monotonicity. This is a model robustness exercise, not real ladder safety certification.

**Assessment:** Modeling: multiple loads and uncertain inputs; reasoning: worst-case combinations; mathematics: affine bounds + monotonic cotangent; principles: torque, friction and uncertainty; insight: strongest loading need not maximize friction in the same direction; estimated 45–75 min.

**Concept notes:** Morin Section 2-1 - Balancing Forces (not included; [edition scope](../SOURCES.md#pending)) · Morin Section 2-2 - Balancing Torques (not included; [edition scope](../SOURCES.md#pending)) · [Morin Laws and Mathematical Techniques](morin-laws-and-mathematical-techniques.md).

**Attempt status:** Unattempted in this record.

<a name="section-11"></a>

## C02-M10 — Stress in a uniformly rotating rod

A straight homogeneous slender rod of length L, cross-sectional area S and volume mass density ρ rotates at constant angular speed Ω in a horizontal plane about a frictionless pin at one end. Ignore gravity in the in-plane balance and neglect elastic elongation. Determine the axial tension T(r) at distance r from the pin, the pin's in-plane force magnitude, the maximum allowable Ω if tensile stress cannot exceed σₐ, and the total rotational kinetic energy.

**Supplied future input:** a point at radius x requires inward acceleration Ω²x; a rod element has mass ρS dx; tensile stress is T/S and kinetic energy is (1/2)∫v²dm. Assume strength failure is controlled only by axial tension.

**Source:** Original AI question, 2026-10-19; all additional model laws are stated above.

**Prerequisites:** Current cut-subsystem reasoning; supplied future Chapters 3 and 8 inputs: centripetal acceleration and kinetic energy. This is steady rotation, not inertial-frame statics.

**Assessment:** Modeling: distributed acceleration and stress; reasoning: choose the outer segment; mathematics: two integrals; principles: Newtonian force, strength and energy; insight: local tension supports the required acceleration of the entire outer segment; estimated 35–60 min.

**Concept notes:** Morin Section 2-1 - Balancing Forces (not included; [edition scope](../SOURCES.md#pending)) · [Morin Laws and Mathematical Techniques](morin-laws-and-mathematical-techniques.md).

**Attempt status:** Unattempted in this record.

[Section index](README.md) · [Home](../README.md)
