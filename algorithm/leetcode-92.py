# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        s,p,q = ListNode(-1),head,head
        s.next = head
        # 可以用空的节点作为形式头节点
        new_head = s
        for i in range(m-1):
            s = p
            p = p.next
        q = p

        for i in range(n-m):
            q = q.next
            p.next = q.next
            q.next = s.next
            s.next = q
            q = p
        # 因为原来的head有可能被替换，所以这样最保险
        return new_head.next