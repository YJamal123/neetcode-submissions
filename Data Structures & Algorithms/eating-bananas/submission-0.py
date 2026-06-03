import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 
        right = max(piles)
        curr = max(piles)
        while left <= right : 
            middle = (left + right)//2
            total = 0
            for i in range(len(piles)):
                total += math.ceil(piles[i]/middle)
            if total > h: 
                left = middle + 1
            elif total <= h: 
                curr = min(middle, curr)
                right = middle - 1
        return curr