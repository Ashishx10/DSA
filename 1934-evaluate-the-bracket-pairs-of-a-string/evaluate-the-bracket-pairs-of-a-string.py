class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = {k: v for k, v in knowledge}
        
        # Split by opening bracket
        parts = s.split('(')
        ans = [parts[0]]  # The first part never starts with a key
        
        for part in parts[1:]:
            # Every subsequent part contains exactly one ')'
            key, text = part.split(')')
            ans.append(d.get(key, '?'))
            ans.append(text)
            
        return "".join(ans)
