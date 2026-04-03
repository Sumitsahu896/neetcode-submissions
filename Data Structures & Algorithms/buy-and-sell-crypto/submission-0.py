class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minPrice = float("inf")
        for price in prices:
            if price < minPrice:
                minPrice = price
            elif price - minPrice > profit:
                profit =  price - minPrice

        return profit