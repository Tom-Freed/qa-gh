from programs.vowels import vowels

def test_vow():
    assert vowels('Yo') == 1
    assert vowels('Hi hello') == 3
    assert vowels('These are some words') == 7