from exgcd import exgcd

def modInv(a, m):
    """Returns the modular multiplicative inverse of a modulo m:
    i.e., x such that ax is congruent to 1 mod m."""
    gcd, x, y = exgcd(a, m)
    if gcd != 1:
        # a and m cannot be coprime
        print("Error: the modular inverse does not exist.")
        return None
    else:
        return x % m
