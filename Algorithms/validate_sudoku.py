class Solution:
    def isValidSudoku(self, board) -> bool:
        i, j, k = 0, 0, 0
        trnboard = [] * 9
        y = 0
        while y < 9:
            arr = []
            for x in range(9):
                arr.append(board[x][y])
            trnboard.append(arr)
            y += 1

        sqrboard = [] * 9
        arr = []
        count, m, n, s = 0, 0, 3, 0
        while count < 27:
            index = count % 9
            line = board[index]
            arr += line[m:n]
            if count % 3 == 2:
                sqrboard.append(arr)
                arr = []
                s += 1
            if count % 9 == 8:
                m += 3
                n += 3
            count += 1

        def row_check(row, i):
            row_arr =  [] * 9
            for digit in row:
                if digit.isdigit():
                    row_arr.append(int(digit))
            i += 1
            row_set = set(row_arr)
            if i < 9:
                return (len(row_set) == len(row_arr)) and row_check(board[i], i)
            return (len(row_set) == len(row_arr))

        def column_check(column, j):
            column_arr =[] * 9
            for digit in column:
                if digit.isdigit():
                    column_arr.append(int(digit))
            j += 1
            column_set = set(column_arr)
            if j < 9:
                return (len(column_set) == len(column_arr)) and column_check(trnboard[j], j)
            return (len(column_set) == len(column_arr))
                  
        def box_check(box, k):
            box_arr = [] * 9
            for digit in box:
                if digit.isdigit():
                    box_arr.append(int(digit))
            k += 1
            box_set = set(box_arr)
            if k < 9:
                return (len(box_set) == len(box_arr)) and box_check(sqrboard[k], k)
            return (len(box_set) == len(box_arr))

        if row_check(board[i], i) and column_check(trnboard[j], j) and box_check(sqrboard[k], k):
            return True

        return False


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
