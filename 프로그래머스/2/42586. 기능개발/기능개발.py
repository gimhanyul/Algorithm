def solution(progresses, speeds):
    완료일 = [(100 - progresses[i]) // speeds[i] + (1 if (100 - progresses[i]) % speeds[i] != 0 else 0) for i in range(len(progresses))]

    answer = []
    
    배포일 = 완료일[0]
    count = 1
    
    # 각 배포일을 체크
    for i in range(1, len(완료일)):
        if 완료일[i] <= 배포일:
            # 완료일이 현재 배포일보다 빠르면 같은 그룹
            count += 1
        else:
            answer.append(count)
            배포일 = 완료일[i]
            count = 1
    
    # 마지막 배포 그룹 추가
    answer.append(count)
    
    return answer