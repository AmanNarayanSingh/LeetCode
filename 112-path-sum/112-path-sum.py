# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        lst=[]
        if root is None:
            return False 
        def helper(root,val):
            if root.left is None and root.right is None:
                val+=root.val
                lst.append(val)
                return
            val+=root.val
            if root.left:
                helper(root.left,val)
            if root.right:
                helper(root.right,val)
        helper(root,0)
        if targetSum in lst:
            return True
        return False 