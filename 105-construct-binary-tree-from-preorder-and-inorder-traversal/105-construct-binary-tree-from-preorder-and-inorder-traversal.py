# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(preorder,inorder):
            if inorder:
                root=TreeNode(preorder.pop(0))
                idx=inorder.index(root.val)
                root.left=helper(preorder,inorder[:idx])
                root.right=helper(preorder,inorder[idx+1:])
                return root
        return helper(preorder,inorder)
            