from fix_me import Transformer


def test_transformed_data_is_expected_value():
    t = Transformer()
    assert t.transform() == [4, 9, 11]
