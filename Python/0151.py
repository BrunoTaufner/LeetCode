class Solution:
    @staticmethod
    def reverseWords(s: str) -> str:
        words = s.split(' ')
        words = list(filter(lambda word: word != '', words))
        words.reverse()
        return ' '.join(words)


print(Solution().reverseWords('Hello World  '))
