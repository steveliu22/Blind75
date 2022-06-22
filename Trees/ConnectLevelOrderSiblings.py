
# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if root == None:
            return None
        else:
            queue = [root]

            while len(queue) != 0:
                queue_length = len(queue)
                for i in range(queue_length):
                    node = queue.pop(0)

                    if i == (queue_length - 1):
                        node.next = None
                    else:
                        node.next = queue[0]

                    if node.left != None:
                        queue.append(node.left)
                        
                    if node.right != None:
                        queue.append(node.right)
        
        return root

            