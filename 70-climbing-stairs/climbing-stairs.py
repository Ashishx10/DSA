# recursive approach
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-2) + self.climbStairs(n-1)
'''

'''
# Top Down (memotization) approach
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}
        def f(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = f(n-2) + f(n-1)
                return memo[n]
        return f(n)
'''

'''
# Bottom Up (tabulation) approach
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * n
        dp[1] = 0
        dp[2] = 1
        for i in range(2,n):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n-1]
'''

# Bottom Up (tabulation) approach with optimisation
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev = 1
        curr = 2
        for i in range(2,n):
            prev,curr = curr, prev+curr
        return curr
