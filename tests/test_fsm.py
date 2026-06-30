from chfoa.core.fsm import FSMModel, Context, StakeholderProfile, ActionOption


def test_fsm_predict_stub():
    fsm = FSMModel()
    ctx = Context(id="ctx_test", domain="public_health", metadata={})
    stakeholders = [StakeholderProfile(id="elderly", vulnerability_weight=2.0, preferences={})]
    action = ActionOption(id="A1", metadata={}, features={})
    pred = fsm.predict(ctx, action, stakeholders)
    assert "physical_health" in pred
    assert isinstance(pred["physical_health"], float)
