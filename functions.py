from typing import Tuple, List, Optional

# Prime, power.
PrimeFactor = Tuple[int, int]

# a*X cng. b (mod m)
Congruency = Tuple[int, int, int]


def eulers_totient(n: int) -> int:
    totient = 1
    factors = prime_factors(n)
    for prime, power in factors:
        totient *= prime ** power - prime ** (power - 1)
    return totient


def prime_factors(n: int) -> List[PrimeFactor]:
    result = []
    prime = 2
    while prime <= n:
        power = 0
        while n % prime == 0:
            n //= prime
            power += 1
        if power > 0:
            result.append((prime, power))
        prime += 1 if prime == 2 else 2
    return result


def solve_congruency_system(first: Congruency, second: Congruency) -> Optional[int]:
    # first will have always greater leading quotient
    if first[0] < second[0]:
        first, second = second, first
    a1, b1, m1 = first
    a2, b2, m2 = second
    if m1 != m2:
        return False
    a = a1 % a2
    b = b1 - ((a1 // a2) * b2)
    if a == 1:
        # TODO: check if correct
        return b
    return solve_congruency_system(second, (a, b, m1))


def create_pair_congruency_to_solve(cong: Congruency) -> Congruency:
    return cong[2], 0, cong[2]


def gcd(a: int, b: int) -> int:
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    pass
