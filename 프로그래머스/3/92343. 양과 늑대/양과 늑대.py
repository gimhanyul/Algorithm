def solution(info, edges):
    visited = [0] * len(info)  # 각 노드의 방문 여부
    max_sheep = [0]  # 최대 양의 수를 담을 리스트
    
    def dfs(node, sheep, wolf, next_nodes):
        if info[node] == 0:  # 현재 노드가 양이라면
            sheep += 1
        else:  # 현재 노드가 늑대라면
            wolf += 1
        if sheep <= wolf:  # 늑대의 수가 양보다 많거나 같으면 더 이상 탐색하지 않음
            return
        max_sheep[0] = max(max_sheep[0], sheep)  # 최대 양의 수 갱신
        
        for i in next_nodes:  # 다음 가능한 모든 노드에 대해 탐색
            visited[i] = 1  # 방문 표시
            # 다음 탐색할 노드 추가, 현재 노드 제외
            new_next_nodes = next_nodes + [child for parent, child in edges if parent == i and not visited[child]]
            new_next_nodes.remove(i)  # 현재 탐색하는 노드는 제외
            dfs(i, sheep, wolf, new_next_nodes)  # 재귀 호출
            visited[i] = 0  # 방문 해제(백트래킹)

    # 루트 노드에서 시작, 처음에는 양 한 마리
    visited[0] = 1
    initial_nodes = [child for parent, child in edges if parent == 0]
    dfs(0, 0, 0, initial_nodes)

    return max_sheep[0]