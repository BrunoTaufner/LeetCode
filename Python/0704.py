def binarySearch(nums, target, left, right):
    middle = int(right + left) / 2
    if nums[middle] == target:
        return middle
    if nums[middle] > target:
        
    binarySearch(nums, target, None, None)


class Solution:
    @staticmethod
    def search(nums: list[int], target: int) -> int:

        binarySearch(nums, target, 0, len(nums))
        return 0

print(Solution().search([-1,0,3,5,9,12]))
