from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dupDict = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                print(f'{r}, {c}, {board[r][c]}')
                number = board[r][c]
                
                if number == '.':
                    continue

                # 3 by 3 grid
                gridRow = r // 3
                gridCol = c // 3
                grid = (gridRow, gridCol)

                if number in dupDict[grid]:
                    return False
                if number in dupDict[(r, 'r')]:
                    return False
                if number in dupDict[(c, 'c')]:
                    return False
                dupDict[grid].add(number)
                dupDict[(r, 'r')].add(number)
                dupDict[(c, 'c')].add(number)
        return True