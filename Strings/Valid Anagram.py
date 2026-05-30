"""
# Problem: Valid Anagram
# Leetcode: 242
# Difficulty: Easy
# Pattern: String + HashMap

Problem:
Return True if t is an anagram of s,
otherwise return False.

Example:
s = "anagram"
t = "nagaram"
Output = True


Idea:
- Count frequency of each character
- Compare frequencies of both strings
- If frequencies match, they are anagrams

Revision:
- Practiced character frequency counting
- Used HashMaps to compare occurrences

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        h1 = {}
        h2 = {}

        for i in s:
            if i not in h1:
                h1[i] = 1
            else:
                h1[i] += 1
        
        for j in t:
            if j not in h2:
                h2[j] = 1
            else:
                h2[j] += 1
        
        return h1 == h2
        