class Solution:
    @staticmethod
    def myAtoi(s: str) -> int:
        num = ''
        for c in s:
            if len(num) > 0 and 48 >= ord(c) >= 57:
                break
            if 48 <= ord(c) <= 57 or c == '-':
                num += c
        try:
            num = int(num)
        except:
            return 0
        if num > (2 ** 31) - 1:
            return (2 ** 31) - 1
        if num < -2 ** 31:
            return -2 ** 31
        return num

print(Solution().myAtoi(' +0 123'))
