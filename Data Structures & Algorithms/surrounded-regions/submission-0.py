class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        zero = set()
        num = 0

        def dfs(matrix, r, c, visited):
            ROWS, COLS = len(matrix), len(matrix[0])
            if r not in range(ROWS) or c not in range(COLS):
                return True
            if matrix[r][c] == 'X':
                return False
            if ((r,c)) in visited:
                return False
            
            visited.add((r,c))
            
            offSet = [(0,1),(0,-1),(1,0),(-1,0)]
            res = False
            for rOf, cOf in offSet:
                rOf, cOf = r + rOf, c + cOf
                res = dfs(matrix, rOf, cOf, visited) or res
            return res

        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    if not dfs(board, r, c, set()):
                        board[r][c] = 'X'