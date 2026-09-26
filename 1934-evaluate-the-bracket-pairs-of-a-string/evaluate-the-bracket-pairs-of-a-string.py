class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = {k: v for k, v in knowledge}
        stack = []
        is_key = False
        current_key = []
        
        for char in s:
            if char == '(':
                is_key = True
            elif char == ')':
                is_key = False
                key_str = "".join(current_key)
                stack.append(d.get(key_str, '?'))
                current_key = []  # Reset for the next bracket pair
            elif is_key:
                current_key.append(char)
            else:
                stack.append(char)
                
        return "".join(stack)
