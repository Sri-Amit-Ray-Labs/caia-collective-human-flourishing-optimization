"""
Synthetic data generator for CHFOA benchmarks.

Generates synthetic trajectories and labels for testing flourishing-based decision-making.
"""

import random
from typing import Dict, List, Any


def generate_sample(n: int = 100) -> List[Dict[str, Any]]:
    rows = []
    for i in range(n):
        row = {
            "context_id": f"ctx_{i}",
            "domain": "public_health",
            "stakeholder_group": random.choice(["elderly", "rural", "urban", "general"]),
            "action_type": random.choice(["urban_focus", "rural_focus", "mixed_outreach"]),
            "vulnerability_weight": random.uniform(1.0, 2.0),
            "task_utility": random.uniform(0.0, 1.0),
            "physical_health_delta": random.uniform(-0.2, 0.4),
            "trust_delta": random.uniform(-0.1, 0.3),
            "equity_delta": random.uniform(-0.15, 0.35),
            "learning_delta": random.uniform(-0.05, 0.25),
            "social_connection_delta": random.uniform(-0.05, 0.25),
            "observed_flourishing_score": random.uniform(0.0, 1.0),
            "observed_harm_indicator": random.choice([0, 1]),
            "reviewer_feedback": random.uniform(0.0, 1.0),
            "delayed_outcome_score": random.uniform(0.0, 1.0)
        }
        rows.append(row)
    return rows
