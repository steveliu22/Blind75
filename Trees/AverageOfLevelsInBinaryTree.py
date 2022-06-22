from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> list[float]:
        if root == None:
            return []
        else:
            queue = [root]
            ans = []

            while len(queue) > 0:
                length = len(queue)
                sum = 0
                for i in range(length):
                    node = queue.pop(0)
                    sum += float(node.val)

                    if node.left != None:
                        queue.append(node.left)
                    
                    if node.right != None:
                        queue.append(node.right)
                
                ans.append(sum / float(length))
        
        return ans