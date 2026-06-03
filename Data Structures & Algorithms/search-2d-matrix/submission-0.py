class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while left <= right: 
            middle = (right + left) // 2
            print(f"left={left}, right={right}, middle={middle}, matrix[middle][0 ={matrix[middle][0]}")
            if matrix[middle][0] > target: 
                right = middle - 1
            elif matrix[middle][0] < target:
                print(f"last element={matrix[middle][-1]}")
                if matrix[middle][-1] >= target:#Found the row target should be in
                    l = 0
                    r = len(matrix[middle]) - 1
                    while l <= r: 
                        inside = (l + r)//2
                        if matrix[middle][inside] == target: 
                            return True
                        elif matrix[middle][inside] < target: 
                            l = inside + 1
                        else: 
                            r = inside - 1
                    return False
                else: 
                    left = middle + 1
            elif matrix[middle][0] == target: 
                return True
        return False