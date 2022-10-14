class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        lista_nums = []
        sum = 0
        for num in nums:
            sum += num
            lista_nums.append(sum)
        return lista_nums