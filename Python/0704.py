def binarySearch(nums, target, left, right):
    middle = int((right + left) / 2)
    if nums[middle] == target:
        return middle
    elif left + 1 == right:
        return -1
    elif nums[middle] > target:
        return binarySearch(nums, target, left, middle)
    else:
        return binarySearch(nums, target, middle, right)


class Solution:
    @staticmethod
    def search(nums: list[int], target: int) -> int:
        num = binarySearch(nums, target, 0, len(nums))
        return num

print(Solution().search([5], 5))
