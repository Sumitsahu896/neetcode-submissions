# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         result = [0] * len(temperatures)
#         stack = [] # pair: [temp, index]

#         for i, t in enumerate(temperatures):
#             while stack and t > stack[-1][0]:
#                 stackT, stackInd = stack.pop()
#                 result[stackInd] = i - stackInd
#             stack.append([t, i])
#         return result

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                result[prev_day] = i - prev_day
            stack.append(i)

        return result        