def isBadVersion(n):
    bad = 1
    if n < bad:
        return False
    else:
        return True


def binarySearch(n):
    left = 1
    right = n + 1
    if isBadVersion(n) and n == 1:
        return n
    while left + 1 <= right:
        middle = int((left + right) / 2)
        atual = isBadVersion(middle)
        anterior = isBadVersion(middle - 1)
        if atual and not anterior:
            return middle
        if isBadVersion(middle):
            right = middle
        else:
            left = middle

    return None


class Solution:

    def firstBadVersion(self, n: int):
        return binarySearch(n)

print(Solution().firstBadVersion(2))
