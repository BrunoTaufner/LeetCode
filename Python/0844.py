class Solution:
    def removeCharacters(self, s):
        s = list(s)
        i = 0
        while i < len(s):
            if s[i] == '#':
                del s[i]
                if i > 0:
                    del s[i - 1]
                    i -= 1
                i -= 1
            i += 1
        return str(s)

    def backspaceCompare(self, s: str, t: str) -> bool:
        if self.removeCharacters(s) == self.removeCharacters(t):
            return True
        return False


print(Solution().backspaceCompare('ad#c', 'ac#c'))
