def exgcd(a, b):
    """Uses the extended Euclidean algorithm to return
    the gcd as well as the solutions to Bézout's identity:
    coefficients x and y such that ax + by = gcd(a, b)."""
    x, y = 0, 1
    u, v = 1, 0
    while a != 0:
        quo = b // a
        rem = b % a
        m = x - (quo * u)
        n = y - (quo * v)
        b, a = a, rem
        x, y = u, v
        u, v = m, n
    gcd = b
    return gcd, x, y
