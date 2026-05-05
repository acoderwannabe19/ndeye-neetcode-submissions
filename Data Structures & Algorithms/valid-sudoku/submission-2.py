class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Check rows
        for i in range(9):
            nums = [x for x in board[i] if x != "."]
            if len(nums) != len(set(nums)):
                return False
        
        # Check columns
        for j in range(9):
            column = [board[i][j] for i in range(9) if board[i][j] != "."]
            if len(column) != len(set(column)):
                return False
        
        # Check 3x3 boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = []
                for i in range(3):
                    for j in range(3):
                        val = board[box_row + i][box_col + j]
                        if val != ".":
                            box.append(val)
                if len(box) != len(set(box)):
                    return False
        
        return True