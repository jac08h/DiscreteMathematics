from functions import eulers_totient, prime_factors, solve_congruency_system, gcd
from primality_tests import fermat_primality_test, euler_primality_test
from rsa import RSA


def test_eulers_totient() -> None:
    # from https://oeis.org/A000010
    result_totients = [1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4, 12, 6, 8, 8, 16, 6, 18, 8, 12, 10, 22, 8, 20, 12, 18, 12,
                       28, 8, 30, 16, 20, 16, 24, 12, 36, 18, 24, 16, 40, 12, 42, 20, 24, 22, 46, 16, 42, 20, 32, 24,
                       52, 18, 40, 24, 36, 28, 58, 16, 60, 30, 36, 32, 48, 20, 66, 32, 44]
    for number, totient in enumerate(result_totients, 1):
        assert eulers_totient(number) == totient


def test_prime_factors() -> None:
    assert prime_factors(100) == [(2, 2), (5, 2)]
    assert prime_factors(60) == [(2, 2), (3, 1), (5, 1)]
    # Multiplication of factors must be equal to original number.
    for i in range(2, 1000):
        factors = prime_factors(i)
        result = 1
        for prime, power in factors:
            result *= prime ** power
        assert result == i


def test_solve_congruency_system() -> None:
    assert solve_congruency_system((13, 1, 32), (32, 0, 32)) == 5


def test_rsa():
    rsa = RSA()
    rsa.n = 51
    rsa.e = 13
    rsa.set_d()
    assert rsa.decrypt(7) == 28
    assert rsa.decrypt(48) == 12


def test_gcd():
    assert gcd(1220, 516) == 4
    assert gcd(gcd(203, 91), 77) == 7


def test_primality_tests() -> None:
    # From https://oeis.org/A000040
    primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
              61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
              131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
              193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257,
              263, 269, 271}
    for i in range(3, 272):
        if fermat_primality_test(i):
            assert i in primes
        else:
            assert i not in primes

        if euler_primality_test(i):
            assert i in primes
        else:
            assert i not in primes


if __name__ == '__main__':
    pass
