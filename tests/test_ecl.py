from chfoa.core.ecl import check_constraints


def test_ecl_no_violation():
    pred = {"physical_health": 0.1, "equity": 0.05}
    violations = check_constraints(pred)
    assert len(violations) == 0


def test_ecl_violation():
    pred = {"physical_health": -0.3, "equity": -0.1}
    violations = check_constraints(pred)
    assert len(violations) >= 1
