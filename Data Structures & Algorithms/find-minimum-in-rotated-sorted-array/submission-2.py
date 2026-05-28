class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        considering this is a BS problem, we would need pointers from
        the start and end to find the mid point
        we could check the size of the array so we know how many numbers
        there to check, if we have the start and end pointer, we would know if 
        the difference between them is 
        """
        start, end = 0, len(nums) - 1
        ans = float('inf')
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                ans = min(ans, nums[end])
                start = mid + 1
            else:
                ans = min(ans, nums[mid])
                end = mid - 1

        return ans