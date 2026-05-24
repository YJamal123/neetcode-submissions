class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        l = 0
        r = len(s) - 1
        while (l < r):
            if(s[l].isalnum()):
                if(s[r].isalnum()):
                    if (s[l] != s[r]):
                        return False
                    else:
                        l += 1
                        r -= 1
                else:
                    r -= 1
            else:
                l += 1
        return True