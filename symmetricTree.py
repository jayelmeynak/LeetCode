from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            node.left, node.right = node.right, node.left

        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

            return False

        left, right = root.left, root.right
        dfs(left)

        return isSameTree(left, right)


