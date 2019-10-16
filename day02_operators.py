import math
import os
import random
import re
import sys


# Complete the solve function below.

def solve(meal_cost, tip_percent, tax_percent):
    if __name__ == '__main__':
        meal_cost = float(input())

        tip_percent = int(input())

        tax_percent = int(input())

        # meal cost
        meal_cost = meal_cost
        # calculate tip cost
        tip_cost = meal_cost * (tip_percent / 100)
        # calculate tax cost
        tax_cost = meal_cost * (tax_percent / 100)
        # total bill cost with rounding off
        totalCost = round(meal_cost + tip_cost + tax_cost)

        print(totalCost)

solve(12.00, 20, 8)
