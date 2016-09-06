Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.

The key is to determine if only one char is observed odd times and other chars are observed even times.

#### solution

```python
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        counter = {}
        for char in s:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
                
        odd_flag = 0
        for v, k in counter.items():
            if k%2 == 1:
                odd_flag += 1
                
        if odd_flag > 1:
            return False
        return True
        

```

tag: dict hash counting 
