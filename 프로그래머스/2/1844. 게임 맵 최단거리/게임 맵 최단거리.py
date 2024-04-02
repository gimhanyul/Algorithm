from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    # 방문한 위치를 체크할 배열
    visited = [[False] * m for _ in range(n)]
    
    # 상하좌우 이동
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    # BFS를 위한 큐 초기화 및 시작 위치 설정
    queue = deque([(0, 0, 1)]) # x, y, distance
    visited[0][0] = True
    
    while queue:
        x, y, dist = queue.popleft()
        
        # 목적지에 도착한 경우
        if x == n-1 and y == m-1:
            return dist
        
        # 상하좌우 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 맵 범위 내에 있고, 벽이 아니며, 방문하지 않았다면
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, dist+1))
    
    # 목적지에 도달할 수 없는 경우
    return -1