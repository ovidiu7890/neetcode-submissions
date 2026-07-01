# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ok = True
    def helper(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        if p != None and q != None:
            if p.val == q.val:
                self.isSameTree(p.left, q.left)
                self.isSameTree(p.right, q.right)
            else:
                self.ok = False
        else:
            if p == None:
                if q != None:
                    self.ok = False
            else:
                if q == None:
                    self.ok = False
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.helper(p, q)
        return self.ok


        
        