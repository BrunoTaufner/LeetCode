class Solution:
    @staticmethod
    def reverse(x: int) -> int:
        print(2**31)
        if x < 0:
            x = list(str(x))
            x.reverse()
            x.insert(0, '-')
            x.pop()
        else:
            x = list(str(x))
            x.reverse()
        res = int(''.join(x))

        return res

print(Solution().reverse(1534236469))