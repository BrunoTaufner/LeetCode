class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.sum = 0

    def paths(self, x: int, y: int):
        if x == self.m - 1 and y == self.n:
            self.sum += 1
        if x + 1 < self.m:
            self.paths(x + 1, y)
        if y + 1 < self.n:
            self.paths(x, y + 1)

    def uniquePaths(self, m: int, n: int) -> int:
        self.m = m - 1
        self.n = n - 1
        self.sum = 0
        self.paths(0, 0)

        return self.sum


print(Solution().uniquePaths(23, 12))
