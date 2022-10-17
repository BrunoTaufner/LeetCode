class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones.sort(reverse=True)
        x, y = -1, -1
        i = 0
        while i < len(stones):

            print(f'{i}ª stone: {stones[i]}')
            if stones[i] > x:
                x = i
            if stones[i] < x:
                del stones[x]
                del stones[y - 1]


            # elif stones[i] == stones[j]:
            #     print(stones)
            #     del stones[i]
            #     del stones[j - 1]
            #     print(stones)
            #     i -= 2
            #     j -= 1
            i += 1

        return i

print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]))
