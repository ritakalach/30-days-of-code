'''
Given an array, a, of size n distinct elements, sort the array in ascending order using the Bubble Sort algorithm. 
Once sorted, print the following 3 lines:
  1. "Array is sorted in numSwaps swaps." where numSwaps is the number of swaps that took place.
  2. "First Element: firstElement" where firstElement is the first element in the sorted array.
  3. "Last Element: lastElement" where lastElement is the last element in the sorted array.
'''

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

num_swaps = 0

for i in range(n):
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            tmp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = tmp
            num_swaps += 1

    if num_swaps == 0:
        break

print("Array is sorted in {} swaps.".format(num_swaps))
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[len(a) - 1]))
