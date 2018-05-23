from heapq import *

class MedianFinder(object):

    def __init__(self):
        """
        initialize data structures here.
        """
        self.minheap = []   # top half
        self.maxheap = []   # bottom half
        self.median = 0
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if num >= self.median:
            # top half
            if len(self.minheap) == len(self.maxheap):   
                heappush(self.minheap, num)
                self.median = self.minheap[0] * 1.0
            elif len(self.minheap) > len(self.maxheap):
                moved = heappop(self.minheap)
                heappush(self.maxheap, moved*-1.0)
                heappush(self.minheap, num)
                self.median = (num + moved) / 2.0
            else:
                heappush(self.minheap, num)
                self.median = (self.minheap[0] + self.median) / 2.0
        else:
            # bottom half
            if len(self.minheap) == len(self.maxheap):
                heappush(self.maxheap, num*-1.0)
                self.median = self.maxheap[0] *-1.0
            elif len(self.minheap) > len(self.maxheap):
                heappush(self.maxheap, num*-1.0)
                self.median = (self.minheap[0] + self.median) / 2.0
            else:
                moved = heappop(self.maxheap)
                heappush(self.minheap, moved*-1.0)
                heappush(self.maxheap, num*-1.0)
                self.median = (self.minheap[0] + self.maxheap[0]*-1.0) / 2.0

    def findMedian(self):
        """
        :rtype: float
        """
        return self.median


if __name__ == '__main__':
    obj = MedianFinder()
    print obj.maxheap, obj.minheap
    obj.addNum(-1)
    print obj.maxheap, obj.minheap
    obj.addNum(-2)
    print obj.maxheap, obj.minheap
    print obj.findMedian()
    obj.addNum(-3)
    print obj.maxheap, obj.minheap
    print obj.findMedian()
    obj.addNum(-4)
    print obj.maxheap, obj.minheap
    print obj.findMedian()


