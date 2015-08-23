# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        def func_iter(node, path):
            if node.left is None and node.right is None:
                path.append(str(node.val))
                r.append('->'.join(path))
                return
            if node.left is not None:
                _path = path[:]
                _path.append(str(node.val))
                func_iter(node.left, _path)
            if node.right is not None:
                _path = path[:]
                _path.append(str(node.val))
                func_iter(node.right, _path)
        if root is None:
            return []
        r = []
        func_iter(root, [])
        return r
        
