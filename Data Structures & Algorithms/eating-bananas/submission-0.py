import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        
        while low < high:
            mid = (low + high) // 2
            
            hours_spent = 0
            for pile in piles:
                hours_spent += (pile + mid - 1) // mid
            
            if hours_spent <= h:
                high = mid
            else:
                low = mid + 1
                
        return low