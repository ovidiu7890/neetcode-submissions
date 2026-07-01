# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxi = 0
    def helper(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        else:
            l = self.helper(root.left)
            r = self.helper(root.right)
            diam = l + r
            #print(diam, l , r)
            if diam > self.maxi:
                self.maxi = diam
            l += 1
            r += 1
            if l>r:
                return l
            else:
                return r
        return 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.maxi
        
        