class Solution(object):
    @staticmethod
    def breakPalindrome(palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''
        index_changed = 0
        num_changing = 30
        i = 0
        while i < len(palindrome):
            num = ord(palindrome[i]) - 96

            if len(palindrome) % 2 == 0 and num - 1 <= num_changing:
                if num == 2:
                    palindrome[i] = chr(num - 1)
                    break
                elif num > 2:
                    num_changing = num - 1
                    index_changed = i


            else:
                k = 0
            i += 1

        return palindrome


print(Solution().breakPalindrome('az'))
