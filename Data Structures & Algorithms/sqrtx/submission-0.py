class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0 , x
        result = 0

        while left <= right:
            m = (left + right) // 2
            if m * m > x:
                right = m - 1
            elif m * m < x:
                left = m + 1
                result = m
            else:
                return m

        return result