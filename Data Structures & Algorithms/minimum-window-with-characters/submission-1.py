class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        for char in t:
            freq[char] = freq.get(char, 0) + 1
        
        curr = {}

        have = 0
        need = len(freq)

        best_len = float("inf")
        best_window = ""

        l = 0
        for i in range(len(s)):
            curr[s[i]] = curr.get(s[i], 0) + 1
            c = s[i]

            if c in freq and curr[c] == freq[c]:
                have += 1
            
            while have == need:
                current_len = i - l + 1
                if current_len < best_len:
                    best_len = current_len
                    best_window = s[l:i+1]
                left_char = s[l]
                curr[left_char] -= 1
                if left_char in freq and curr[left_char] < freq[left_char]:
                    have -= 1
                l += 1
        return best_window