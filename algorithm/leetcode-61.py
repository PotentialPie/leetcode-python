# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or head.next is None:
            return head
        if k == 0:
            return head
        left_step = k
        s, p, q = None, head, head
        total_len = 0
        while left_step - 1 > 0:
            if q.next is None:
                total_len = total_len + 1
                left_step = k%total_len + 1
                if left_step == 1:
                    break
                q = head
            else:
                q = q.next
                total_len = total_len + 1
            left_step -= 1
        while q.next is not None:
            s = p
            p = p.next
            q = q.next
        if s is None:
            return head
        s.next = q.next
        q.next = head
        return p

solution = Solution()
head = ListNode(1)

print(solution.rotateRight(head,1))


# 1->2->3->4->5->NULL, k = 2
# 0->1->2->NULL, k = 4
# [1,2,3]
# 2000000000