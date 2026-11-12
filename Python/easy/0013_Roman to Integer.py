"""
Problem: Roman to Integer 
Link: https://leetcode.com/problems/roman-to-integer/
Difficulty: Easy
Approach: 

Description: roman to integer

Complexity:
Time:  O
Space: O
"""

#code goes here
class Solution:
    def romanToInt(self, s: str) -> int:
        roman={ 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result=0
        i=0
        while i<len(s):
            if i!=len(s)-1:
                if roman[s[i]]<roman[s[i+1]]:
                    result += roman[s[i]]
                else:
                    result = result + (roman[s[i+1]]-roman[s[i]])
                    i=i+1
                    
                i=i+1
            else:
                result = result + roman[s[i]]
                i=i+1

        return result





""" 
# SOLUTION NOTES

## Approach
- we can start by mapping the roman numerals to their correspoinding values
- since we know a large numeral comes before small numeal suhc numerals cna be directly calulated from the mapping and added to result
- if we find a small numeral then a larger numeral, we simple subtract them and add to result
- now traverse throught string of roman numeral always checking by pairs and implement hthis logic
- if the character is a V X or C, check it s follwing character

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