from typing import List
from collections import deque


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = None


'''
# deque() 사용방법
def isPalindrome(head: ListNode) -> bool:
    q = deque()

    if not head: return True
    node = head

    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True
'''


# 런너 기법 사용 방법

def isPalindrome(head: ListNode) -> bool:
    rev = None
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    if fast:
        slow = slow.next

    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev


if __name__ == "__main__":
    list1 = ListNode(1)
    list2 = ListNode(2)
    list3 = ListNode(2)
    list4 = ListNode(1)
    head = list1
    list1.next = list2
    list2.next = list3
    list3.next = list4

    print(isPalindrome(head))
