# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#coding=utf-8
class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ## 边界！边界！边界！咋就是不听话呢！！！！打自己记耳光
        if not head or head.next is None:
            return head

        return_head = head.next

        p = head
        q = head.next
        temp_node = ListNode(-1)
        temp_node.next = head

        while q is not None:
            p.next = q.next
            q.next = p
            temp_node.next = q

            temp_node = p
            if temp_node.next is None:
                break
            p = p.next
            q = p.next

        return return_head
