from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        ROW, COL = len(grid), len(grid[0])
        
        maxG = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
                maxG = max(maxG, grid[r][c])
        
        if maxG == 0:
            return 0
        


        time = -1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2


                offSet = [(0,1),(0,-1),(1,0),(-1,0)]
                for rOf, cOf in offSet:
                    rOf, cOf = r + rOf, c + cOf
                    if rOf not in range(ROW) or cOf not in range(COL) or (rOf, cOf) in visited or grid[rOf][cOf] != 1:
                        continue
                    q.append((rOf, cOf))
                    visited.add((rOf, cOf))
            time += 1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1


        return time
            
            

        

        