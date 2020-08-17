from math_series.series import fibonacci,lucas,sum_series

def test_fibonacci():
    expected = 8
    actual = fibonacci(7)
    assert expected == actual

def test_fibonacci2():
    expected=34
    actual = fibonacci(10)
    assert expected == actual


def test_fibonacci3():
     expected = 3333333
     actual = fibonacci(1)
     assert expected != actual

def test_lucas():
    expected = 123
    actual = lucas(10)
    assert expected == actual

def test_lucas2():
    expected = 29
    actual = lucas(7)
    assert expected == actual

def test_sum():
    expected = 29
    actual = sum_series(7,2,1)
    assert expected == actual
def test_sum2():
    expected = 8
    actual = sum_series(7)
    assert expected == actual

def test_sum3():
    actual = sum_series(7,3,4)
    expected =18
    assert actual == expected

def test_sum4():
    actual = sum_series(10,3,4)
    expected = 76
    assert actual ==expected
