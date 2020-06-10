'''
Read a string, S, and print its integer value; if  cannot be converted to an integer, print "Bad String".
Note: You must use the String-to-Integer and exception handling constructs built into your submission language.
'''

S = input().strip()

try:
    print(int(S))
except ValueError:
    print("Bad String")
