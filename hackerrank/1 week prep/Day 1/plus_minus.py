#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    n = len(arr)
    positive, negative, zero = 0, 0, 0
    
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
    print(positive / n, negative / n, zero / n, sep='\n')
    return 

if __name__ == '__main__':
    # n = int(input().strip())

    # arr = list(map(int, input().rstrip().split()))
    arr = []

    print(plusMinus(arr))
    assert (0.4, 0.4, 0.2)
