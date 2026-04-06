class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        prof = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if(prices[j] - prices[i]) > prof:
                    prof = prices[j] - prices[i]
        return prof


