# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append((root , 0))
        result = defaultdict(list)
        while q:
            curr_root , level = q.popleft()
            if curr_root.left:
                q.append((curr_root.left, 1 + level))
            if curr_root.right:
                q.append((curr_root.right , 1 + level))

            result[level].append(curr_root.val)
        
        result_list  = [[ ] for i in range(max(result.keys())+1)]
   
        for k,v in result.items():
           
            result_list[k].extend(v)
        return result_list
            
        
        