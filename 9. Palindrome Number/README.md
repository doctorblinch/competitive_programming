# 9. Palindrome Number

Difficalty: **Easy**

Feels like: **Easy**

Language: **Python3**

## Problem description

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

## Solution idea

The idea is to get till the middle of the number and check if halves are equal or half // 10 is equal to another one (in case number has odd quantity of digits). In addition some initial checks are provided for some edge cases.

## Complexity

Both time and memory complexities are $O(n)$ (where n - length of the number) because we only store at most half of the number in an integer variable and timewise we loop till the middle of the number.
