<a name="section-1"></a>

# Review Writing Lesson 1 — From Question to Evidence

> **Edition scope:** original AI-assisted supplement or study material. Some prerequisite lessons are withheld for source review; their titles are plain text, not unavailable links. [Attribution and scope](../SOURCES.md#pending).


> **Review status: unverified.** AI-assisted educational draft; human scientific review remains pending. [Sources and limitations](../SOURCES.md).


> **Provenance and purpose**
> This is **AI instructional material**, not a literature review or a set of research findings. It develops the existing [Track A](literature-and-review-writing-track.md), rather than creating a competing track. All numerical teaching cards below are deliberately hypothetical. They are not measurements, simulations, published papers or evidence for your manuscript. Human review is pending.

[Writing dashboard](README.md) · [Independent assignment](review-writing-assignment-1.md) · [Existing argument guide](argument-and-revision-guide.md)

<a name="section-2"></a>

## 1. What a scientific review contributes

A research paper usually presents a particular investigation. A review develops an answer from a body of literature: what is supported, where studies agree or conflict, what conditions explain differences, and what remains unresolved. Its contribution is a defensible synthesis, not merely a longer list of summaries.

For example, “soft pressure sensors” is a subject area. “What evidence distinguishes mechanical relaxation from changes in conductive contacts when an electrical loading–unloading loop is observed?” is an analytical question. The second question specifies a phenomenon, competing explanatory categories and an evidential task. It can guide what you extract from each paper.

This wording proposes possibilities to investigate; it does not assert that either mechanism has been established in a particular device. A mechanism label in an abstract is not automatically evidence that competing explanations were excluded.

A **narrative review** can organize a critical, explicitly bounded argument. A **systematic review** requires a documented, reproducible search and selection process appropriate to its question; calling a review systematic does not make an informal reading list reproducible. A **scoping review** maps the range and characteristics of a literature. Select an approach because it fits the question and available work, and accurately describe what you actually did. This lesson does not claim that a formal review protocol or exhaustive search has been completed.

> **Checkpoint W1-A**
> Rewrite a broad topic you care about as a question that identifies a system, a phenomenon, and an uncertainty. Which observations could change your eventual answer?

<a name="section-3"></a>

## 2. Make the question precise enough to investigate

For a pressure-sensor project, specify at least the sensing modality, material/device class, loading conditions, output metric and intended comparison. The right scope may be much narrower than the title of your eventual review.

A useful provisional question is: “Within compressive piezoresistive sensors tested over a specified pressure range, what experimental designs separate a history-dependent electrical output from time-dependent mechanical deformation?” The words “specified pressure range” are a prompt to fill in your actual scope, not permission to invent a common range for all studies.

Ask whether a candidate paper can answer part of that question. A high sensitivity under one protocol may be relevant to device response but insufficient to distinguish causes of hysteresis. Define inclusion and exclusion reasons before results tempt you to choose only favorable examples. Preserve negative findings and papers that challenge the emerging argument.

**Poor scope:** “Find the best sensor and explain why its polymer removes hysteresis.” This presupposes a universal ranking and a mechanism.

**Better scope:** “Compare reported loading–unloading response under stated protocols, identify the evidence supporting proposed explanations, and separate comparisons that are compatible from those that remain unresolved.” This leaves room for contradictions and missing information.

<a name="section-4"></a>

## 3. Read a paper in passes, each with a different question

**Orientation pass:** identify the research question, material/device system, measurement, central claim and location of the key evidence. Read the abstract as a map of claims, not as a substitute for their support.

**Methods-and-figures pass:** locate the actual observable, axis definitions, units, normalization, loading rate, dwell time, range, conditioning, number of independent samples and analysis method. A hundred cycles on one device are not a hundred independently fabricated devices. Repeated measurements can characterize repeatability while leaving manufacturing variability unresolved.

**Inference pass:** distinguish what was observed from what the authors propose explains it. Ask what else could yield the observation and what control would discriminate. A statement that a mechanism is “consistent with” data is weaker than a uniquely identifying intervention. Record the authors' wording and your interpretation separately.

**Audit pass:** trace each intended claim to a figure, table, equation or passage. Record inaccessible supplementary material, ambiguous definitions and contradictions. Do not turn “not reported in the material inspected” into “the experiment was not performed”; those are different claims.

These passes can be spread over sessions. Their purpose is to give each reading a concrete output, not to impose another calendar.

<a name="section-5"></a>

## 4. Build an evidence record instead of a free-floating summary

An evidence record should allow another reader to reconstruct what supports a claim. Include the source identity/version, exact locator, measured quantity, relevant conditions, data processing, observation, author interpretation, uncertainty and limitation.

| Field | Why it matters |
| --- | --- |
| Exact source and locator | Makes the statement inspectable rather than merely plausible |
| Observable and definition | Prevents treating different quantities as the same measurement |
| Protocol and sample basis | Reveals rate, range, history and replication differences |
| Reported observation | Records what the paper actually shows or states |
| Authors' explanation | Preserves attribution rather than converting it to established fact |
| Your inference and alternatives | Makes the inferential step explicit and contestable |
| Missing information | Prevents silent completion of gaps by assumption |

Use an evidence record for actual accessible sources. Keep these hypothetical teaching cards out of that research ledger. The assignment has its own learning record.

<a name="section-6"></a>

## 5. Worked example — why metric definitions change a comparison

**Hypothetical teaching scenario only.** Let $r=R/R_0$ be a dimensionless electrical output. For this lesson alone, define a normalized maximum branch separation

$$h=\frac{\max_{P\in[P_{\min},P_{\max}]}|r_{\uparrow}(P)-r_{\downarrow}(P)|}{\Delta r_{\mathrm{FS}}}\times100\%,$$

where $\Delta r_{\mathrm{FS}}>0$ is a specified full-scale response span. This is a defined teaching metric, not a claim that every paper uses it. Other papers may use loop area, another denominator, different branches, or another output variable. Record the actual definition before comparing numbers.

| Hypothetical card | Maximum branch gap | Full-scale span | Pressure interval | Loading rate | Replication |
| --- | --- | --- | --- | --- | --- |
| A | 0.08 | 1.60 | 0–50 kPa | 1 kPa/s | Not specified |
| B | 0.03 | 0.30 | 0–10 kPa | 5 kPa/s | Not specified |

Applying the declared definition gives $h_A=0.08/1.60\times100\%=5\%$ and $h_B=0.03/0.30\times100\%=10\%$. Although B has a smaller absolute gap, it has a larger value of this normalized metric. Even that calculation does not establish that A is a universally better sensor: the pressure intervals and loading rates differ and the sample basis is unknown.

**Poor illustrative claim:** “B has less hysteresis because its branch gap is smaller, so its material is superior.”

**Improved illustrative reasoning:** “Under the metric defined for these hypothetical cards, B has a smaller absolute branch gap but a larger normalized gap. Different pressure intervals and loading rates prevent attributing that comparison to material choice alone.”

The improvement is not merely more cautious wording. It fixes the comparison quantity, restores the conditions and removes a causal conclusion unsupported by the example.

<a name="section-7"></a>

### An electrical loop is not automatically mechanical dissipated energy

Mechanical work has the form $\int F\,dx$; a force–displacement loop encloses energy with units of joules under the relevant quasistatic interpretation. A resistance–pressure loop has units $\Omega\cdot\mathrm{Pa}$, while an $R/R_0$–pressure loop has pressure units. Neither is automatically an energy measurement. A validated mapping between measured variables and conjugate mechanical quantities would be needed to infer mechanical dissipation.

This is an AI dimensional argument, linked to [units and scaling](../morin/morin-mathematical-prerequisites.md#section-6), not a reported result from a sensor paper. It illustrates how physics constrains scientific language.

> **Checkpoint W1-B**
> A paper calls a loop “small.” What definition, denominator, protocol and uncertainty would you need before using that statement in a cross-paper comparison?

<a name="section-8"></a>

## 6. Separate observation, proposed mechanism and inference

Suppose a hypothetical card reports different electrical outputs during loading and unloading at equal pressure. That establishes path dependence of the stated electrical measurement under that protocol. It does not alone uniquely identify its microscopic cause.

Possible explanations to investigate might include time-dependent material deformation, rearrangement of a conductive network, interfacial changes, or measurement-system response. These are hypotheses, not a claim that all occur in the sample. A useful discriminating test should predict a different outcome under competing explanations. For instance, simultaneous mechanical and electrical measurements may help separate changes in mechanical deformation from changes in electrical transduction, but only if their resolution, synchronization and controls are adequate.

“The authors attribute the response to X” reports an interpretation. “The data are compatible with X but also with Y under these conditions” is your bounded inference. “X is the unique cause” requires stronger exclusion of alternatives. Preserve these categories in separate sentences or fields rather than blending them into confident prose.

<a name="section-9"></a>

## 7. Construct an argument from claim, evidence, warrant and limitation

An argument has four connected parts:

1. **Claim:** the bounded proposition you want the reader to accept.
2. **Evidence:** a located observation or checked calculation supporting it.
3. **Warrant:** the reasoning explaining why that evidence bears on the claim.
4. **Limitation:** what the evidence does not distinguish or where the claim stops applying.

For the worked teaching cards, a defensible claim is that an absolute branch gap is insufficient for ranking the chosen normalized metric. The evidence is the two explicit calculations. The warrant is that both numerator and denominator determine a ratio. The limitation is that this calculation does not resolve cross-protocol performance or material causation.

A citation supplies traceability; it does not replace the warrant. Likewise, writing “may” before an unsupported mechanism does not turn it into an evidence-backed explanation. Identify exactly what information is missing.

<a name="section-10"></a>

## 8. Synthesize rather than concatenate summaries

A list might say “A reported X, B reported Y, C reported Z.” A synthesis groups claims by a shared question: which variables were measured comparably, which explanations are tested, and which differences survive those checks.

Build a comparison table before drafting a comparative sentence. Use explicit entries such as “definition unavailable in inspected text,” rather than a blank cell that could be read as zero. If two papers disagree, inspect whether they actually measure the same quantity over the same range and history. If they do, preserve the conflict and identify the experiment or analysis that could help resolve it. Do not choose the result that best fits an attractive narrative.

A research gap should follow from this analysis: “No inspected study independently varies X while holding Y fixed” is bounded by the inspected literature. “Nobody has studied X” makes a much broader claim that requires much broader search evidence.

<a name="section-11"></a>

## 9. Revise at the level of reasoning before polishing sentences

First repair unsupported claims, incompatible comparisons and hidden assumptions. Then revise paragraph organization, attribution and notation. Last, improve sentence rhythm and formatting. A beautifully typeset invalid inference remains invalid.

Use the existing [revision guide](argument-and-revision-guide.md). For every revision, record the original claim, evidence checked, change and remaining limitation. When feedback identifies a flaw, write the revision yourself and explain why it fixes that flaw. A generated replacement paragraph does not demonstrate your independent skill.

<a name="section-12"></a>

## 10. Independent assignment and evaluation

Proceed to [Review Writing Assignment 1](review-writing-assignment-1.md). Its new hypothetical cards deliberately differ from the worked example, and no model answer is included. Produce a short evidence table, a bounded comparative paragraph, a proposed discriminating test and a revision rationale. Optional real-paper extraction is conditional on actual source access; do not replace missing full text with invented details.

The rubric evaluates claim scope, traceability, metric/protocol comparability, separation of inference, alternatives/limitations and independent revision. Later lessons will develop verified searching, evidence extraction, multi-paper synthesis, argument structure, figures/tables, citation practice and peer-review-style revision through the existing Track A stages.

<a name="section-13"></a>

## Summary

Know how to turn a subject into a bounded question, extract a traceable observation, distinguish it from its explanation, normalize metrics correctly, test comparison conditions, and construct a claim whose scope matches its support. Reproduce the worked metric calculation and explain why it does not establish causation. Then demonstrate the skill on the independent assignment.

Human scientific review: pending.

[Section index](README.md) · [Home](../README.md)
