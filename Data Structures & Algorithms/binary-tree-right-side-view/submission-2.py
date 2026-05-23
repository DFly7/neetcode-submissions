# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        que = deque()
        res = []
        if root:
            que.append(root)

        while que:
            res.append(que[0].val)

            for i in range(len(que)):
                cur = que.popleft()
                if cur.right:
                    que.append(cur.right)
                if cur.left:
                    que.append(cur.left)
            
        return res

        