"""
Determine if a given string, s, is a palindrome.

Write the following declarations and implementations:
  1. Two instance variables: one for your stack, and one for your queue.
  2. A void pushCharacter(char ch) method that pushes a character onto a stack.
  3. A void enqueueCharacter(char ch) method that enqueues a character in the queue instance variable.
  4. A char popCharacter() method that pops and returns the character at the top of the stack instance variable.
  5. A char dequeueCharacter() method that dequeues and returns the first character in the queue instance variable.
"""

import sys

class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []

    def popCharacter(self):
        return self.stack.pop()

    def pushCharacter(self, char):
        self.stack.append(char)

    def dequeueCharacter(self):
        char = self.queue[0]
        self.queue = self.queue[1:]
        return char

    def enqueueCharacter(self, char):
        self.queue.append(char)

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    
