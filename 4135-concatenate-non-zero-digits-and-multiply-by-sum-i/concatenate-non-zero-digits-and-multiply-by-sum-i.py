class Solution:
    def sumAndMultiply(self, n: int) -> int:
        summ=0
        res=[]
        while n>0:
            digits=n%10
            if digits!=0:
                res.append(digits)
                summ+=digits
            n//=10
        x=0
        while res:
            x=x*10+res.pop()
        return x*summ
#time complexity:o(logn)
#space complexity:o(logn)

        