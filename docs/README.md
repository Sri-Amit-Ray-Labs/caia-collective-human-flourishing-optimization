# CHFOA Documentation

This folder is the documentation root for the **Collective Human Flourishing Optimized Algorithm (CHFOA)**.

- **Full manuscript:** [`../paper/CHFOA_Sri_Amit_Ray_Paper.html`](../paper/CHFOA_Sri_Amit_Ray_Paper.html) — formal problem definition, equations, the 25-algorithm conceptual mapping, datasets, evaluation metrics, transformer architecture, ethics/governance, FAQ, and references.
- **Architecture diagrams:** [`../images/`](../images/) — CHFOA decision loop, synthetic data pipeline, and an illustrative public-health policy comparison.
- **API surface:** see module docstrings under [`../chfoa/core/`](../chfoa/core/) (`fsm.py`, `cee.py`, `ecl.py`, `cdi.py`, `acll.py`, `scoring.py`, `transformer_chfoa.py`).
- **Getting started:** see the top-level [`../README.md`](../README.md) for installation, usage, and the repository map.

## Module Index

| Module | Layer | Purpose |
|---|---|---|
| `chfoa/core/fsm.py` | Flourishing State Modeling | Predicts domain-level flourishing deltas per stakeholder/action |
| `chfoa/core/cee.py` | Compassion Evaluation Engine | Scores suffering reduction and vulnerable-group uplift |
| `chfoa/core/ecl.py` | Ethical Constraint Layer | Flags Ahimsa/fairness/safety violations |
| `chfoa/core/cdi.py` | Collective Deliberation Interface | Human review and weight adjustment |
| `chfoa/core/acll.py` | Adaptive Compassion Learning Loop | Tracks prediction error from observed outcomes |
| `chfoa/core/scoring.py` | Scoring | Computes the composite objective `J(a)` |
| `chfoa/core/transformer_chfoa.py` | Transformer scaffold | Decision-Transformer-style sequence model (stub) |

This is a conceptual/technical scaffold grounded in publicly available Sri Amit Ray CAIA/HFOA materials; it does not reproduce proprietary algorithm internals.
