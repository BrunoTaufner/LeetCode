badversion = 6


def isBadVersion(num: int) -> bool:
    if num < badversion:
        return False
    else:
        return True


class Solution:

    @staticmethod
    def binarySearch(n):
        left = 0
        right = n
        print(isBadVersion(n))
        while left + 1 == right:
            middle = int((left + right) / 2)
            if isBadVersion(middle):
                
        return 2

    def firstBadVersion(self, n: int) -> int:
        return self.binarySearch(n)


Solution().binarySearch(10)
