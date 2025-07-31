from prime_factors import PrimeFactor

def test_prime_factor_of_1():
    prime_factor = PrimeFactor()
    assert prime_factor.of(1) == []

def test_prime_factor_of_2():
    prime_factor = PrimeFactor()
    assert prime_factor.of(2) == [2]

def test_prime_factor_of_3():
    prime_factor = PrimeFactor()
    assert prime_factor.of(3) == [3]