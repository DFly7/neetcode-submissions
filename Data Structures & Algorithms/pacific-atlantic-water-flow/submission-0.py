class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.atlantic = set()
        self.pacific = set()

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                self.pacific.add((0,c))
                self.atlantic.add((len(heights)-1,c))
            self.pacific.add((r,0))
            self.atlantic.add((r,len(heights[0])-1))


        def dfs(matrix, r, c, visited, prev):
            ROWS, COLS = len(matrix), len(matrix[0])
            if r not in range(ROWS) or c not in range(COLS) or matrix[r][c] > prev or (r,c) in visited:
                return False
            visited.add((r,c))
            intersect = self.atlantic.intersection(visited)
            intersetct2 = self.pacific.intersection(visited)
            # if visited has both an atlantic and a pacific corords
            if intersect and intersetct2:
                return True
            offSet = [(0,1),(0,-1),(1,0),(-1,0)]
            res = False
            for rOf, cOf in offSet:
                rOf, cOf = r + rOf, c + cOf
                result = dfs(matrix, rOf, cOf, visited, matrix[r][c])
                res = res or result
            return res

        res = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if dfs(heights,r,c,set(),float("inf")):
                    res.append([r,c])
        
        return res