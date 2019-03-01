#! python3
# This is the unit test for polynomials.py

from polynomials import polynomial

poly1 = polynomial([1, 2, 3])

poly2 = polynomial([2, 1, 1, 1])

poly3 = polynomial([0])

poly4 = polynomial([3, 1, 0])

def test_add():
    assert poly1.add(poly2) == [3, 3, 4, 1], 'poly1 and poly2 did not sum correctly'
    assert poly1.add(poly3) == [1, 2, 3], 'poly1 and poly3 did not sum correctly'
    assert poly1.add(poly4) == [4, 3, 3], 'poly1 and poly4 did not sum correctly'

def test_degree():
    assert poly1.degree() == 2, 'poly1 degree was not determined correctly'
    assert poly2.degree() == 3, 'poly2 degree was not determined correctly'
    assert poly3.degree() == 0, 'poly3 degree was not determined correctly'
    assert poly4.degree() == 1, 'poly4 degree was not determined correctly'

def test_derivative():
    assert poly1.derivative() == [2, 6], 'poly1 derivative was not determined correctly'
    assert poly2.derivative() == [1, 2, 3], 'poly2 derivative was not determined correctly'
    assert poly3.derivative() == [0], 'poly3 derivative was not determined correctly'
    assert poly4.derivative() == [1], 'poly4 derivative was not determined correctly'

def test_evaluate():
    assert poly1.evaluate(0) == 1, 'poly1 did not evaluate correctly at 0'
    assert poly1.evaluate(2) == 17, 'poly1 did not evaluate correctly at 2'
    assert poly2.evaluate(0) == 2, 'poly2 did not evaluate correctly at 0'
    assert poly2.evaluate(2) == 16, 'poly2 did not evaluate correctly at 2'
    assert poly3.evaluate(0) == 0, 'poly3 did not evaluate correctly at 0'
    assert poly3.evaluate(2) == 0, 'poly3 did not evaluate correctly at 2'
    assert poly4.evaluate(0) == 3, 'poly4 did not evaluate correctly at 0'
    assert poly4.evaluate(2) == 5, 'poly4 did not evaluate correctly at 2'