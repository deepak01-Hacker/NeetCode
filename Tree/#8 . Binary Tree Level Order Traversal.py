class Solution(object):
    def levelOrder(self, root):
        
        if root is None:
            return []
    
        res = []
        
        queue = [root]
    
        
        
        while(True):
            
            if queue :
                
                lengthOfrow = len(queue)
                res.append([])
                
                while(lengthOfrow>0):
                    
                    root = queue.pop(0)
                    res[-1].append(root.val)
                    
                    if root.left:
                        queue.append(root.left)
                        
                    if root.right:
                        queue.append(root.right)
                    
                    lengthOfrow -= 1
            else:
                break
        return res
