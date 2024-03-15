#!/usr/bin/python3
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def isWinner(x, nums):
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
