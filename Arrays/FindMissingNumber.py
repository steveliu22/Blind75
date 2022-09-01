# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = 1
        if root == None:
            return False
        elif root.left == None and root.right == None:
            return False
        else:
            stack = deque([root.val])
            seen = 0
            while len(stack) != 0:
                node = stack.po 
            
                
                    
                
            
            