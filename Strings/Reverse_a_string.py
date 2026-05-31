
"""
# Problem: Reverse String
# Difficulty: Easy
# Pattern: Two Pointers

Problem:
Reverse a string and return the reversed string.

Example:
s = "Santosh"
Output = "hsotnaS"


Idea:
- Use two pointers
- One starts from the beginning
- One starts from the end
- Swap characters until both pointers meet

Revision:
- Practiced Two Pointer technique
- Reversed string without using slicing [::-1]

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def reverseString(self, String):
        String = list(String)
        i = 0
        j = len(String) - 1

        while i < j:
            String[i], String[j] = String[j],String[i]
            i += 1
            j -= 1
        return "".join(String)

s = Solution()
r = s.reverseString("Santosh")
print(r)