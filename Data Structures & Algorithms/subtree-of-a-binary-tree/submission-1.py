# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2 or root1.val != root2.val:
                return False
            l = dfs(root1.left, root2.left)
            r = dfs(root1.right, root2.right)

            return (l and r)

        if not root:
            return False
        ans = dfs(root, subRoot)
        if ans:
            return True
        r = self.isSubtree(root.right, subRoot)
        l = self.isSubtree(root.left, subRoot)

        return r or l


        
        