# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head

        t = head
        l = 1

        while t.next != None:
            l += 1
            t = t.next

        k = k % l

        if k == 0:
            return head

        s, p, q = None, head, head

        for i in range(k - 1):
            q = q.next

        while q.next != None:
            s = p
            q = q.next
            p = p.next

        s.next = None
        q.next = head

        return p

solution = Solution()
head = ListNode(1)

print(solution.rotateRight(head,1))


# 1->2->3->4->5->NULL, k = 2
# 0->1->2->NULL, k = 4
# [1,2,3]
# 2000000000