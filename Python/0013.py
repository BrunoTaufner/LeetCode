class Solution:
    @staticmethod
    def romanToInt(s: str) -> int:
        numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        for i, c in enumerate(s):
            if i + 1 < len(s) and numbers[s[i + 1]] > numbers[c]:
                num -= numbers[c]
            else:
                num += numbers[c]

        return num


print(Solution().romanToInt('MCMXCIV'))

