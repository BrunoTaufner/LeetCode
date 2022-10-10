import math


class Solution(object):
    @staticmethod
    def breakPalindrome(palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''
        palindrome = list(palindrome)
        letter = 'X'
        index_changed = -1
        i = 0
        while i < math.floor(len(palindrome) / 2):
            num = ord(palindrome[i]) - 96
            if 2 < num < 26:
                letter = 'a'
                index_changed = i
                break
            elif num == 1:
                index_changed = i
            elif num == 2:
                letter = chr(num + 95)
                index_changed = i
                break
            elif num == 26:
                letter = 'a'
                index_changed = i
                break
            i += 1
        if letter != 'X':
            palindrome[index_changed] = letter
        else:
            palindrome[index_changed + math.ceil(len(palindrome) / 2)] = 'b'
        return ''.join(palindrome)


print(Solution().breakPalindrome('oisio'))
