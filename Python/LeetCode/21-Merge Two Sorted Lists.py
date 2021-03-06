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
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            node = ListNode(l1.val)
            node.next = self.mergeTwoLists(l1.next, l2)
        else:
            node = ListNode(l2.val)
            node.next = self.mergeTwoLists(l1, l2.next)
        return node
