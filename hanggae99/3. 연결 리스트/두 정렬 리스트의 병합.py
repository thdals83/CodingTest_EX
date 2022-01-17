from typing import List
from collections import deque


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = None


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if (not l1) or (l2 and l1.val > l2.val):
        l1,l2 = l2,l1

    if l1:
        l1.next = mergeTwoLists(l1.next,l2)

    return l1


if __name__ == "__main__":
    list1 = ListNode(1)
    list2 = ListNode(2)
    list3 = ListNode(3)
    head1 = list1
    list1.next = list2
    list2.next = list3

    list4 = ListNode(1)
    list5 = ListNode(3)
    list6 = ListNode(4)
    head2 = list4
    list4.next = list5
    list5.next = list6

    head = mergeTwoLists(head1,head2)

    while head:
        print(head.val,end="")
        if head.next:
            print("->",end="")
        head = head.next
