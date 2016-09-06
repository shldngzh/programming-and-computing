# LeetCode OJ, Nested List Weight Sum

```python

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        return self.ds(nestedList, 1)
        
    def ds(self, nestedList, depth):
        s = 0
        for ele in nestedList:
            if ele.isInteger():
                s += ele.getInteger() * depth
            else:
                s += self.ds(ele.getList(), depth+1)
        return s
        
# OR

class Solution(object):
    def depthSum(self, nestedList, depth=1):
        # by setting a default depth to avoid multiple functions
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        s = 0
        for e in nestedList:
            if e.isInteger():
                s += e.getInteger() * depth
            else:
                s += self.depthSum(e.getList(), depth+1)
                
        return s
        
        
```
