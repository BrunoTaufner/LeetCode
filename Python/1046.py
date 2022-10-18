class Solution:
    @staticmethod
    def lastStoneWeight(stones: list[int]) -> int:

        while len(stones) > 1:
            x, y = 0, 1
            i = 0
            while i < len(stones):
                if stones[x] < stones[i] and stones[x] <= stones[y] and i != y:
                    x = i
                elif stones[y] < stones[i] and x != i:
                    y = i
                i += 1
            if stones[x] != stones[y]:
                sub = abs(stones[x] - stones[y])
                if x < y:
                    del stones[y]
                    stones[x] = sub
                else:
                    del stones[x]
                    stones[y] = sub
            else:
                if x < y:
                    del stones[y]
                    del stones[x]
                else:
                    del stones[x]
                    del stones[y]
        if len(stones) == 0:
            return 0
        return stones[0]
