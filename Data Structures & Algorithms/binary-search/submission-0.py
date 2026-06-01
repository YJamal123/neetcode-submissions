class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            print(f"left: {left} and right: {right}")
            middle = (right + left)//2
            print(f"{middle} which is {nums[middle]}")
            if nums[middle] == target: 
                return middle
            elif nums[middle] < target: 
                left = middle + 1
            else:
                print("here")
                right = middle - 1
        return -1