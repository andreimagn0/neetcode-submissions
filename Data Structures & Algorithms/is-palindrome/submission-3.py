class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(s_str)
        start, end = 0, len(s_str) - 1
        while start < end:
            if s_str[start] == s_str[end]:
                start += 1
                end -= 1
            else:
                return False
        return True