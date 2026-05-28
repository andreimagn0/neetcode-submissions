class Solution:
    def search(self, nums: List[int], target: int) -> int:
        found = False
        start, end = 0, (len(nums) - 1)
        #need two pointers one at start and end
        #check first if the current nums/2 is equal to the target
        #if so, return that index
        #if target is greater than the current nums/2, start == nums/2
        #else, end == nums/2
        #base case: we stop the while loop when the external list len is equal
        #to 1, or when start == end
        while start <= end:
            mid = int((start + end) / 2)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1
