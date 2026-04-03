"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(mid, row, col):
            allSame = True
            for i in range(mid):
                for j in range(mid):
                    if grid[row][col] != grid[row + i][col + j]:
                        allSame = False
                        break
                
            if allSame:
                return Node(grid[row][col], True)

            mid = mid // 2
            topleft = dfs(mid, row, col)
            topright = dfs(mid, row, col + mid)
            bottomleft = dfs(mid, row + mid, col)
            bottomright = dfs(mid, row + mid, col + mid)

            return Node(0, False, topleft, topright, bottomleft, bottomright)

        return dfs(len(grid), 0, 0)
