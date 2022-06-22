
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if root == None:
            return []

        else:
            queue = [root]
            ans = []
            while len(queue) != 0:
                length = len(queue)
                for i in range(length):
                    node = queue.pop(0)
                    
                    if i == (length - 1):
                        ans.append(node.val)
                    
                    if node.left != None:
                        queue.append(node.left)
                    
                    if node.right != None:
                        queue.append(node.right)

            return ans
        