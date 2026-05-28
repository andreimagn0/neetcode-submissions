class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup = set()
        l, maxV = 0, 0
        for i in range(len(s)):
            while s[i] in dup:
                dup.remove(s[l])
                l += 1
            dup.add(s[i])
            maxV = max(maxV, i - l + 1)
        return maxV
            
