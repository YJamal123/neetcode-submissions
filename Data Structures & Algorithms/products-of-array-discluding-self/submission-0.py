class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        for i in range(len(nums)):
            if i == 0: 
                prefix.append(1)
            else:
                prefix.append(nums[i-1]*prefix[i-1])
        print(prefix)
        nums.reverse()
        postfix = []
        for i in range(len(nums)):
            if i == 0:
                postfix.append(1)
            else:
                postfix.append(nums[i-1]*postfix[i-1])
        postfix.reverse()
        prod = []
        for i in range(len(nums)):
            prod.append(prefix[i] * postfix[i])
        return prod
        print(postfix)