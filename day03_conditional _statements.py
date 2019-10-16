import math
import os
import random
import re
import sys
import random


if __name__ == '__main__':
    for x in range(10):
        a = random.randint(1, 101)

        N = a # int(input())
        print(N)

        # If is odd, print Weird
        if N % 2 != 0:
            print("Weird")
            break
        # If is even and in the inclusive range(2,5) print Not Weird
        elif N % 2 == 0 and N in range(2, 6):
            print("Not Weird")
            break
        # # If is even and in the inclusive range(6,20) print Weird
        elif N % 2 == 0 and N in range(6, 21):
            print("Weird")
            break
        # If is even and greater 20, print Not Weird
        elif N % 2 == 0 and N > 20:
            print("Not Weird")
            break