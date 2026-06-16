class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        maxp=0
        n=len(prices)
        while r<n:
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxp=max(maxp,profit)
            else:
                l=r
            r+=1
        return maxp
#time complexity:0(n)
#space complexity:0(1)