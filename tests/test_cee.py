from chfoa.core.fsm import StakeholderProfile
from chfoa.core.cee import estimate_compassion


def test_compassion_in_bounds():
    pred = {"equity": 0.2, "trust": 0.1}
    stakeholders = [
        StakeholderProfile(id="rural", vulnerability_weight=1.5, preferences={}),
        StakeholderProfile(id="urban", vulnerability_weight=1.0, preferences={}),
    ]
    score = estimate_compassion(pred, stakeholders)
    assert 0.0 <= score <= 1.0


def test_compassion_higher_with_more_equity_and_trust():
    stakeholders = [StakeholderProfile(id="general", vulnerability_weight=1.0, preferences={})]
    low = estimate_compassion({"equity": -0.1, "trust": -0.1}, stakeholders)
    high = estimate_compassion({"equity": 0.3, "trust": 0.3}, stakeholders)
    assert high > low
