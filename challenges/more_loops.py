"""
Given a string, S, of length N that is indexed from 1 to 0 - 1, 
print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
number_of_strings = int(input())

for i in range(0, number_of_strings):
    string = input()
    print(string[::2], string[1::2])
