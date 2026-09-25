class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        result = set()
        def dfs(exp):
            # No more braces → complete word
            if "}" not in exp:
                result.add(exp)
                return
            # Find first closing brace
            j = exp.find("}")
            # Find its matching opening brace
            i = exp.rfind("{", 0, j)
            # Parts before and after the braces
            left = exp[:i]
            right = exp[j + 1:]
            # Options inside the braces
            options = exp[i + 1:j].split(",")
            # Try every option
            for option in options:
                dfs(left + option + right)
        dfs(expression)
        return sorted(result)