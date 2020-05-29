"""
Given an integer, n, print its first 10 multiples.
"""

if __name__ == '__main__':
    n = int(input())

    for i in range(1,11):
        result = n * i
        print("{} x {} = {}".format(n, i, result))
