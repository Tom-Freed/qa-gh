from programs.list_of_squares import list_of_squares

def test_sq():
    assert list_of_squares(10) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
    assert list_of_squares(2) == {1: 1, 2: 4}
    assert list_of_squares(3) == {1: 1, 2: 4, 3: 9}