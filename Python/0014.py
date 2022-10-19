class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        i = 0
        j = 0
        prefix = ''
        menor_tam = None
        while j < len(strs[i]):
            last_char = strs[i][j]
            while i < len(strs):
                if menor_tam is None:
                    menor_tam = len(strs[i])
                if len(strs[i]) < menor_tam:
                    menor_tam = len(strs[i])
                if j < len(strs[i]):
                    if last_char != strs[i][j]:
                        return prefix
                    last_char = strs[i][j]
                i += 1
            if j < menor_tam:
                prefix += strs[i - 1][j]
            i = 0
            j += 1

        return prefix


print('str:', Solution().longestCommonPrefix(["aaa", "aa", "aaa"]))
