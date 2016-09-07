# Valid Anagram
## LeetCode OJ

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

#### solution

```python
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        dict_s = {}
        dict_t = {}
        
        s = list(s)
        t = list(t)
        
        for s_ in s:
            if s_ in dict_s:
                dict_s[s_] += 1
            else:
                dict_s[s_] = 1
        for t_ in t:
            if t_ in dict_t:
                dict_t[t_] += 1
            else:
                dict_t[t_] = 1
                
        for k in dict_s:
            if k not in dict_t or dict_s[k] != dict_t[k]:
                return False
        for k in dict_t:
            if k not in dict_s or dict_t[k] != dict_s[k]:
                return False
        
        return True
        
```

#### notes

dict is used a lot. is that okay?
