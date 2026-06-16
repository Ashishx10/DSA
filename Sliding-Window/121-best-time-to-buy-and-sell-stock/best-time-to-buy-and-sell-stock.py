class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        maxp=0
        n=len(prices)
        for r in range(1,n):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxp=max(maxp,profit)
            else:
                l=r
        return maxp
#time complexity:o(n)
#space complexity:o(1)