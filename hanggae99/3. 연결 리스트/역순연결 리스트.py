from typing import List
from collections import deque
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = None

# 파이썬 리스트를 연결 리스트로 변환
def to_linked_list(list1: List[int]) -> ListNode:
    head = ListNode(list1[0])
    tail = head
    e = 1
    while e < len(list1):
        tail.next = ListNode(list1[e])
        tail = tail.next
        e += 1
    return head

# Linked List 출력
def print_list(head: ListNode):
    while head:
        print(head.val, end="")
        if head.next:
            print("->", end="")
        head = head.next

# 재귀 사용 방법 https://ihp001.tistory.com/143
def reverseList(head: ListNode) -> ListNode:
    def reverse(node: ListNode, prev: ListNode = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        print(node.val)
        return reverse(next,node)

    return reverse(head)
'''
def reverseList(head: ListNode) -> ListNode:
    prev = None
    node =  head

    while node:
        next = node.next
        node.next = prev

        prev = node
        node = next

    return prev
'''
if __name__ == "__main__":
    list1 = [1,2,3,4,5]
    list2 = to_linked_list(list1)
    list3 = reverseList(list2)
    print_list(list3)
