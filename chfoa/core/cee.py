"""
CEE: Compassion Evaluation Engine

Computes compassion scores using flourishing predictions, vulnerability weights,
and Sri Amit Ray-inspired indices (Empathy Quotient, Vulnerability Safeguard, etc.).
"""

from typing import List
from chfoa.core.fsm import StakeholderProfile, FlourishingVector


def estimate_compassion(pred: FlourishingVector, stakeholders: List[StakeholderProfile]) -> float:
    """
    Simple placeholder compassion score.
    Replace with a richer model combining Empathy Quotient, Vulnerability Safeguard, etc.
    """
    equity = pred.get("equity", 0.0)
    trust = pred.get("trust", 0.0)
    avg_vuln = sum(s.vulnerability_weight for s in stakeholders) / max(1, len(stakeholders))
    score = 0.5 + 0.4 * equity + 0.2 * trust + 0.1 * (avg_vuln - 1.0)
    return max(0.0, min(1.0, score))
