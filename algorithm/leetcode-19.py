# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        before_leap, leap, tail = None, head, head

        for tail_move in range(n):
            if tail.next != None:
                tail = tail.next
            elif tail_move == n - 1:
                return head.next
            elif tail_move < n - 1:
                return None

        while tail != None:
            tail = tail.next
            before_leap = leap
            leap = leap.next

        before_leap.next = leap.next

        return head
def listprint(head):
    while head is not None:
        print(str(head.val))
        head = head.next

solution = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
print(listprint(solution.removeNthFromEnd(head,1)))
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
print(listprint(solution.removeNthFromEnd(head,2)))
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
print(listprint(solution.removeNthFromEnd(head,3)))
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
print(listprint(solution.removeNthFromEnd(head,4)))
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
print(listprint(solution.removeNthFromEnd(head,5)))