"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Approach: Brute force → nested loop (later upgrade to hashmap)

Description:

Complexity:
Time:  O(n²)
Space: O(1)
"""

#code goes here




""" 
# SOLUTION NOTES

## Approach
- Use a hashmap to store numbers we've already seen
- For each number, check if (target - number) exists in the map
- If yes → we found the pair, return indices
- If no → store current number with its index

## Why this works
Instead of re-scanning the array for the complement (O(n²)),
the map gives us O(1) lookup. One pass total.

## Complexity
Time: O(n) — single pass
Space: O(n) — hashmap stores up to n elements

## What I learned
- Trade space for time — classic hashmap pattern
- First tried brute force O(n²), then optimized
"""