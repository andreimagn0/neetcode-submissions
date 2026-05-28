class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1
        while low <= high:
            mid = (low + high) // 2
            mid_val = matrix[mid // n][mid % n]
            
            if mid_val == target:
                return True
            if mid_val < target:
                low = mid + 1
            else:
                high = mid - 1
        return False