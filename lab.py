"""
Shor's Algorithm - Classical Components Lab
CSC 4700/7700 - Quantum Computing

Instructions:
- Implement all methods in the QuantumLab class below
- Do NOT modify method signatures or class name
- You may add helper methods if needed
- Submit this file to Gradescope
- Total Points: 10

Required installations:
pip install numpy

Always check your Python version with:
python3 --version
"""

import numpy as np
import math


class QuantumLab:
    """
    Lab implementation for classical components of Shor's Algorithm.
    Implement all methods marked with 'pass'.
    """

    def __init__(self):
        pass

    # =========================================================================
    # Problem 1: Compute Modular Exponentiation (2 points)
    # =========================================================================

    def modular_exponentiation(self, a, x, N):
        """
        Compute a^x mod N efficiently.

        This is the function f(x) = a^x mod N used in Shor's algorithm.

        Example from lecture (slide 6):
        a=2, N=15
        x=0: 2^0 mod 15 = 1
        x=1: 2^1 mod 15 = 2
        x=2: 2^2 mod 15 = 4
        x=3: 2^3 mod 15 = 8
        x=4: 2^4 mod 15 = 1

        Args:
            a: int, base
            x: int, exponent
            N: int, modulus

        Returns:
            int: result of a^x mod N

        Hints:
            - Use Python's built-in pow(a, x, N) function
            - This computes modular exponentiation efficiently
        """
        pass

    # =========================================================================
    # Problem 2: Find Period Classically (3 points)
    # =========================================================================

    def find_period(self, a, N):
        """
        Find the period r of f(x) = a^x mod N.

        From lecture (slide 6): "The function repeats every r steps (period)"
        The period r is the smallest positive integer where a^r ≡ 1 (mod N).

        Example from lecture:
        a=2, N=15
        We compute: 2^1, 2^2, 2^3, 2^4 mod 15
        Values: 2, 4, 8, 1
        When we reach 1 at x=4, the period is r=4

        Args:
            a: int, base (1 < a < N)
            N: int, modulus

        Returns:
            int: the period r

        Hints:
            - Loop r from 1 to N
            - Use modular_exponentiation(a, r, N)
            - Return r when result equals 1
        """
        pass

    # =========================================================================
    # Problem 3: Extract Factors from Period (3 points)
    # =========================================================================

    def extract_factors(self, a, N, r):
        """
        Extract factors of N using the period r.

        From lecture (slide 7): "Why the Period Helps"
        If a^r ≡ 1 (mod N), then:
        - a^r - 1 ≡ 0 (mod N)
        - Factor as: (a^(r/2) - 1)(a^(r/2) + 1) ≡ 0 (mod N)

        We compute:
        p = gcd(a^(r/2) - 1, N)
        q = gcd(a^(r/2) + 1, N)

        Example from lecture:
        a=2, N=15, r=4
        a^(r/2) = 2^2 = 4
        p = gcd(4-1, 15) = gcd(3, 15) = 3
        q = gcd(4+1, 15) = gcd(5, 15) = 5
        Factors: 3 and 5 ✓

        Args:
            a: int, base
            N: int, number to factor
            r: int, period

        Returns:
            tuple: (p, q) where p and q are factors of N
                   Returns (None, None) if r is odd

        Hints:
            - First check if r is even: if r % 2 != 0, return (None, None)
            - Compute x = a^(r/2) mod N using modular_exponentiation
            - Compute p = gcd(x - 1, N) using math.gcd()
            - Compute q = gcd(x + 1, N)
            - Return (p, q)
        """
        pass

    # =========================================================================
    # Problem 4: Verify Factorization (2 points)
    # =========================================================================

    def verify_factorization(self, N, p, q):
        """
        Verify that p and q are valid non-trivial factors of N.

        Valid factors must satisfy:
        1. p * q = N
        2. 1 < p < N (non-trivial)
        3. 1 < q < N (non-trivial)

        Args:
            N: int, original number
            p: int, first factor
            q: int, second factor

        Returns:
            bool: True if p and q are valid factors, False otherwise

        Hints:
            - Check if p * q == N
            - Check if p > 1 and p < N
            - Check if q > 1 and q < N
            - Return True only if all conditions are met
        """
        pass


if __name__ == "__main__":
    lab = QuantumLab()
    # Test your implementations here
