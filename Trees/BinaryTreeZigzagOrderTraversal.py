
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root == None:
            return None
        else:
            queue = [root]
            ans = []
            direction = False
            while len(queue) > 0:
                direction = not direction
                part_ans = deque([])
                for i in range(len(queue)):
                    node = queue.pop(0)

                    if direction:
                        part_ans.append(node.val)
                    else:
                        part_ans.appendleft(node.val)

                    if node.left != None:
                        queue.append(node.left)
                    
                    if node.right != None:
                        queue.append(node.right)
                
                ans.append(part_ans)
            
            return ans

        