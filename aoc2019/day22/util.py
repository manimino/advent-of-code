from functools import lru_cache

def list_eq(l1, l2):
    # used in tests
    match = (len(l1) == len(l2)) and all(l1[i] == l2[i] for i in range(len(l1)))
    if not match:
        print("Mismatch:")
        print(l1)
        print(l2)
    return match


@lru_cache()
def modInverse(a, m):
    # not mine. source: https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
    m0 = m
    y = 0
    x = 1

    if (m == 1):
        return 0

    while (a > 1):
        # q is quotient
        q = a // m

        t = m

        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y

        # Update x and y
        y = x - q * y
        x = t

    # Make x positive
    if (x < 0):
        x = x + m0
    return x