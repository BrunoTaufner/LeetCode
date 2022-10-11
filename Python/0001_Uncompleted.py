class Solution:
    @staticmethod
    def twoSum(nums: list[int], target: int) -> list[int]:
        closest_sum = 21389128390128
        listinha = []
        lista = []
        i = 0
        while i < len(nums) - 1:
            soma = nums[i]
            lista.append(i)
            j = i + 1
            while j < len(nums):
                soma += nums[j]
                lista.append(j)
                if target >= soma:
                    dist_target_soma = target - soma
                else:
                    dist_target_soma = soma - target
                if target >= closest_sum:
                    dist_target_cl = target - closest_sum
                else:
                    dist_target_cl = closest_sum - target
                if dist_target_cl > dist_target_soma:
                    closest_sum = soma
                    listinha = lista.copy()
                soma -= nums[j]
                lista.pop()
                j += 1
            lista.pop()
            i += 1
        return listinha

print(Solution.twoSum([0,4,3,0], 0))
