class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = -1
        mini = prices[0]
        for i in range(len(prices)):
            mini = prices[0]
            for j in range(1, i):
                if prices[j]<mini:
                    mini = prices[j]
            if maxi < (prices[i] - mini):
                maxi = prices[i] - mini
        if maxi < 0:
            return 0
        return maxi


        
        