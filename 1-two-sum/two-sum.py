class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        have={}
        for i in range(n):
            need=target-nums[i]
            if need in have:
                return[have[need],i]
            have[nums[i]]=i
#time complexity:o(n)
#space complexity:o(n)