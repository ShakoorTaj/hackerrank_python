#!/bin/python3

import sys

n = 3 # int(input().strip())
a = [3,1,2]#list(map(int, input().strip().split(' ')))
# Write Your Code Here

numberOfSwaps = 0
for j in range(n):
    for i in range(n-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            numberOfSwaps +=1
print('Array is sorted in {} swaps.'.format(numberOfSwaps))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[-1]))



