def 스도쿠(board):
    rows = [[False] * 10 for _ in range(9)]
    cols = [[False] * 10 for _ in range(9)]
    boxes = [[False] * 10 for _ in range(9)]

    빈공간들 = []
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != 0:
                rows[i][num] = True
                cols[j][num] = True
                boxes[(i // 3) * 3 + (j // 3)][num] = True
            else:
                빈공간들.append((i, j))

    def 중복검사(row, col, num):
        return not rows[row][num] and not cols[col][num] and not boxes[(row // 3) * 3 + (col // 3)][num]

    def solve(empty_index=0):
        if empty_index == len(빈공간들):
            return True
        row, col = 빈공간들[empty_index]
        for num in range(1, 10):
            if 중복검사(row, col, num):
                board[row][col] = num
                rows[row][num] = cols[col][num] = boxes[(row // 3) * 3 + (col // 3)][num] = True
                
                if solve(empty_index + 1):
                    return True
                
                # Backtrack
                board[row][col] = 0
                rows[row][num] = cols[col][num] = boxes[(row // 3) * 3 + (col // 3)][num] = False
        return False

    if solve():
        return board
    else:
        return "No solution exists"

board = []
for i in range(9):
    row_input = input()
    row = [int(num) for num in row_input]
    board.append(row)

solved_board = 스도쿠(board)

for row in solved_board:
    print(''.join(str(num) for num in row))