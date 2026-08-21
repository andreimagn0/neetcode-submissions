class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        curr = {}
        for index, num in enumerate(nums):
            complement = target - num

            if complement in curr:
                return [curr[complement], index]
            
            curr[num] = index