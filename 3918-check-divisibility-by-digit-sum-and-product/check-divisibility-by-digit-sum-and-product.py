class Solution:
    def checkDivisibility(self, n: int) -> bool:
        summ = 0
        product = 1
        i = n
        while i>0:
            digit = i % 10
            i //= 10
            summ += digit
            product *= digit
        return n % (summ+product) == 0




        