// https://leetcode.com/problems/intersection-of-two-arrays-ii

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1
        
        count = Counter(nums1)
        union = []
        for num in nums2:
            if num in count and count[num]:
                union.append(num)
                count[num] -= 1
        return union