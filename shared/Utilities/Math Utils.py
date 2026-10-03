# shared/utilities/math_utils.py
# Reusable Mathematical and Helper Functions in Python

import math

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    print("Is 29 prime?", is_prime(29))
    print("GCD of 48 and 18:", gcd(48, 18))
