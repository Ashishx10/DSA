class Solution:
    def fib(self, n: int) -> int:
       # bottom up approach
        if n == 0:
            return 0
        if n == 1:
            return 1
        #dp = [0] * (n+1)
        #dp[0] = 0
        #dp[1] = 1
        prev = 0
        curr = 1
        for i in range(2,n+1):
            #dp[i] = dp[i-2] + dp[i-1]
            prev,curr = curr, prev + curr
        return curr
        #return dp[n]
# time complexity: o(n)
# space complexity: o(1)      