class Solution:
    def isValidSudoku(self, board) -> bool:
        # Check rows, columns, and 3x3 sub-boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue

                # Check row
                if num in rows[i]:
                    return False
                rows[i].add(num)

                # Check column
                if num in cols[j]:
                    return False
                cols[j].add(num)

                # Check 3x3 box
                box_index = (i // 3) * 3 + (j // 3)
                if num in boxes[box_index]:
                    return False
                boxes[box_index].add(num)

        return True


sol = Solution()
board = [
    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", ".", "3"],
    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

print(sol.isValidSudoku(board))
