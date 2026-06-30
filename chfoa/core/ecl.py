"""
ECL: Ethical Constraint Layer

Enforces Ahimsa in code, fairness thresholds, safety gates, and rights-based constraints
inspired by Sri Amit Ray CAIA.
"""

from typing import Dict, List, Any


def check_constraints(pred: Dict[str, float]) -> List[Dict[str, Any]]:
    """
    Return a list of constraint violations.

    Each violation: {
        "constraint_id": str,
        "severity": float,
        "description": str
    }
    """
    violations = []

    # Example Ahimsa: physical health should not decrease severely
    if pred.get("physical_health", 0.0) < -0.2:
        violations.append({
            "constraint_id": "no_mass_harm",
            "severity": 1.0,
            "description": "Severe physical health decline (Ahimsa violation)."
        })

    # Example fairness: equity should not decrease beyond threshold
    if pred.get("equity", 0.0) < -0.05:
        violations.append({
            "constraint_id": "fairness_threshold",
            "severity": 0.6,
            "description": "Equity decreases for vulnerable groups."
        })

    return violations
