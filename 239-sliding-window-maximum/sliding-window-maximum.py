from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==0 or k==0:
            return [] 

        n= len(nums)
        ans=[0]*(n-k+1)
        que= deque()

        for i in range(n):
            while len(que) > 0 and que[0] < i-k+1:
                que.popleft()

            while len(que) > 0 and nums[que[-1]] < nums[i]:
                que.pop()
            
            que.append(i)

            if i >= k-1:
                ans[i-k+1]= nums[que[0]]
        return ans


