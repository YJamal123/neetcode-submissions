class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ours = set()
        for num in nums:
            if num not in ours:
                ours.add(num)
            elif num in ours:
                return True
        return False