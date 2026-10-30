<a name="section-1"></a>

# Statics — LaTeX and MATLAB Bridge

> **Edition scope:** original AI-assisted supplement or study material. Some prerequisite lessons are withheld for source review; their titles are plain text, not unavailable links. [Attribution and scope](../SOURCES.md#pending).


> **Review status: unverified.** AI-assisted educational draft; human scientific review remains pending. [Sources and limitations](../SOURCES.md).


**AI instructional draft.** Attempt the task yourself before opening the reference implementation.

<a name="section-2"></a>

## Typesetting task

During the appropriate existing LaTeX lesson, typeset and explain one checked equilibrium calculation from §2.1 (not included; [edition scope](../SOURCES.md#pending)) or §2.2 (not included; [edition scope](../SOURCES.md#pending)). For example, preserve the distinction between a signed friction force and its inequality:

```latex
\begin{align}
f &= Mg\sin\theta-P\cos\theta,\\
N &= Mg\cos\theta+P\sin\theta,\\
|f| &\le \mu_s N,\qquad N\ge 0.
\end{align}
```

For a standalone LaTeX document, `align` requires `amsmath`. In Obsidian use the note's `$...$` and `$$...$$` mathematics; a full document preamble does not belong inside a display. Define every symbol, state contact assumptions and write a sentence interpreting a sign change. Independently change the axis convention and explain which signs change. Formatting success alone does not establish physics understanding.

For review-writing practice, typeset your own paragraph or a clearly labeled hypothetical comparison table from [Review Writing Assignment 1](../scientific-writing/review-writing-assignment-1.md). Do not create fake bibliography entries to fill the real-reference milestone.



<a name="section-3"></a>

## MATLAB task and reference

Before reading the code, plan a grid of angles and dimensionless pushes, calculate the required normal and friction forces, and plot the region satisfying both contact and static-friction conditions. Mark the friction sign-change curve. This is a calculated model visualization, not measured data.

Reference: [statics_feasibility.m](statics_feasibility.m). It uses base MATLAB arrays, elementwise operations and plotting. Call the function with an explicit output directory and coefficient, for example `statics_feasibility('chosen-output-folder',0.4)` after adding its directory to your MATLAB path. MATLAB is not installed/available in the inspected shell, so syntax/runtime and exported output have **not** been verified in MATLAB.

After targeted feedback, independently change the coefficient and predict what happens before rerunning. Record MATLAB release, actual output and any errors in the existing learning template. Do not claim a pass from the Python counterpart.

<a name="section-4"></a>

## Executed Python alternative

[plot_models.py](plot_models.py) recreates the five original instructional figures using NumPy/Matplotlib. Run it with `--output-dir` pointing to a chosen writable folder. This Python implementation was executed and the resulting figures visually inspected. Its computations and labels were checked; it is explicitly a Python alternative.

The figures embedded in the lessons are original instructional diagrams or model plots. They are not copied textbook figures and are not measurements. The source page references identify the physical teaching context, not ownership of the new drawings.

Human scientific review and independent student reproduction remain pending.

[Section index](README.md) · [Home](../README.md)
