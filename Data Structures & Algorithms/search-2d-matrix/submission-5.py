class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix)-1, len(matrix[0])-1

        low, high = 0, ROWS

        while low<=high:
            mid = (high+low)//2

            if target < matrix[mid][0]:
                high = mid - 1
            elif target > matrix[mid][-1]:
                low = mid + 1
            else:
                break

        if mid not in range(ROWS+1):
            return False

        RF = mid

        low, high = 0, len(matrix[RF]) - 1
        while low<=high:
            mid = (low+high)//2

            if target < matrix[RF][mid]:
                high = mid - 1
            elif target > matrix[RF][mid]:
                low = mid + 1
            else:
                return True
        
        return False




        
