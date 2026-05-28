class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #check each combo
        #start pointer start and end
        #have a max area
        #find smallest val, square, compare with max
        #decrimate or incrimate depending on which 
        #is the smallest value
        start = 0
        end = len(heights) - 1
        max = 0
        print(min(heights[start], heights[end]))
        while start < end:
            lim = min(heights[start], heights[end]) * (end - start)
            if lim > max:
                max = lim
            if min(heights[start], heights[end]) == heights[start]:
                start += 1
            else:
                end -= 1
        return max
                    
            

                
                

