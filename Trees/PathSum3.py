# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self.pathSumAcc(root, targetSum, targetSum, 0)
    
    def pathSumAcc(self, root: Optional[TreeNode], targetSum: int, original_target_sum, count) -> int:
        if root == None:
            return 0
        elif (root.left == None and root.right == None):
            if root.val == targetSum:
                return count + 1
            else:
                return count

        else:
            if root.val > targetSum:
                return self.pathSumAcc(root.left, targetSum, original_target_sum, count) + self.pathSumAcc(root.right, targetSum, original_target_sum, count)
            elif root.val == targetSum:
                return count + 1
            else:
                return self.pathSumAcc(root.left, targetSum - root.val, original_target_sum, count) + self.pathSumAcc(root.right, targetSum - root.val, original_target_sum, count) 
                
            