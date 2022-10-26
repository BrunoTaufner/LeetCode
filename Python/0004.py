class Solution:
    @staticmethod
    def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
        
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        if len(nums1) % 2 == 0:
            middle = int(len(nums1) / 2)
            media = (nums1[middle] + nums1[middle - 1]) / 2
        else:
            middle = int(len(nums1) / 2)
            media = nums1[middle]
        return media

print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
