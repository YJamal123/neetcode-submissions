class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = defaultdict(set)
        number = set(nums)
        number = sorted(number)
        max = 0
        for num in number: 
            if num-1 in hashmap: 
                hashmap[num] = hashmap[num-1] + 1
                if hashmap[num] > max: 
                    max = hashmap[num]
            else: 
                hashmap[num] = 1
                if hashmap[num] > max: 
                    max = hashmap[num]
        return max