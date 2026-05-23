# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, smallVal, bigVal):
            if not root:
                return True
            if root.val <= smallVal or root.val >= bigVal:
                return False
            
            left = dfs(root.left, smallVal, root.val)
            right = dfs(root.right, root.val,bigVal)

            return (left and right)

        return dfs(root, float("-inf"), float("inf"))
            



        

                
            