# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        def helper(root,level):
            if root:
                if len(ans)<=level:
                    ans.append([root.val])
                else:
                    ans[level].append(root.val)
                helper(root.left,level+1)
                helper(root.right,level+1)
        helper(root,0)
        return ans