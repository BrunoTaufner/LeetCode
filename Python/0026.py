class Solution:
    @staticmethod
    def removeDuplicates(nums: list[int]) -> int:
        i = 0
        nums_set = sorted(list(set(nums)))
        while i < len(nums):
            if i < len(nums_set):
                nums[i] = nums_set[i]
            else:
                nums[i] = '_'
            i += 1
        print(nums)
        return len(nums_set)


print(Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
