# flip game

You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

For example, given s = "++++", after one move, it may become one of the following states:

[
  "--++",
  "+--+",
  "++--"
]

#### solution

```python
class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        window_size = 2
        ss = list(s)
   
        for i in range(0, len(s)-window_size+1):
            if ''.join(s[i:i+window_size]) == '++':
                res.append(s[:i]+'--'+s[i+window_size:])
        return res
  ```
  
  #### notes
  tag: str, list, for loop, index range
