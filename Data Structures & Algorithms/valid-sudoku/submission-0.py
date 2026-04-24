class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            check = set()
            for j in range(9):
                if board[i][j] in check:
                    return False
                elif board[i][j] != ".":
                    check.add(board[i][j])
        
        for i in range(9):
            check = set()
            for j in range(9):
                if board[j][i] in check:
                    return False
                elif board[j][i] != ".":
                    check.add(board[j][i])
        
        for i in range(3):
            for j in range(3):
                check = set()
                for k in range(3):
                    for l in range(3):
                        if board[3*i+k][3*j+l] in check:
                            return False
                        elif board[3*i+k][3*j+l] != ".":
                            check.add(board[3*i+k][3*j+l])

        return True
        