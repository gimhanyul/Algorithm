from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(100000)

N, M = map(int, input().split())
battlefield = [list(input().strip()) for _ in range(M)]
visited = [[False] * N for _ in range(M)]

def bfs(start_i, start_j):
    queue = [(start_i, start_j)]
    visited[start_i][start_j] = True
    count = 1  # 현재 그룹의 병사 수
    while queue:
        i, j = queue.pop(0)
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # 대각선 인접 제외, 상하좌우 탐색
            ni, nj = i + di, j + dj
            if 0 <= ni < M and 0 <= nj < N and not visited[ni][nj] and battlefield[ni][nj] == battlefield[i][j]:
                visited[ni][nj] = True
                queue.append((ni, nj))
                count += 1
    return count

power_white = 0
power_blue = 0

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            size = bfs(i, j)
            if battlefield[i][j] == 'W':
                power_white += size ** 2
            else:
                power_blue += size ** 2

print(power_white, power_blue)