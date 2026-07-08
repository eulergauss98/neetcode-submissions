class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize 9 empty sets for rows, columns, and 3x3 subgrids
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        
        # Single pass through the 9x9 board
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == '.':
                    continue
                
                # 1. Check Row
                if val in rows[r]:
                    return False
                rows[r].add(val)
                
                # 2. Check Column
                if val in cols[c]:
                    return False
                cols[c].add(val)
                
                # 3. Check 3x3 Subgrid
                # Math trick to map (r, c) to a 0-8 index for the 9 subgrids
                sq_idx = (r // 3) * 3 + (c // 3)
                if val in squares[sq_idx]:
                    return False
                squares[sq_idx].add(val)
                
        # If we pass all checks, it's a valid Sudoku
        return True