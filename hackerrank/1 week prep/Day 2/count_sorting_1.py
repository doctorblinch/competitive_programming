#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr: list[int], forced_size=100):
    index_arr = [0 for _ in range(forced_size)]

    for i in arr:
        index_arr[i] += 1

    return index_arr

if __name__ == '__main__':
    print(countingSort([1,1,3,2,1]))
