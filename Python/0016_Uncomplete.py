class Solution(object):
    @staticmethod
    def threeSumClosest(nums: list[int], target: int) -> int:
        closest_sum = 1234949349382498234923849328493284982918219
        i = 0
        while i < len(nums):
            somatoria = nums[i]
            j = i + 1
            while j < len(nums):
                somatoria += nums[j]
                k = j + 1
                while k < len(nums):
                    somatoria += nums[k]
                    if target >= somatoria:
                        dist_som = target - somatoria
                    else:
                        dist_som = somatoria - target
                    if target >= closest_sum:
                        dist_closest = target - closest_sum
                    else:
                        dist_closest = closest_sum - target
                    if dist_som < dist_closest:
                        closest_sum = somatoria
                    somatoria -= nums[k]
                    k += 1
                somatoria -= nums[j]
                j += 1
            i += 1

        return closest_sum


print(Solution().threeSumClosest([1, 1, 1, 1], 4))
