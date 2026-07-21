class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        runningsum=0
        minsum=0
        for num in nums:
            runningsum+=num
            minsum=min(minsum,runningsum)
        return -minsum+1 if minsum<1 else 1
