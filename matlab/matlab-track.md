<a name="section-1"></a>

# Track B — MATLAB

> **Edition scope:** original AI-assisted supplement or study material. Some prerequisite lessons are withheld for source review; their titles are plain text, not unavailable links. [Attribution and scope](../SOURCES.md#pending).


> **Review status: framework.** Educational framework; this is not a record of learner progress. [Sources and limitations](../SOURCES.md).


| Stage | Practice | Measurable output | Verification and limitations |
| --- | --- | --- | --- |
| 1. Syntax and arrays | Variables, indexing, dimensions, elementwise versus matrix operations | A script with shape and expected-value assertions | Explain dimensions and indexing without running the code |
| 2. Scripts, functions, and plotting | Refactor a calculation into a function; plot labeled quantities | Function, calling script, and labeled figure | Test a simple known case and invalid input |
| 3. Data processing | Import a small dataset; handle units, missing values, ordering, and provenance | Reproducible processing script and data dictionary | Preserve raw data and justify every exclusion |
| 4. Numerical fitting | Fit a stated model to explicitly synthetic or available measured data | Fit report with residuals and assumptions | Check identifiability, initial conditions, sensitivity, and overfitting |
| 5. Uncertainty analysis | Propagate specified uncertainties; compare analytical and numerical approaches | Uncertainty budget and sensitivity plot | State distribution/correlation assumptions and sampling convergence |
| 6. Differential equations | Implement a sourced simple initial-value model | Solver script with initial conditions and parameter units | Compare with an analytical case where available; vary tolerances and step scales |
| 7. Physics-based simulation | Model a clearly bounded project question | Reproducible code, parameter provenance, validation report | Check units, limiting cases, convergence, and model applicability |

<a name="section-2"></a>

## Working conventions

Use a practice note to connect mathematical background, code paths/commits, tests, numerical limitations, and research applications. Record MATLAB release and toolbox requirements. Prefer base MATLAB when sufficient; do not assume optional toolboxes are installed.

Keep code and small supporting files beside the associated learning note when appropriate; store large datasets externally with stable references. Label synthetic datasets explicitly and never present them as measurements. This vault setup does not claim that MATLAB has been run in the cloud environment.


[Section index](README.md) · [Home](../README.md)
