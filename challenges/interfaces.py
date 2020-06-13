"""
Complete the implementation of Calculator class, which implements the AdvancedArithmetic interface. 
The implementation for the divisorSum(n) method must return the sum of all divisors of n.
"""

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        divisors = 0
        for i in range(1, n+1):
            if n % i == 0:
                divisors += i
        return divisors

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
