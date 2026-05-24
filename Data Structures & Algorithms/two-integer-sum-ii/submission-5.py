class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        answer = []
        while (l < r): 
            sum = numbers[l] + numbers[r]
            if sum == target:
                answer.append(l + 1) 
                answer.append(r + 1) 
                break
            elif target > sum:
                l += 1
            elif target < sum: 
                r -= 1
        return answer