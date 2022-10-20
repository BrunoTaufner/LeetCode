class Solution:
    @staticmethod
    def longestPalindrome(s: str) -> str:

        i, j = 0, len(s) - 1
        while i < len(s):
            c = s[i]


            i += 1
            j -= 1

        return s


print(Solution().longestPalindrome('cbabad'))
