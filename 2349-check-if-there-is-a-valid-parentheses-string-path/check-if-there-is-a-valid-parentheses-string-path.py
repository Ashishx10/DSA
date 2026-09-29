from functools import lru_cache

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        # Total path length must be even
        if (m + n - 1) % 2:
            return False

        @lru_cache(None)
        def dfs(r, c, balance):

            # Process current cell
            if grid[r][c] == '(':
                balance += 1
            else:
                balance -= 1

            # Invalid prefix
            if balance < 0:
                return False

            # Cells remaining after current cell
            remaining = (m - r - 1) + (n - c - 1)

            # Not enough cells left to close all '('
            if balance > remaining:
                return False

            # Destination
            if r == m - 1 and c == n - 1:
                return balance == 0

            # Down
            if r + 1 < m and dfs(r + 1, c, balance):
                return True

            # Right
            if c + 1 < n and dfs(r, c + 1, balance):
                return True

            return False

        return dfs(0, 0, 0)
# time complexity: O(m × n × (m+n))
# space complexity: O(m × n × (m+n))
