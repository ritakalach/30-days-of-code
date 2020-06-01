"""
Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. 
You will then be given an unknown number of names to query your phone book for. 
For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; 
if an entry for name is not found, print Not found instead.
"""

import sys 

n = int(input())
phone_book = {}

for _ in range(n):
    name, phone = input().split()
    phone_book[name] = phone

lines = sys.stdin.readlines()
for line in lines:
    name = line.strip()
    if name in phone_book:
        print(name + "=" + str(phone_book[name]))
    else:
        print("Not found")
