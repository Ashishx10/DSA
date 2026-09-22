class Solution:
    def arraySign(self, nums: list[int]) -> int:
        product_sign = 1
        for x in nums:
            if x == 0:
                return 0
            elif x < 0:
                product_sign *= -1
        return product_sign
# time complexity: o(n)
# space complexity: o(1)
