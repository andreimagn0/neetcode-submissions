class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_dup = len(nums) != len(set(nums))
        return has_dup
        
   