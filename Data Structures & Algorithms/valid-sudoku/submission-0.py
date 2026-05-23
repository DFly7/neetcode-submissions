class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashRows = defaultdict(set)
        hashCols = defaultdict(set)
        hashSet = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if(board[r][c] in hashRows[r] or board[r][c] in hashCols[c] or board[r][c] in hashSet[((r // 3),(c // 3))]):
                    return False
                hashRows[r].add(board[r][c])
                hashCols[c].add(board[r][c])
                hashSet[((r // 3),(c // 3))].add(board[r][c])
        
        return True