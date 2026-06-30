from chfoa.core.transformer_chfoa import CHFOATransformer


def test_transformer_init():
    model = CHFOATransformer(config={"d_model": 128})
    assert model.config["d_model"] == 128
