'''class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        vis = [False] * 1000
        ans = 0
        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or k == j or digits[k] % 2 != 0:
                        continue
                    x = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if not vis[x]:
                        vis[x] = True
                        ans += 1
        return ans
# Time complexity: o(n^3)
# space complexity: o(1) '''
from collections import Counter
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        available_counts = Counter(digits)
        valid_count = 0
        for num in range(100,1000,2):
            hundreds = num // 100
            tenths = (num // 10) % 10
            units = num % 10
            needed_counts = Counter([hundreds, tenths, units])
            is_possible = True
            for digit, count in needed_counts.items():
                if available_counts[digit] < count:
                    is_possible = False
                    break
            if is_possible:
                valid_count += 1
        return valid_count 
                




      
                

        