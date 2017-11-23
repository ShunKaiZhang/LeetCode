# python3
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

# An example is the root-to-leaf path 1->2->3 which represents the number 123.

# Find the total sum of all root-to-leaf numbers.

# For example,

#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.

# Return the sum = 12 + 13 = 25.


# My solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        out = []
        res = [[root, '']]
        while res:
            cur = res.pop(0)
            if cur[0] is None:
                continue
            str_cur = cur[1] + str(cur[0].val)
            if cur[0].left is None and cur[0].right is None:
                out.append(int(str_cur))
            res.append([cur[0].left, str_cur])
            res.append([cur[0].right, str_cur])

        return sum(out)



