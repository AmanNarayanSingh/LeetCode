"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def traverse(self,root,lst):
        if root:
            lst.append(root.val)
            for i in root.children:
                self.traverse(i,lst)
        return lst
    def preorder(self, root: 'Node') -> List[int]:
        return self.traverse(root,[])