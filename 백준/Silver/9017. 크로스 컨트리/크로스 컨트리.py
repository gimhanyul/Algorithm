import sys
from collections import Counter
input = sys.stdin.readline

T= int(input().rstrip())

for _ in range(T):
    n = int(input().rstrip())
    scores = list(map(int, input().rstrip().split()))
    #각 팀을 딕셔너리의 키로 저장하고,팀의 개수를 딕셔너리의 값으로 저장
    counter = Counter(scores) 
    board = {} #6명 이상 참가한 팀들의 점수 딕셔너리
    skipped_count = 0 #6명이상 참가 안 한 팀은 넘겨서
    
    for i in range(n):
        if counter[scores[i]] < 6: #팀의 수가 6명이 안되면
            skipped_count += 1
            continue
        if scores[i] in board: #조건에 해당하는 팀들만 점수 계산
            board[scores[i]].append(i - skipped_count)
        else:
            board[scores[i]] = [i - skipped_count]
    print(sorted(board, key=lambda x:(sum(board[x][0:4]), board[x][4]))[0])