class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def percorreLista(l: ListNode) -> int:
    numero = []
    while True:
        numero.insert(0, l.val)
        if l.next is None:
            return int(''.join(map(str, numero)))
        l = l.next


def inverteLista(l: list) -> ListNode:
    l_aux = None
    ant = None
    for num in l:
        l_aux = ListNode(num)
        l_aux.next = ant
        ant = l_aux
    return l_aux


class Solution:
    @staticmethod
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        numero1 = percorreLista(l1)
        numero2 = percorreLista(l2)
        soma = numero1 + numero2
        soma = list(map(int, str(soma)))
        return inverteLista(soma)



l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

Solution().addTwoNumbers(l1, l2)
