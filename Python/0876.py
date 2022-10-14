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


def criarLista(array: list) -> ListNode:
    ant = None
    head = None
    for num in array:
        node_list = ListNode(num)
        if head is None:
            head = node_list
        if ant is not None:
            ant.next = node_list
        ant = node_list
    return head


class Solution:
    @staticmethod
    def middleNode(head: ListNode) -> ListNode:
        node = head
        lista = []
        while 1:
            lista.append(node.val)
            if node.next is None:
                break
            node = node.next

        i = int(len(lista) / 2)
        ant = None
        head = None
        while i < len(lista):
            node_list = ListNode(lista[i])
            if head is None:
                head = node_list
            if ant is not None:
                ant.next = node_list
            ant = node_list
            i += 1

        return head


print(Solution().middleNode(criarLista([1,2,3,4,5])))
