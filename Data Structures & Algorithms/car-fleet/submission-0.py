class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p,s] for p , s in zip(position, speed)] #This basically just puts them into pairs (p,s) instead of keeping them in seperated lists.
        stack = []
        for p,s in sorted(pairs)[::-1]: #Syntax to reverse a list 
            time = (target - p) / s
            stack.append(time)
            if (len(stack) >= 2 and stack[-1] <= stack[-2]):
                stack.pop()
        return len(stack)