from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        def bfs(r, c):
            ROWS = len(grid)
            COLS = len(grid[0])

            visited = set()
            que = deque()
            que.append((r,c))
            visited.add((r,c))

            level = 0
            while que:
                for i in range(len(que)):
                    r, c = que.popleft()
                    if grid[r][c] > level:
                        grid[r][c] = level

                    offSet = [(1,0),(-1,0),(0,1),(0,-1)]
                    for rOf, cOf in offSet:
                        newR, newC = r + rOf, c + cOf
                        if newR not in range(ROWS) or newC not in range(COLS) or (newR, newC) in visited or grid[newR][newC] == -1:
                            continue
                        # grid[newR][newC] = 12

                        visited.add((newR,newC))
                        que.append((newR,newC))
                level += 1
    
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    bfs(r, c)
                

            