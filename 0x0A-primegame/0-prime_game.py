#!/usr/bin/python3
"""Define isWineer function, solution to the Prime Game problem"""


def is_prime(num):
    """
    Check if a number is prime.

    Parameters:
    - num (int): The number to be checked for primality.

    Returns:
    - bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    Determine the winner of each round of the prime game.

    Parameters:
    - x (int): The number of rounds.
    - nums (list of int): An array of n for each round,
      where n is the upper limit of the consecutive integers.

    Returns:
    - str or None: The name of the player with the most wins.
      If the winner cannot be determined, returns None.
    """
    wins_maria = 0
    wins_ben = 0

    for n in nums:
        primes_count = sum(1 for i in range(1, n+1) if is_prime(i))
        if primes_count % 2 == 0:
            wins_ben += 1
        else:
            wins_maria += 1

    if wins_maria == wins_ben:
        return None
    elif wins_maria > wins_ben:
        return "Maria"
    else:
        return "Ben"
