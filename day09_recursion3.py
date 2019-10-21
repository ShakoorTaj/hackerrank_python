# n = 3 #int(input())
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(fact)


# def factorial(n):
#     # n = int(input('Enter number: '))
#     if n <= 1:
#         return 1
#     else:
#         result = n * factorial(n-1)
#         return result
# n = 3
# obj = factorial(n)
# print(obj)


# solved solution for Hacker Rank editor ...
# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the factorial function below.
def factorial(n):
    if n <= 1:
        return 1
    else:
        result = n * factorial(n-1)
        return result


print(factorial(int(input())))
