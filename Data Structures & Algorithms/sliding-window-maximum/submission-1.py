class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        maxEl, cur, left = [], [], 0
        for num in range(k):
            cur.append(nums[num])
        maxEl.append(max(cur))

        for i in range(k, len(nums)):
            cur.append(nums[i])
            window = i - left + 1
            while window > k:
                cur.pop(0)
                left += 1
                window = i - left
            maxEl.append(max(cur))
        return maxEl
