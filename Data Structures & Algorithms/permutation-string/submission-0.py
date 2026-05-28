class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1, freq2, left = {}, {}, 0
        for char in s1:
            freq1[char] = freq1.get(char, 0) + 1
        for i in range(len(s2)):
            while i - left >= len(s1):
                freq2[s2[left]] -= 1
                if freq2[s2[left]] == 0:
                    del freq2[s2[left]]
                left += 1
            freq2[s2[i]] = freq2.get(s2[i], 0) + 1
            if freq1 == freq2:
                return True
        return False