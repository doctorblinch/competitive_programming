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

def diagonalDifference(arr: list[int]):
    """
    Given a square matrix, calculate the absolute difference between 
    the sums of its diagonals.
    """
    primary_diag_sum = 0
    secondary_diag_sum = 0
    n = len(arr)

    for i in range(n):
        primary_diag_sum += arr[i][i]
        secondary_diag_sum += arr[n-1-i][i]

    return abs(primary_diag_sum - secondary_diag_sum)

if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]
    print(diagonalDifference(matrix))  
