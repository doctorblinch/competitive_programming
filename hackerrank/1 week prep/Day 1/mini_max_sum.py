#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    """
    Given five positive integers, find the minimum and maximum values that 
    can be calculated by summing exactly four of the five integers. 
    Then print the respective minimum and maximum values as a single 
    line of two space-separated long integers.
    """
    min_num = min(arr)
    max_num = max(arr)
    arr_sum = sum(arr)
    print(
        arr_sum - max_num, arr_sum - min_num
    )

if __name__ == '__main__':
    miniMaxSum([1,3,5,7,9])
