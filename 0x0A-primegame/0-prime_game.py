#!/usr/bin/python3
""" Prime game function """


def isWinner(x, nums):
    """
    Determine the winner of each round and return the overall winner.
    Maria always goes first, and both play optimally.

    :param x: Number of rounds (int)
    :param nums: List of n values for each round (list of int)
    :return: Name of the overall winner ('Maria', 'Ben') or None if tied
    """
    def sieve(n):
        """Generate prime numbers up to n using Sieve of Eratosthenes."""
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for multiple in range(i * i, n + 1, i):
                    is_prime[multiple] = False

        return is_prime

    def prime_count(is_prime, n):
        """Count the number of primes up to n."""
        return sum(is_prime[:n + 1])

    if x < 1 or not nums:
        return None

    max_n = max(nums)
    is_prime = sieve(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = prime_count(is_prime, n)

        # Maria wins if the number of primes is odd, Ben wins otherwise.
        if primes % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
