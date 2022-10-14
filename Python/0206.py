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
    def reverseList(head: ListNode) -> ListNode:
        ant = None
        node = head
        if node is None:
            return head
        while True:
            temp = node.next
            head = node
            if node.next is None:
                node.next = ant
                break
            node.next = ant
            ant = node
            node = temp

        return head


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


print(Solution().reverseList(criarLista([])))
