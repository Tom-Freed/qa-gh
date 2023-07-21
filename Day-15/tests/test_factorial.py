from programs import factorial

def test_fact():
    assert factorial.fact(0) == 1
    assert factorial.fact(5) == 120
    assert factorial.fact(10) == 3628800