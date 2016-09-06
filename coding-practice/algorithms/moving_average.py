class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.data = [None]*size
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        for i in range(self.size-1, -1, -1):
            self.data[i-1] = self.data[i]
        self.data[-1] = val
        
        asize = sum(1 for i in self.data if i !=None)
        
        return sum(i for i in self.data if i!=None)/float(asize)
        

# for optimization:
#  1) asize can be a counter and after stack is full we can simply use self.size

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
