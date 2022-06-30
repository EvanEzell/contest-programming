// https://leetcode.com/problems/find-median-from-data-stream

# heapq only implements min heap
# for maxHeap, need to invert values as they are pushed and popped

# need to maintain following properties
#  - len(smallValues) same or one less than len(largeValues)
#  - all smallValues <= all largeValues

class MedianFinder:

    def __init__(self):
        self.smallValues = [] # maxHeap
        self.largeValues = [] # minHeap
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallValues, -1 * num)
        
        if self.largeValues and -1 * self.smallValues[0] > self.largeValues[0]:
            value = -1 * heapq.heappop(self.smallValues)
            heapq.heappush(self.largeValues, value)
        
        if len(self.smallValues) - 1 > len(self.largeValues):
            value = -1 * heapq.heappop(self.smallValues)
            heapq.heappush(self.largeValues, value)            
        if len(self.largeValues) > len(self.smallValues):
            value = heapq.heappop(self.largeValues)
            heapq.heappush(self.smallValues, -1 * value)
        
    def findMedian(self) -> float:
        if (len(self.smallValues) + len(self.largeValues)) % 2 == 0:
            return (-1 * self.smallValues[0] + self.largeValues[0]) / 2
        else: # odd number of values
            return -1 * self.smallValues[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()