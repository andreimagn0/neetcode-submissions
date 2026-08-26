from collections import defaultdict

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}
        for i in arr:
            if i not in count:
                count[i] = 0
            count[i] += 1
        for i in arr:
            if count[i] == 1:
                k -= 1
            if k == 0:
                return i
        return ""
