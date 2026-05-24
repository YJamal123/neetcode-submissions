class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = dict()
        for i in nums: 
            if i in dictionary: 
                dictionary[i] += 1
            else:
                dictionary[i] = 1
        l = []
        for key,value in dictionary.items():
            t = (value,key)
            l.append(t)
        l.sort()
        l.reverse()
        ans = []
        for i in range(k):
            ans.append(l[i][1])
        return ans