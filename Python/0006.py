def desceVerticalmente(matrix, numRows, index, s):
    pass

class Solution:
    @staticmethod
    def convert(s: str, numRows: int) -> str:
        matriz = []
        for num in range(1, numRows + 1):
            matriz.append('')

        subindo = 0
        j = 0
        for i, c in enumerate(s):
            matriz[j] += c
            if subindo == 0:
                if j < numRows - 1:
                    j += 1
                else:
                    j -= 1
                    subindo = 1
            else:
                if j > 0:
                    j -= 1
                else:
                    j += 1
                    subindo = 0

        return ''.join(matriz)


print(Solution().convert('PAYPALISHIRING', 4))

