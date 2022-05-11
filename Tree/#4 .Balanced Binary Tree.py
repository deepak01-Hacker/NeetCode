# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution(object):
    def util(self,root,ans):
        if root is None:
            return 0
        l = self.util(root.left,ans)
        r = self.util(root.right,ans)
        
        if max(l,r)-min(l,r) > 1:
            ans[0] = False
        if l > r:
            return l+1
        return r+1
        
    def isBalanced(self, root):
        ans = [True]
        self.util(root,ans)
        return ans[0]
        
