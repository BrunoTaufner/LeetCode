class Solution:
    @staticmethod
    def findErrorNums(nums: list[int]) -> list[int]:
        num_repetido = -1
        lista_nums = list(range(1, len(nums) + 1))
        i = 0
        while i < len(nums):
            num = nums[i]
            if num in lista_nums:
                lista_nums.remove(num)
            else:
                num_repetido = num
            i += 1
        if num_repetido > 0:
            lista_nums.insert(0, num_repetido)
        return lista_nums


print(Solution().findErrorNums([2, 2]))
