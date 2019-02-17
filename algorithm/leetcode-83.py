class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        p, q = head, head
        while q.next is not None:
            q = q.next
            if q.val != p.val:
                p.next = q
                p = q

        return head