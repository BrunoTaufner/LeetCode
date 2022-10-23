class Solution:
    @staticmethod
    def myAtoi(s: str) -> int:
        num = ''
        for c in s:
            if (ord(c) < 48 or ord(c) > 57) and ((len(num) < 1 and c != ' ' and c != '-' and c != '+') or len(num) >= 1):
                break
            if 48 <= ord(c) <= 57 or c == '-' or c == '+':
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

print(Solution().myAtoi('     +-42'))
