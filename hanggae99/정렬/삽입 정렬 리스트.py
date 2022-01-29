# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # 초기값 변경
        cur = parent = ListNode(0)

        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            head, cur.next, head.next = head.next, head, cur.next

            if head and cur.val > head.val:
                cur = parent

        return parent.next
'''
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        print(head)
        sort = []
        while head:
            num = head.val
            head = head.next
                        
            if len(sort) == 0:
                sort.append(num)
            else:
                che = True
                for i in range(len(sort)):
                    if sort[i] > num:
                        sort.insert(i, num)
                        che = False
                        break
                if che:
                    sort.append(num)
        
        final = start = ListNode(None)
        for n in sort:
            tmp = ListNode(n)
            start.next = tmp
            start = start.next
                      
        return final.next
'''