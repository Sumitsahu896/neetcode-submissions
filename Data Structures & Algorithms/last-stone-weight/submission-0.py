class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Since python does not have a maxheap
        # we will multiply every element with negative value
        # and put it in a min heap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])