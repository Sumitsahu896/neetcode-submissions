class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        L = 0
        longestString = 0
        for R in range(len(s)):
            if s[R] in hashset:
                while s[R] in hashset:
                    hashset.remove(s[L])
                    L += 1
            hashset.add(s[R])
            longestString = max(longestString, R - L + 1)
        return longestString