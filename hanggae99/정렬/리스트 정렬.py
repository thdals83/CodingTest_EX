# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: [ListNode]) -> [ListNode]:
        node = head
        arr = []

        while node:
            arr.append(node.val)
            node = node.next

        arr.sort()

        node = head
        for n in arr:
            node.val = n
            node = node.next

        return head

