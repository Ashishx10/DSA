class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        # Sort the array in ascending order
        nums.sort()
        # Swap adjacent elements (step by 2)
        for i in range(0, len(nums), 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums
