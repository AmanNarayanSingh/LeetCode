# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def arr(self,lst,root):
        if root != None:
            self.arr(lst,root.left)
            lst.append(root.val)
            self.arr(lst,root.right)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst=[]
        self.arr(lst,root)
        return lst