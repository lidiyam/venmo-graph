from heapq import heappush, heappop

class MedianFinder(object):

    def __init__(self):
        """
        initialize data structures here.
        """
        self.minheap = []   # top half
        self.maxheap = []   # bottom half
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        median = self.findMedian()
        if num >= median:
            # top half
            if len(self.minheap) == len(self.maxheap):   
                heappush(self.minheap, num)
            elif len(self.minheap) > len(self.maxheap):
                moved = heappop(self.minheap)
                heappush(self.maxheap, -moved)
                heappush(self.minheap, num)
            else:
                heappush(self.minheap, num)
        else:
            # bottom half
            if len(self.minheap) == len(self.maxheap):
                heappush(self.maxheap, -num)
            elif len(self.minheap) > len(self.maxheap):
                heappush(self.maxheap, -num)
            else:
                moved = heappop(self.maxheap)
                heappush(self.minheap, -moved)
                heappush(self.maxheap, -num)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.minheap) == len(self.maxheap) and len(self.minheap) == 0:
            return 0
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0]*1.0 + self.maxheap[0]*-1.0) / 2.0
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]*1.0
        else:
            return self.maxheap[0]*-1.0


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


