from typing import List
from collections import deque


class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = None


# 책 풀이코드(재귀 방법을 이용)
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    # li = [], l2 = [] ==> []
    # li = [], l2 = [0] ==> [0]

    if (not l1) or (l2 and l1.val > l2.val):
        l1,l2 = l2,l1

    if l1:
        l1.next = mergeTwoLists(l1.next,l2)

    return l1


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    res = ListNode()
    tail = res

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    return res.next


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
