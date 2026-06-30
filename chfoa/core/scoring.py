"""
CHFOA Scoring

Implements the composite CHFOA objective J(a).
"""

from typing import Dict, List, Any
from chfoa.core.fsm import StakeholderProfile, FlourishingVector
from chfoa.core.cee import estimate_compassion
from chfoa.core.ecl import check_constraints


def aggregate_flourishing(pred: FlourishingVector, stakeholders: List[StakeholderProfile]) -> float:
    """
    Aggregate flourishing vector into a scalar score.
    """
    domain_weights = {
        "physical_health": 0.3,
        "trust": 0.2,
        "equity": 0.25,
        "learning": 0.15,
        "economic_security": 0.05,
        "social_connection": 0.05,
    }
    scalar = 0.0
    for d, w in domain_weights.items():
        scalar += pred.get(d, 0.0) * w
    return scalar


def score_action(base_score: float, pred: FlourishingVector, stakeholders: List[StakeholderProfile]) -> Dict[str, Any]:
    """
    Compute CHFOA score and related metrics for a single action.
    """
    F = aggregate_flourishing(pred, stakeholders)
    C = estimate_compassion(pred, stakeholders)
    violations = check_constraints(pred)
    harm = max(0.0, -min(pred.get("physical_health", 0.0), pred.get("equity", 0.0)))
    penalty = sum(v["severity"] for v in violations)

    J = 0.2 * base_score + 0.5 * F + 0.25 * C - 0.8 * penalty - 0.5 * harm

    return {
        "score": J,
        "flourishing_scalar": F,
        "compassion": C,
        "harm": harm,
        "violations": violations,
    }
