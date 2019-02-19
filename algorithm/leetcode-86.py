# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        val_node, fix_node, q = None, None, head
        if head.val < x:
            val_node = head
        else:
            fix_node = head

        while q.next is not None:
            q = q.next
            if q.val < x:
                if not val_node:
                    fix_node.next = q.next
                    q.next = head
                    head = q
                    val_node = q
                    q = fix_node
                else:
                    if fix_node is not None:
                        fix_node.next = q.next
                        q.next = val_node.next
                        val_node.next = q
                        val_node = q
                        q = fix_node
                    else:
                        val_node.next = q
                        val_node = q
            else:
                fix_node = q

        return head


