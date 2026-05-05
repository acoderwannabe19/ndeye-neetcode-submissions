class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] in seen:
                    return False
                if board[row][i] == ".":
                    continue
                seen.add(board[row][i])
        
        # columns
        for column in range(9):
            seen = set()
            for cell in range(9):
                if board[cell][column] == ".":
                    continue
                if board[cell][column] in seen:
                    return False
                seen.add(board[cell][column])
                
        # 3x3 boxes
        for box in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (box // 3) * 3 + i
                    column = (box % 3)*3 + j
                    if board[row][column] == ".":
                        continue
                    if board[row][column] in seen:
                        return False
                    seen.add(board[row][column])
        
        return True
            