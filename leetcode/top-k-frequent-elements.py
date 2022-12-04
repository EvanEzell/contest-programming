// https://leetcode.com/problems/top-k-frequent-elements

from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)
    
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        freqs = []
        for num, freq in count.items():
            freqs.append(PrioritizedItem(freq, num))
        
        minheap = []
        for i in range(k):
            heapq.heappush(minheap, freqs[i])
        
        for i in range(k,len(freqs)):
            heapq.heappushpop(minheap, freqs[i])
        
        return map(lambda x: x.item, minheap)