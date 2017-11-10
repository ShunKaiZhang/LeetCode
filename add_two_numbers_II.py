# python3
# You are given two non-empty linked lists representing two non-negative integers.
# The most significant digit comes first and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

# Example:

# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7


# My solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num_1 = ''
        num_2 = ''
        while l1:
            num_1 += str(l1.val)
            l1 = l1.next
        while l2:
            num_2 += str(l2.val)
            l2 = l2.next

        new_num = str(int(num_1) + int(num_2))
        node = ListNode(new_num[0])
        head = node
        for i in range(1, len(new_num)):
            node.next = ListNode(new_num[i])
            node = node.next
        return head


