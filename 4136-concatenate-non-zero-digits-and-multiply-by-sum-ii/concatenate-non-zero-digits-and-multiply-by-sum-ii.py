class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)
        prefix_sum = [0] * (n + 1)
        prefix_num = [0] * (n + 1)
        pow10 = [1] * (n + 1)
        cnt = [0] * (n + 1)
        for i in range(n):
            pow10[i + 1] = (pow10[i] * 10) % MOD
            digit = int(s[i])
            prefix_sum[i + 1] = prefix_sum[i]
            prefix_num[i + 1] = prefix_num[i]
            cnt[i + 1] = cnt[i]
            if digit != 0:
                prefix_sum[i + 1] += digit
                prefix_num[i + 1] = (prefix_num[i] * 10 + digit) % MOD
                cnt[i + 1] += 1
        ans = []
        for l, r in queries:
            summ = prefix_sum[r + 1] - prefix_sum[l]
            non_zero = cnt[r + 1] - cnt[l]
            x = (prefix_num[r + 1]- prefix_num[l] * pow10[non_zero]) % MOD
            ans.append((x * summ) % MOD)
        return ans
#time complexity:o(n+q)
#space complexity:o(n)
    