#Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.

#### solution

```python
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if nums1 == None or nums2 == None:
            return None
        
        s1 = set(nums1)
        s2 = set(nums2)
        
        return list(s1.intersection(s2))
        # return list(set(nums1).intersection(set(nums2)))
  
  ```
  
  #### notes
  
  Key: seems very simple and easy in Python with set
