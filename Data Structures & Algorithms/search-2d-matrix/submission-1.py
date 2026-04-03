class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows , cols = len(matrix) , len(matrix[0])

        top = 0
        bot = rows -1

        while top <= bot:
            centr = ( top + bot )//2
            if target < matrix[centr][0]:
                bot = centr - 1
            elif target > matrix[centr][0]:
                top = centr + 1
            else:
                break
        
        
        centr = ( top + bot )//2
        l , r = 0 , cols - 1
        while l<= r:
            mid = (l+r)//2
            if target > matrix[centr][mid]:
                l = mid+1
            elif target < matrix[centr][mid]:
                r = mid - 1
            else:
                return True
        
        return False

        