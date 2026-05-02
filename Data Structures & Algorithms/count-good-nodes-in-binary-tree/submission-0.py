# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    

    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0
        def dfs(root, max_value):
            
            nonlocal good_nodes

            if not root:
                return 
            if root.val>=max_value:
                good_nodes +=1
            max_value = max(max_value , root.val)
            dfs(root.left , max_value)
            dfs(root.right,max_value)
            return 

        dfs(root , -101 )
        return good_nodes