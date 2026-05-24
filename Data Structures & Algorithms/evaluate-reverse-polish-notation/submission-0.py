class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        operators = {
            '+' : lambda a, b: a + b,
            '-' : lambda a, b: a - b,
            '*' : lambda a, b: a * b,
            '/' : lambda a, b: a / b
        }
        for token in tokens:
            if token not in operators:
                res.append(token)
            else:
                right = int(res.pop())
                left = int(res.pop())
                op = operators.get(token)
                val = op(left, right)
                res.append(val)
        return int(res[0])


        