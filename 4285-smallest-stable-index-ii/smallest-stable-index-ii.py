class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        minvalue = [inf] * (n-1) + [nums[-1]]
        for i in range(n-2,-1,-1):
            minvalue[i] = min(minvalue[i+1],nums[i])
        maxvalue = 0
        for i in range(n):
            maxvalue = max(maxvalue,nums[i])
            if maxvalue - minvalue [i] <= k:
                return i
        return -1