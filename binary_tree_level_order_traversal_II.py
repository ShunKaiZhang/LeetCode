# python3
# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]


# My solution, think again, you spend a lot time on it
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        def search(root, level):
            if root is None:
                return
            if len(out) < level + 1:
                out.insert(0, [])
            out[-(level + 1)].append(root.val)
            search(root.left, level + 1)
            search(root.right, level + 1)

        out = []
        search(root, 0)
        return out