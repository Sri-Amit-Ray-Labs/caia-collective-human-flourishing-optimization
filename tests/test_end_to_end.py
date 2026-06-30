"""
Minimal end-to-end scaffold test.

This is only a structural test; replace with real flows.
"""

from chfoa.core.fsm import FSMModel, Context, StakeholderProfile, ActionOption
from chfoa.core.scoring import score_action


def test_end_to_end_stub():
    fsm = FSMModel()
    ctx = Context(id="ctx_e2e", domain="public_health", metadata={})
    stakeholders = [StakeholderProfile(id="rural", vulnerability_weight=1.5, preferences={})]
    action = ActionOption(id="A1", metadata={}, features={})
    pred = fsm.predict(ctx, action, stakeholders)
    metrics = score_action(base_score=0.7, pred=pred, stakeholders=stakeholders)
    assert "score" in metrics
