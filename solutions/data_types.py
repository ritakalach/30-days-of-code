"""
Save a line of input from stdin to a variable, print "Hello, World." on a single line, 
and finally print the value of your variable on a second line.
"""

i = 4
d = 4.0
s = 'HackerRank '

# Read and save an integer, double, and String to your variables.
i2 = int(input())
d2 = float(input())
s2 = input()

# Print the sum of both integer variables on a new line.
print(i + i2)

# Print the sum of the double variables on a new line.
print(d + d2)

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s + s2)
