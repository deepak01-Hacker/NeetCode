# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if root is None:
            return root
        newRoot = root
        stack = []
        
        stack.append(root)
        
        while(True):
            if stack == []:
                break
            levelLength = len(stack)
            
            while(levelLength):
                root = stack.pop(0)
                
                if root.left:
                    stack.append(root.left)
                if root.right:
                    stack.append(root.right)
                
                ll = root.left
                rr = root.right
                root.left,root.right = rr,ll
                
                levelLength -= 1
        return newRoot
                
        
