<a name="section-1"></a>

# LaTeX Starter Guide

> **Edition scope:** original AI-assisted supplement or study material. Some prerequisite lessons are withheld for source review; their titles are plain text, not unavailable links. [Attribution and scope](../SOURCES.md#pending).


> **Review status: framework.** Educational framework; this is not a record of learner progress. [Sources and limitations](../SOURCES.md).


<a name="section-2"></a>

## Start small in Overleaf

Use [Overleaf's official introduction](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes) for a targeted explanation, then reproduce the syntax without copying.

The files are learning scaffolds, not scientific prose or a finished manuscript:

- [Minimal article source](starter/main.tex) — title, sections, paragraphs, and one section cross-reference, with instructions for your own writing.
- [Bibliography starter](starter/references.bib) — a comment-only verification checklist, with **zero bibliography entries**.

Create a blank Overleaf project and manually upload/copy the starter when useful. Set `main.tex` as the main document and select pdfLaTeX. Click Recompile, replace the instructional paragraphs with your own question/scope, then change a heading independently. The source currently has no scientific equation, MATLAB figure, table, or citations; those are your later exercises. It is not the eight-week milestone.

No local TeX installation, Obsidian community plugin, or automatic Overleaf sync is required. Keep learning/reflection notes in Obsidian and edit/compile `.tex` in Overleaf; treat internal links to source files as navigation, not a promise that Obsidian renders them. Record the Overleaf project location and copy source back manually when intentionally versioning it. Do not maintain two separately edited versions of manuscript text.

<a name="section-3"></a>

## Later exercises and verification

For Weeks 3–4, use `amsmath` (already loaded) to typeset a source-checked definition. Number an equation, place a unique `\label` inside its environment, and refer to it with `\eqref`. Preserve the physical meaning, units, assumptions, pressure range, and normalization. A typesetting correction must not silently change the science.

For Weeks 5–6, export a plot from your existing MATLAB work and upload it manually. The starter loads `graphicx`. Use `\includegraphics`, `\caption`, and a unique `\label` after the caption; refer to it with `\ref`. Keep axes/units legible and record code/data provenance, conditions, processing, uncertainty, and whether data are measured, published, digitized, or synthetic. A synthetic teaching plot remains explicitly synthetic in the caption and surrounding text. No MATLAB plot is supplied or claimed as executed here.

For Week 7, build a small `tabular` inside a `table`, with a caption, label, and text reference. The starter loads `booktabs` for simple table rules. Copy only checked values/conditions; retain `not reported`, `not accessed`, negative findings, and conflicts. Empty cells do not mean zero.

<a name="section-4"></a>

## Add citations only after verification

The starter uses the standard BibTeX route when you are ready. For each **real** source, check authors, title, year, publication venue, DOI or stable identifier, version, and access limits against the source. Use a stable key and link the bibliographic record to its Obsidian paper/evidence note. Keep source locations for particular claims in the evidence chain; a bibliography entry alone does not verify a claim.

After adding real entries to `references.bib`, insert `\cite{your-actual-verified-key}` using a key you actually created. Uncomment the `\bibliographystyle{plain}` and `\bibliography{references}` lines in `main.tex`. Overleaf normally runs the required compilation sequence. If compiling in an already available local environment, the standard sequence is pdfLaTeX → BibTeX → pdfLaTeX → pdfLaTeX. Do not run BibTeX on the empty starter and treat its lack of entries as a failure of your learning.

Never insert placeholder bibliographic entries to hide unresolved citation warnings. The final exercise needs at least **three independently verified sources**; if they are unavailable, record the gap and leave the milestone incomplete. No sources were collected or fabricated for this setup.

<a name="section-5"></a>

## Completion checks

- Formatting: compilation succeeds; no unresolved labels/citations; figures, table, and equation are legible and referenced correctly.
- Science: meaning and evidence are unchanged; attribution, units, normalization, data provenance, and unresolved flags remain visible.
- Independence: after a hint, reproduce or modify the command yourself and explain why it works.

[Eight-week curriculum](latex-track.md) · internal review documentation (not included in this collection)

[Section index](README.md) · [Home](../README.md)
