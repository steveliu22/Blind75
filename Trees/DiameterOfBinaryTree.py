# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        elif(root.left == None and root.right == None):
            return 1
        else:
            max_left = self.max_depth(root.left)
            max_right = self.max_depth(root.right)
            return max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right), max_left + max_right)
        
    
    def max_depth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        elif root.left == None and root.right == None:
            return 1
        
        else:
            return 1 + max(self.max_depth(root.left), self.max_depth(root.right))