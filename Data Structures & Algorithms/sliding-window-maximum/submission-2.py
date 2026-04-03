class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # heap = [] # Create a heap
        # output = [] # Create a output array where we will throw the output values
        # for i in range(len(nums)): # Run the for loop from 0 to last element
        #     heapq.heappush(heap, (-nums[i], i)) # Keep pushing the elements in the heap. We will create a maxHeap with nums and their index
        #     if i >= k - 1:
        #         while heap[0][1] <= i - k:
        #             heapq.heappop(heap)
        #         output.append(-heap[0][0])
        # return output

        output = []
        q = deque()
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output