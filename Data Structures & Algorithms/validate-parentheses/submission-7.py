class Solution:
    def isValid(self, s: str) -> bool:
        
        hash = {
            "(": ")",
            "{" : "}",
            "[" : "]"
        }
        stack = []
        for i in range(len(s)):
            if s[i] in hash: 
                stack.append(s[i])
            else: 
                if len(stack) > 0: 
                    latest = stack.pop()
                else: return False
                if hash[latest] != s[i]:
                    return False
        return len(stack) == 0