class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(shipCapacity):
            day = 1
            capacity = 0
            for w in weights:
                capacity += w
                if capacity > shipCapacity:
                    capacity = w  # Start new day with current package
                    day += 1
                    if day > days:  # Early termination optimization
                        return False
            return True
        
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid  # Try smaller capacity
            else:
                left = mid + 1  # Need larger capacity
        return left

# class Solution:
#     def shipWithinDays(self, weights: List[int], days: int) -> int:
#         left, right = max(weights), sum(weights)
#         res = right

#         def canShip(cap):
#             ships = 1
#             currCap = cap
#             for w in weights:
#                 if currCap - w < 0:
#                     ships += 1
#                     currCap = cap
#                 currCap -= w
#             return ships <= days

#         while left <= right:
#             mid = (left + right) // 2
#             if canShip(mid):
#                 res = min(res, mid)
#                 right = mid - 1
#             else:
#                 left = mid + 1

#         return res
