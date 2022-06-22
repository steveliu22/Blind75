from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.sumNumbersHelp(root, 0)
        
    def sumNumbersHelp(self, root: Optional[TreeNode], accumulated_sum: int) -> int:
        if root == None:
            return 0
        elif (root.left == None and root.right == None):
            return root.val + (accumulated_sum * 10)
        
        else:
            total_sum = root.val + (accumulated_sum * 10)
            return self.sumNumbersHelp(root.left, total_sum) + self.sumNumbersHelp(root.right, total_sum)