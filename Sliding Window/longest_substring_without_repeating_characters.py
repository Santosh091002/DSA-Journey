# Problem: Longest Substring Without Repeating Characters
# Leetcode: 3
# Difficulty: Medium
# Pattern: Sliding Window

"""
Approach:
- Use sliding window
- Store frequencies in hashmap
- Shrink window when duplicate appears
"""

s = "pwwkew"

def LongSub(s):

    i = 0
    j = 0
    h = {}
    length = 0

    while j < len(s):

        if s[j] not in h:
            h[s[j]] = 1
        else:
            h[s[j]] += 1

        while h[s[j]] > 1:
            h[s[i]] -= 1

            if h[s[i]] == 0:
                h.pop(s[i])

            i += 1

        length = max(length, j - i + 1)

        j += 1

    return length

print(LongSub(s))