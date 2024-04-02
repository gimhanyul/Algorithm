def 입력함수():
    board = []
    for _ in range(5): #5X5보드 판
        row = list(map(int, input().split()))
        board.append(row)
    r, c = map(int, input().split())  #학생의 현재 위치 입력
    return board, r, c

board, r, c = 입력함수()
bool =False

def dfs(r ,c ,move, apple) :
    global bool

    apple = apple
    if r >4 or c>4 or r<0 or c<0 or move > 3:
        return
    if board[r][c] == -1: #막히면 못감
        return
    if board[r][c] == 1: #사과를 먹음
        apple +=1

    지나간위치 = board[r][c]
    board[r][c] = -1 #지나간 길을 장애물로 표시

    if apple == 2:
        bool = True
        return

    #현재 위치에서 상하좌우로 이동
    dfs(r+1 ,c ,move+1, apple)
    dfs(r-1 ,c ,move+1, apple)
    dfs(r ,c+1 ,move+1, apple)
    dfs(r ,c-1 ,move+1, apple)

    board[r][c] = 지나간위치

dfs(r,c,0,0)
if bool:
    print(1)
else:
    print(0)