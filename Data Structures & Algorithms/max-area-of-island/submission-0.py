class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        self.visited = set()

        def dfs(grid, r, c):
            ROW, COL = len(grid), len(grid[0])
            if min(r, c) < 0 or r == ROW or c == COL or grid[r][c] == 0 or (r,c) in self.visited:
                return 0
            
            self.visited.add((r,c))
            offSet = [(0,-1),(0,1),(1,0),(-1,0)]
            for rOf, cOf in offSet:
                newR = r + rOf
                newC = c + cOf

                dfs(grid, newR, newC)
        res = 0
        temp = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                prev = len(self.visited)
                dfs(grid, r, c)
                temp = len(self.visited) - prev
                res = max(temp, res)
        return res
