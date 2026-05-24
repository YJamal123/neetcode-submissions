class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pool = set()
        left = 0
        answer = 0
        for i in range(len(s)):
            while s[i] in pool: 
                pool.remove(s[left])
                left += 1
            pool.add(s[i])
            answer = max(answer, len(pool))
        return answer