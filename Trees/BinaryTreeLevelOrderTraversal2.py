from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root == None:
            return None
        else:
            
            ans = deque([])
            queue = [root]
            
            while len(queue) != 0:
                part_ans = []

                for i in range(len(queue)):
                    node = queue.pop(0)
                    part_ans.append(node.val)

                    if node.left != None:
                        queue.append(node.left)
                    
                    if node.right != None:
                        queue.append(node.right)
                ans.appendleft(part_ans)

            return list(ans)