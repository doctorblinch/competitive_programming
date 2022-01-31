# [38. Count and Say](https://leetcode.com/problems/count-and-say)

Difficulty: **Medium**

Feels like: **Easy**

Language: **Python3**

## Problem description

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

- $countAndSay(1) = "1"$

- $countAndSay(n)$ is the way you would "say" the digit string from $countAndSay(n-1)$, which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

For example, the saying and conversion for digit string "3322251":

![Example](https://assets.leetcode.com/uploads/2020/10/23/countandsay.jpg)

Given a positive integer $n$, return the $n^{th}$ term of the **count-and-say** sequence.

## Solution idea

The task is solved recursively, we pass trough each character of the given string and count how long is each number sequence adding the required numbers.

## Complexity

### Time

We recursively pass trough each value until $n$, so time complexity is - $O(n)$. Inside of each function call we iterate over the entire input string.

### Memory

Even though we do not store additional sequences, so $O(1)$. Nevertheless, it is worth to mention that the size of the result string size soars, for instance $countAndSay(50)$ result is around 800k characters long.
