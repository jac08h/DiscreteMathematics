from random import randint

from functions import gcd


def fermat_primality_test(p: int) -> bool:
    tried = set()
    for _ in range(3):
        a = randint(2, p - 1)
        while a in tried:
            a = randint(2, p - 1)
        # Found divisor of p.
        if gcd(a, p) != 1:
            return False
        # a ** (p-1) % p == 1
        if not a ** (p - 1) % p == 1:
            return False
    return True


def euler_primality_test(p: int) -> bool:
    # Use two bases, 2 and 3.
    # First pseudoprime for both bases: 1729
    for a in [2, 3]:
        # Found divisor of p.
        if gcd(a, p) != 1:
            return False
        # a ** ((n-1)/2 % n = +- 1
        rem = (a ** ((p - 1) // 2)) % p
        return rem == 1 or rem == p - 1


if __name__ == '__main__':
    print(euler_primality_test(1729))
