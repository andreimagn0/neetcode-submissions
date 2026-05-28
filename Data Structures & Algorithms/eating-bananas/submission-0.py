import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #min pointer = 0, max = greatest val in array
        #find max val in the array first
        #then while min <= max:
        target = 0
        minP, maxP = 1, max(piles)
        while minP <= maxP:
            mid = (maxP + minP) // 2
            isWithin = 0
            for i in range(len(piles)):
                isWithin += math.ceil(piles[i] / mid)
            if isWithin <= h:
                target = mid
                maxP = mid - 1
            else:
                minP = mid + 1
        return target

            