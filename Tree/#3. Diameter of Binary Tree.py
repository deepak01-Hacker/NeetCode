# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def diameterOfBinary(self,root,ans):
        if root is None:
                return 0

        l = self.diameterOfBinary(root.left,ans)
        r = self.diameterOfBinary(root.right,ans)
        ans[0] = max(ans[0],l+r)

        if l > r:
            return l+1
        return r+1
        
    def diameterOfBinaryTree(self, root):
        ans = [0]
        self.diameterOfBinary(root,ans)
        return ans[0]
        
