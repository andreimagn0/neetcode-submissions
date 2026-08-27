class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        use two pointer, check max height at each right pointer
        we need a condition to move the left pointer
        if current right pointer is greater than the left pointer
        we move that pointer left
        we can start from 0 and 1 and go until the end 
        '''
        best = 0
        l, r = 0, len(heights) - 1
        while l < r:
            curr_best = min(heights[l], heights[r]) * (r - l)
            best = max(best, curr_best)
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        return best
            