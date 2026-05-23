# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pQue = deque()
        qQue = deque()

        if p == None and q == None:
            return True
        if not (p and q):
            return False

    

        pQue.append(p)
        qQue.append(q)

        while pQue:
            for i in range(len(pQue)):
                Pcur = pQue.popleft()
                Qcur = qQue.popleft()

                if Pcur.val != Qcur.val:
                    return False

                if (Pcur.left and Qcur.left) or (Pcur.left == None and Qcur.left == None):
                    if Pcur.left:
                        pQue.append(Pcur.left)
                        qQue.append(Qcur.left)
                else:
                    return False
                    

                if (Pcur.right and Qcur.right) or (Pcur.right == None and Qcur.right == None):
                    if Pcur.right:
                        pQue.append(Pcur.right)
                        qQue.append(Qcur.right)
                else:
                    return False
        return True







            