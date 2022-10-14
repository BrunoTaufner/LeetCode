class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
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
        if list1 is None:
            list1 = list2
        elif list2 is not None:
            node = list1
            while True:
                if node.next is None:
                    node.next = list2
                    break
                node = node.next

        node = list1
        if node is None:
            return list1
        while True:
            if node.next is not None:
                if node.val > node.next.val:
                    temp = node.val
                    node.val = node.next.val
                    node.next.val = temp
                    node = list1
                else:
                    node = node.next
            else:
                break

        return list1


def criaLista(lista):
    ant = None
    initial_node = None
    for num in lista:
        node_list = ListNode(num)
        if initial_node is None:
            initial_node = node_list
        if ant is not None:
            ant.next = node_list
        ant = node_list

    return initial_node


lista_ordenada = Solution().mergeTwoLists(criaLista([1, 2, 3]), criaLista([]))
print(lista_ordenada)
