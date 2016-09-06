# Ransom Note
## LeetCode OJ

Given  an  arbitrary  ransom  note  string  and  another  string  containing  letters from  all  the  magazines,  write  a  function  that  will  return  true  if  the  ransom   note  can  be  constructed  from  the  magazines ;  otherwise,  it  will  return  false.   

Each  letter  in  the  magazine  string  can  only  be  used  once  in  your  ransom  note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

#### solution

```python
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        dic_ran = {}
        dic_mag = {}
        
        ran = list(ransomNote)
        mag = list(magazine)
        
        for r in ran:
            if r in dic_ran:
                dic_ran[r] += 1
            else:
                dic_ran[r] = 1
        for m in mag:
            if m in dic_mag:
                dic_mag[m] += 1
            else:
                dic_mag[m] = 1
        
        for k in dic_ran:
            if k not in dic_mag or dic_ran[k] > dic_mag[k]:
                return False
        
        return True
  
  ```
  
#### notes
  
KEY: dic is used a lot. Is this right? At least accpeted.
