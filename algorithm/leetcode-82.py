# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        new_head = None
        s, p, q = None, None, head
        # 单个元素的情况
        if head.next is None or head.val != head.next.val:
            new_head = head
            s = head

        while q.next is not None:
            p = q
            q = q.next
            if q.val == p.val:
                continue
            if q.next is not None and q.val == q.next.val:
                continue
            if new_head is None:
                new_head = q
                s = q
            else:
                s.next = q
                s = q
        # 最后边界，要闭口
        if s is not None:
            s.next = None
        return new_head