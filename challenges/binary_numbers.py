"""
Given a base-10 integer, n, convert it to binary (base-2). 
Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.
"""

if __name__ == '__main__':
    n = int(input())

    count = 0
    maximum = 0

    while n > 0:
        if n % 2 == 1:
            count += 1
        else:
            count = 0
        maximum = max(count, maximum)
        n //= 2

    print(maximum)
