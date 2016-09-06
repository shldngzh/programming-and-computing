Invert a binary tree.

     4
   /   \
   
  2     7
  
 / \   / \
 
1   3 6   9

to

     4
     
   /   \
   
  7     2
  
 / \   / \
 
9   6 3   1


#### solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
            
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        return root
  ```
  
  #### notes
  
  KEY: tree is not complicated at all, just be wise
