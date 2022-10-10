class Solution(object):
    @staticmethod
    def breakPalindrome(palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''
        word = ''
        i = 0
        while i < len(palindrome):
            printx(ord(palindrome[i]))
            i += 1

        return palindrome


print(Solution().breakPalindrome('aabbcc'))
