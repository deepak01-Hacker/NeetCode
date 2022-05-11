# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    
    def getSame(self,root,subRoot):
        if subRoot is None and root is None:
            return True
        if subRoot is None or root is None or root.val != subRoot.val:
            return False
        return self.getSame(root.left,subRoot.left) and self.getSame(root.right,subRoot.right)
        
    
    def isSubtreehelp(self,root, subRoot):
        if root is None:
            return False
        
        if self.getSame(root,subRoot):
            return True
        
        return self.isSubtreehelp(root.left, subRoot) or self.isSubtreehelp(root.right, subRoot)
       
        
    
    
    def isSubtree(self, root, subRoot):
        if subRoot is None:
            return True
        return self.isSubtreehelp(root, subRoot)
        
        
        
