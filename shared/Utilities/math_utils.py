"""
Shared Academic Mathematics & Computation Utilities
"""

import math
from typing import List

def is_prime(n: int) -> bool:
    """Checks if an integer n is prime with O(sqrt(N)) time complexity."""
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
    """Euclidean algorithm for Greatest Common Divisor."""
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a: int, b: int) -> int:
    """Least Common Multiple using GCD."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

def luhn_checksum(card_number_str: str) -> bool:
    """Luhn Algorithm for credit card validation."""
    digits = [int(c) for c in card_number_str if c.isdigit()]
    if not digits:
        return False
    checksum = 0
    reverse_digits = digits[::-1]
    for i, d in enumerate(reverse_digits):
        if i % 2 == 1:
            doubled = d * 2
            checksum += doubled - 9 if doubled > 9 else doubled
        else:
            checksum += d
    return checksum % 10 == 0
