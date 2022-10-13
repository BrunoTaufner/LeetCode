from operator import attrgetter


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __retr__(self):
        string = '['
        node = self
        while True:
            string += str(node.val)
            if node.next is None:
                string += ']'
                break
            string += ', '
            node = node.next
        return string


class Solution:

    @staticmethod
    def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
        lista_ordenada = None

        return


lista_ordenada = Solution().mergeTwoLists()
print(lista_ordenada)
