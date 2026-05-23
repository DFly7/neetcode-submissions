from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = set()
        self.outSet = set()
        def bsf(grid):
            ROW, COL = len(grid), len(grid[0])
            queue = deque()
            queue.append((0,0))

            self.visited.add((0,0))

            res = 0

            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()

                    if grid[r][c] == "1" and (r, c) not in self.outSet:
                        dfs(grid, r, c)
                        res += 1
                    
                    offSet = [(0,1),(0,-1),(1,0),(-1,0)]
                    for rOf, cOf in offSet:
                        newR, newC = r + rOf, c + cOf
                        if (min(newR, newC) < 0 or newR == ROW or newC == COL 
                            or (newR, newC) in self.visited):
                            continue


                        queue.append((newR,newC))

                        self.visited.add((newR,newC))

            return res

        def dfs(grid, r, c):
            ROW, COL = len(grid), len(grid[0])

            if (r == ROW or c == COL
                or min(r,c) < 0 or (r,c) in self.outSet or grid[r][c] == "0"):
                return
            self.outSet.add((r,c))
            
            dfs(grid, r-1, c)
            dfs(grid, r+1, c)
            dfs(grid, r, c+1)
            dfs(grid, r, c-1)

    
        return bsf(grid)




