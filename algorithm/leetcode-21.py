# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pointer_l1 = l1
        pointer_l2 = l2
        newlist_head = ListNode(-1)
        tmp_pointer = newlist_head
        while pointer_l1 is not None and pointer_l2 is not None:
            if pointer_l1.val <= pointer_l2.val:
                new_point = ListNode(pointer_l1.val)
                tmp_pointer.next = new_point
                tmp_pointer = new_point
                pointer_l1 = pointer_l1.next
            else:
                new_point = ListNode(pointer_l2.val)
                tmp_pointer.next = new_point
                tmp_pointer = new_point
                pointer_l2 = pointer_l2.next
        if pointer_l1 is None and pointer_l2 is None:
            return None
        elif pointer_l1 is None:
            tmp_pointer.next = pointer_l2
            return newlist_head.next
        else:
            tmp_pointer.next = pointer_l1
            return newlist_head.next
