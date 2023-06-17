#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def calculate_diagonal_1(arr):
    diag_sum = 0

    for i in range(len(arr)):
        diag_sum += arr[i][i]

    return diag_sum
    

def calculate_diagonal_2(arr):
    diag_sum = 0
    n = len(arr)

    for i in range(n):
        diag_sum += arr[n-1-i][i]

    return diag_sum


def diagonalDifference(arr: list[int]):
    """
    Given a square matrix, calculate the absolute difference between 
    the sums of its diagonals.
    """
    return abs(calculate_diagonal_1(arr) - calculate_diagonal_2(arr))

if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]
    print(diagonalDifference(matrix))  
