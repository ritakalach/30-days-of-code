"""
A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
Given a number, n, determine and print whether it's Prime or Not prime.
"""

from math import sqrt

T = int(input())

def is_prime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

for _ in range(T):
    n = int(input())
    
    if n > 1 and is_prime(n):
        print("Prime")
    else:
        print("Not prime")
