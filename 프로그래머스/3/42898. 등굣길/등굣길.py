def solution(m, n, puddles):
    # 격자를 만들고 모든 칸을 0으로 초기화합니다.
    grid = [[0] * (m + 1) for _ in range(n + 1)]
    # 시작점 초기화
    grid[1][1] = 1

    # 물웅덩이가 있는 위치를 표시합니다.
    for x, y in puddles:
        grid[y][x] = -1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 시작점이거나 물웅덩이인 경우 건너뜁니다.
            if (i == 1 and j == 1) or grid[i][j] == -1:
                continue

            # 왼쪽이나 위쪽 칸이 물웅덩이가 아닌 경우, 해당 칸까지의 경로 수를 더합니다.
            grid[i][j] = max(0, grid[i-1][j]) + max(0, grid[i][j-1])
            grid[i][j] %= 1000000007

    # 목적지 칸의 값을 반환합니다.
    return grid[n][m]
