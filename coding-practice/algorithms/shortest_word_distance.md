# Shortest Word Distance

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

#### solution

```python
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        pos_1 = []
        pos_2 = []
        for i in range(0, len(words)):
            if words[i] == word1:
                pos_1.append(i)
            if words[i] == word2:
                pos_2.append(i)
        
        res = []
        for i in pos_1:
            for j in pos_2:
                res.append(abs(i - j))

        print res
        
        return min(res)
        
  ```
 
 
#### notes
Key is to know word1 and word2 both might be observed more than once so we need 2 arrays to store the positions.

