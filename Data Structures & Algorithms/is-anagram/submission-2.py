class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = dict()
        second = dict()
        for i in range(len(s)):
            if s[i] in first:
                first[s[i]] += 1
            else:
                first[s[i]] = 1
        for i in range(len(t)):
            if t[i] in second:
                second[t[i]] += 1
            else:
                second[t[i]] = 1
        return first == second