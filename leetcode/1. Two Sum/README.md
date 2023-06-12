# [1. Two Sum](https://leetcode.com/problems/two-sum)

Difficulty: **Easy**

Feels like: **Easy**

Language: **Python3**

## Problem description

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Solution idea

The problem could be easily solved with two nested loops with time - $O(n^2)$, memory - $O(1)$, but such solution is not time-optimal. This is why hash tables were used with a single loop. The idea is that we have a hash-table with elements differences to the target element, we iterate through our elements and check if it has a pair element in dictionary already if yes - return the pair, if not - add to the dict.

## Complexity

### Time

Since in worst case scenario we will iterate over all the input array once, so time complexity is $O(n)$.

### Memory

To achieve speed we need to have a hash-table maximum size of which is equal to $O(n)$.
