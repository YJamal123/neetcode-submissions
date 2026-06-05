class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        size = total // 2
        small = nums1 if len(nums1) <= len(nums2) else nums2
        big = nums2 if len(nums1) <= len(nums2) else nums1
        l = 0
        r = len(small) - 1
        while True:
            m = (l + r) // 2
            remaining = size - (m + 1)
            left1 = small[m] if m >= 0 else float('-inf')
            right1 = small[m + 1] if m + 1 < len(small) else float('inf')
            left2 = big[remaining - 1] if remaining > 0 else float('-inf')
            right2 = big[remaining] if remaining < len(big) else float('inf')
            if left1 <= right2 and left2 <= right1:
                if total % 2 == 1:
                    return min(right1, right2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                r = m - 1
            else:
                l = m + 1