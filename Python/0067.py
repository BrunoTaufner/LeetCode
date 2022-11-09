class Solution:
    @staticmethod
    def addBinary(a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        num_resultante = []
        sobra = 0
        while i >= 0 or j >= 0:
            num1 = int(a[i])
            num2 = int(b[j])
            if i < 0:
                num1 = 0
            if j < 0:
                num2 = 0

            soma = num1 + num2 + sobra
            if soma > 1:
                if soma == 2:
                    sobra = 1
                    num_resultante.insert(0, 0)
                else:
                    sobra = 1
                    num_resultante.insert(0, 1)
                if i <= 0 and j <= 0:
                    num_resultante.insert(0, 1)
            else:
                sobra = 0
                num_resultante.insert(0, soma)

            if i >= 0:
                i -= 1
            if j >= 0:
                j -= 1

        return ''.join(map(str, num_resultante))


print(Solution().addBinary('11', '1'))
