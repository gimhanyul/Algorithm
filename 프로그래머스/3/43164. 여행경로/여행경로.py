def solution(tickets):
    from collections import defaultdict

    # 그래프 생성
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)

    for key in graph:
        graph[key].sort(reverse=True)  

    route = []

    def dfs(airport):
        while graph[airport]:
            next_airport = graph[airport].pop()
            dfs(next_airport)
        route.append(airport)

    # DFS 시작
    dfs("ICN")
    return route[::-1]

