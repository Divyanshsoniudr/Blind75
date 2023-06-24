from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        top_k = heapq.nlargest(k, counter, key=counter.get)

        return top_k
