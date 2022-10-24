class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        pilha = []
        for c in s:
            try:
                if c == '(' or c == '[' or c == '{':
                    pilha.append(c)
                else:
                    abre_c = pilha.pop()
                    if abre_c == '(':
                        fecha_c = ')'
                    elif abre_c == '[':
                        fecha_c = ']'
                    else:
                        fecha_c = '}'
                    if fecha_c != c:
                        return False
            except:
                return False
        if len(pilha) > 0:
            return False
        return True


print(Solution().isValid('(('))
