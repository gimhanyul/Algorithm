def solution(n, results):
    wins = [[False] * (n + 1) for _ in range(n + 1)]
    
    for winner, loser in results:
        wins[winner][loser] = True

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if wins[i][k] and wins[k][j]:
                    wins[i][j] = True

    # 정확한 순위를 매길 수 있는 선수의 수 계산
    answer = 0
    for i in range(1, n + 1):
        count = 0
        for j in range(1, n + 1):
            if wins[i][j] or wins[j][i]:
                count += 1
        if count == n - 1:  # 자기 자신을 제외하고 모든 선수와의 관계를 알아야 하므로 n-1 이어야 함
            answer += 1

    return answer
