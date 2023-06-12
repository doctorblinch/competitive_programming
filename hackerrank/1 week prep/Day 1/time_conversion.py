#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s: str):
    """
    Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

    Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
    - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
    """
    afternoon = True if s.find('AM') == -1 else False
    hours = int(s[:2])
    if not afternoon:
        if hours == 12:
            return f'00{s[2:-2]}'
        return s[:-2]
    
    
    if hours != 12:
        hours += 12
    return f'{"0" if hours < 10 else ""}{hours}{s[2:-2]}'


if __name__ == '__main__':
    print(timeConversion('07:05:45AM'))
    print(timeConversion('12:15:00PM'))
    print(timeConversion('02:05:45PM'))
    print(timeConversion('12:05:45AM'))
