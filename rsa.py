from functions import eulers_totient, create_pair_congruency_to_solve, solve_congruency_system


class RSA:
    def __init__(self):
        self.n = self.p = self.q = None
        self.e = self.d = None
        self.decrypted = self.encrypted = None

    def set_d(self) -> bool:
        for attribute in [self.n, self.e]:
            if attribute is None:
                return False

        # e * d % phi(n) = 1
        totient = eulers_totient(self.n)
        cong = (self.e, 1, totient)
        pair_cong = create_pair_congruency_to_solve(cong)
        d = solve_congruency_system(pair_cong, cong)
        if d is not None:
            self.d = d
            return True
        return False

    def decrypt(self, msg: int) -> int:
        return msg ** self.d % self.n

    def encrypt(self, msg: int) -> int:
        return msg ** self.e % self.n


if __name__ == '__main__':
    pass
