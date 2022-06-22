from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        if root == None:
            return []
        elif root.left == None and root.right == None:
            if root.val == targetSum:
                return [[root.val]]
            else:
                return []
        else:
            ans = []

            path_left = self.pathSum(root.left, targetSum - root.val)
            path_right = self.pathSum(root.right, targetSum - root.val)

            for path in path_left:
                dp = deque(path)
                dp.appendleft(root.val)
                ans.append(list(dp))
            
            for path in path_right:
                dp = deque(path)
                dp.appendleft(root.val)
                ans.append(list(dp))
        
            return ans
            
