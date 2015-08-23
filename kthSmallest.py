# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def tree_deep(root):
            if root is None:
                return 0
            return 1 + tree_deep(root.left)+tree_deep(root.right)
        if root is None:
            return 0
        left_deep = tree_deep(root.left)
        if k == left_deep + 1:
            return root.val
        elif left_deep >= k:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k-left_deep-1)
