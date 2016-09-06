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
        for i in range(0, self.size-1):
            self.data[i] = self.data[i+1]
        self.data[-1] = val
        
        asize = sum(1 for i in self.data if i !=None)

        return sum(i for i in self.data if i!=None)/float(asize)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
