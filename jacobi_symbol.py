from functions import is_prime, prime_factors


def jacobi_symbol(a: int, p: int):
    if not is_prime(p):
        factors = prime_factors(p)
        result = 1
        for factor, power in factors:
            # It's not necessary to calculate results of factors in even power, because
            # (+-1) ** (2x) == +1
            if power % 2 != 0:
                result *= jacobi_symbol(a, factor)
        return result

    if a == 1:
        return 1
    if a > p:
        return jacobi_symbol(a % p, p)
    if a % 2 == 0:
        if p % 8 == 1 or p % 8 == 7:
            return jacobi_symbol(a // 2, p)
        return - jacobi_symbol(a // 2, p)
    if a % 2 == 1 and p % 2 == 1:
        if a % 4 != 3 or p % 4 != 3:
            return jacobi_symbol(p, a)
        return - jacobi_symbol(p, a)


if __name__ == '__main__':
    r = jacobi_symbol(1255, 2313)
