class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs: 
            string += "$" + str(len(s)) + "$"
            string += s
        return string
    def decode(self, s: str) -> List[str]:
        i = 0
        l = []
        while (i<len(s)):
            if s[i] == "$":
                ind = s.find("$", i+1)
                num = int(s[i+1:ind])
                l.append(s[ind+1:ind+num+1])
                i = ind + num
            i += 1
        return l