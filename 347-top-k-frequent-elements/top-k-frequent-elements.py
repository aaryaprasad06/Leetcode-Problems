import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for i in nums:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        heap=[]
        for key, value in hashmap.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
            else:
                if value > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (value, key))
        ans=[]
        while heap:
            freq, num= heapq.heappop(heap)
            ans.append(num)
        return ans

        