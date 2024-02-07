def valid_solution(board):
    def is_valid_line(line):
        print("-------------")
        print(line)
        # Check if a line (row, column, or sub-grid) contains all digits from 1 to 9
        return set(line) == set(range(1, 10))

    # Check rows and columns
    for i in range(9):
        #print(board[i])

        #print([board[j][i] for j in range(9)])
        if not is_valid_line(board[i]) or not is_valid_line([board[j][i] for j in range(9)]):
            return False

    # Check sub-grids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sub_grid = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid_line(sub_grid):
                return False

    return True

# Example usage:
valid_board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

invalid_board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 0, 3, 4, 8],
    [1, 0, 0, 3, 4, 2, 5, 6, 0],
    [8, 5, 9, 7, 6, 1, 0, 2, 0],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 0, 1, 5, 3, 7, 2, 1, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 0, 0, 4, 8, 1, 1, 7, 9]
]

print(valid_solution(valid_board))    # Output: True
print(valid_solution(invalid_board))  # Output: False
