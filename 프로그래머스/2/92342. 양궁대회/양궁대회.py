def solution(n, info):
    max_diff = 0 #최대 점수차
    answer = [-1] #라이언의 과녁판 기본값 -1(라이언이 지는 경우)
    
    #점수인덱스, 남은화살, 라이언점수판
    def dfs(score_idx, remaining_arrows, ryan_scores):
        nonlocal max_diff, answer
        
        if score_idx > 10:
            ryan_points = 0 #라이언 점수
            apeach_points = 0 #어피치 점수
            
            for i in range(11): #info[i] = 어피치 점수판
                if ryan_scores[i] == 0 and info[i] == 0:
                    continue
                if ryan_scores[i] > info[i]:
                    ryan_points += 10 - i
                else:
                    apeach_points += 10 - i
            
            #가장 큰 점수 차이 찾기
            diff = ryan_points - apeach_points
            if diff > max_diff:
                max_diff = diff
                answer = ryan_scores[:]
            elif diff == max_diff and max_diff > 0:
                if ryan_scores[::-1] > answer[::-1]:
                    answer = ryan_scores[:]
            return
        
        # 현재 점수 idx에서 가능한 모든 화살 쏘는 경우를 시도
        max_arrows_to_shoot = remaining_arrows
        if score_idx < 10:
            max_arrows_to_shoot = min(remaining_arrows, info[score_idx] + 1)
        
        for arrows in range(max_arrows_to_shoot + 1):
            ryan_scores[score_idx] = arrows
            dfs(score_idx + 1, remaining_arrows - arrows, ryan_scores)
            ryan_scores[score_idx] = 0  # backtrack(사용한 값 초기화)
    
    dfs(0, n, [0] * 11)#초기설정
    
    return answer