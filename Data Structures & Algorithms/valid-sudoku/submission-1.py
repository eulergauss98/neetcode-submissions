
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            seen_row=set()
            for  c in range(9):
                if board[r][c]==".":
                    continue
                
                if board[r][c] in seen_row:
                    return False
                
                seen_row.add(board[r][c])
        

        for c in range(9):
            seen_col=set()
            for r in range(9):
                if board[r][c]==".":
                    continue
                
                if board[r][c] in seen_col:
                    return False 
                
                seen_col.add(board[r][c])
        
        for square in range(9):
                seen_square=set()
                for i in range(3):
                    for j in range(3):
                        row=(square//3)*3+i
                        col=(square%3)*3+j

                        if board[row][col]==".":
                            continue
                        if board[row][col] in seen_square:
                            return False
                        seen_square.add(board[row][col])


        return True