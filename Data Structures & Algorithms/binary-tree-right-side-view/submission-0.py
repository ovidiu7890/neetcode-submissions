class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def dfs(node: Optional[TreeNode], depth: int):
            if not node:
                return
            
            # If the current depth equals the length of our result list,
            # it means this is the first time we are visiting this depth.
            if depth == len(result):
                result.append(node.val)
            
            # Visit the right side FIRST. This ensures the rightmost
            # nodes are added to the result before any left nodes.
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
            
        dfs(root, 0)
        return result