#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    if n % 2 == 0:
        return (sorted_arr[n//2-1] + sorted_arr[n//2-2]) / 2
        
    return sorted_arr[n//2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
