def solution(survey, choices):
    mbti_score = {
        "R" : 0, #1번 지표, 라이언 형
        "T" : 0, #1번 지표, 튜프 형
        "C" : 0, #2번 지표, 콘형
        "F" : 0, #2번 지표, 프로도형
        "J" : 0, #3번 지표, 제이지형
        "M" : 0, #3번 지표, 무지형
        "A" : 0, #4번 지표, 어피치 형
        "N" : 0  #4번 지표, 네오형
    }
    choices_score ={
        1 : 3,#매우 비동의
        2 : 2,#동의
        3 : 1,#약간 동의
        4 : 0,#모르겠음
        5 : 1,#약간 동의
        6 : 2,#동의
        7 : 3 #매우 동의
    }
    
    answer = ''
    for type, choice in zip(survey, choices):
        if choice < 4 : #점수가 4를 기준으로 1,2,3쪽이라면
            mbti_score[type[0]] += choices_score[choice] 
            #RT기준으로 R을 선택해서 type["R"]에 점수를 부여
        elif choice >= 5 : #점수 4 모르겠음 이후의 점수라면
            mbti_score[type[1]] += choices_score[choice]
    
    mbti_keys = list(mbti_score.keys())
    
    for left,right in zip(mbti_keys[::2], mbti_keys[1::2]):
        #점수를 1번 지표, 2번 지표 이렇게 끊어서 비교하기
        #오른쪽 왼쪽 중 점수가 큰 값을 answer에 추가
        #단, 하나의 지표에서 각 성격 유형 점수가 같으면, 
        #두 성격 유형 중 사전 순으로 빠른 성격 유형을 검사자의 성격 유형이라고 판단합니다.
        if mbti_score[left] >= mbti_score[right]:
            answer += left
        else:
            answer += right
    return answer