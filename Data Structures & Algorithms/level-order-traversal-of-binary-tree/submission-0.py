# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        array = []
        def helper(root: Optional[TreeNode], i:int):
            if root != None:
                if len(array)<i+1:
                    array.append([root.val])
                else:
                    array[i].append(root.val)
                helper(root.left, i+1)
                helper(root.right, i+1)
        helper(root, 0)
        return array
            

