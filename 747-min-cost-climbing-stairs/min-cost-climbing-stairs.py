'''
#recursive solution
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        def min_cost(i):
            if i < 2:
                return 0
            return min(cost[i-2] + min_cost(i-2), cost[i-1] + min_cost(i-1))
        return min_cost(n)
# time complexity: o(2^n)
# space complexity: o(n)
'''   
# Top Down approach(Memoization)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {0:0,1:0}
        def min_cost(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = min(cost[i-2] + min_cost(i-2), cost[i-1] + min_cost(i-1))
            return memo[i]
        return min_cost(n)