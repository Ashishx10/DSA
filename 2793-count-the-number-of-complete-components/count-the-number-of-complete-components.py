from collections import defaultdict
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        answer = 0
        def dfs(node):
            visited.add(node)
            nodes = 1
            degree = len(graph[node])
            for nei in graph[node]:
                if nei not in visited:
                    x, y = dfs(nei)
                    nodes += x
                    degree += y
            return nodes, degree
        for i in range(n):
            if i not in visited:
                nodes, degree = dfs(i)
                edge_count = degree // 2
                required = nodes * (nodes - 1) // 2
                if edge_count == required:
                    answer += 1
        return answer