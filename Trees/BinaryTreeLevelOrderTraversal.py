from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root == None:
            return []
        else:
            ans = []
            queue = []
            queue.append(root)

            while len(queue) > 0:
                level = len(queue)
                part_ans = []
                for i in range(level):
                    node = queue.pop(0)
                    part_ans.append(node.val)
                    if node.left != None:
                        queue.append(node.left)
                
                    if node.right != None:
                        queue.append(node.right)
                ans.append(part_ans)


            return ans


