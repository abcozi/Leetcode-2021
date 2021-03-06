# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = [root]
        tmp = []
        level = 0
        sum = {}
        count = {}
        sum[level] = 0
        count[level] = 0
        while len(queue) > 0 or len(tmp) > 0:
            # pop root
            root = queue.pop(0)
            # get values
            if root != None:
                sum[level] += root.val
                count[level] += 1
            
            # put children
            if root.left != None:
                tmp.append(root.left)
            if root.right != None:
                tmp.append(root.right)
                
            if len(queue) == 0:
                queue = tmp
                tmp = []
                level += 1
                count[level] = 0
                sum[level] = 0

        return [sum[l]/count[l] for l in range(level)]