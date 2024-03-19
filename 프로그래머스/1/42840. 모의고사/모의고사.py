def solution(answers):
    # 각 사람별 찍는 패턴
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    # 각 사람별 맞힌 문제 수를 저장할 리스트
    score = [0, 0, 0]
    
    # 각 정답과 각 사람의 답안을 비교
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)]:
                score[j] += 1
    
    # 최고 점수를 받은 사람 찾기
    max_score = max(score)
    return [i+1 for i, s in enumerate(score) if s == max_score]