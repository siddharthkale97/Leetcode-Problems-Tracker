class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        i = 0
        j = len(prices) - 1
        minb = float('inf')
        maxp = 0
        for i in range(len(prices)):
            if (prices[i]<minb):
                minb = prices[i]
            elif (maxp< prices[i] - minb):
                maxp = prices[i] - minb
        return int(maxp)