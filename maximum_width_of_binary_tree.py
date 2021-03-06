# python3
# Given a binary tree, write a function to get the maximum width of the given tree.
# The width of a tree is the maximum width among all levels.
# The binary tree has the same structure as a full binary tree, but some nodes are null.

# The width of one level is defined as the length between the end-nodes
# (the leftmost and right most non-null nodes in the level,
# where the null nodes between the end-nodes are also counted into the length calculation.

# Example 1:
# Input:

#            1
#          /   \
#         3     2
#        / \     \
#       5   3     9

# Output: 4
# Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
# Example 2:
# Input:

#           1
#          /
#         3
#        / \
#       5   3

# Output: 2
# Explanation: The maximum width existing in the third level with the length 2 (5,3).
# Example 3:
# Input:

#           1
#          / \
#         3   2
#        /
#       5

# Output: 2
# Explanation: The maximum width existing in the second level with the length 2 (3,2).
# Example 4:
# Input:

#           1
#          / \
#         3   2
#        /     \
#       5       9
#      /         \
#     6           7
# Output: 8
# Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


# My solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        out = 0
        level_pos = []

        def search(node, level, pos):
            if node is None:
                return
            if len(level_pos) <= level:
                level_pos.append([2 ** (level + 1) - 2, 2 ** level - 1])
            level_pos[level][0] = min(level_pos[level][0], pos)
            level_pos[level][1] = max(level_pos[level][1], pos)
            search(node.left, level + 1, 2 * pos + 1)
            search(node.right, level + 1, 2 * pos + 2)

        search(root, 0, 0)
        out = 0
        for it in level_pos:
            out = max(out, it[1] - it[0] + 1)

        return out

