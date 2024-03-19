import sys

N, P = map(int, sys.stdin.readline().split())
cnt = 0
lst = [[] for _ in range(7)]  
# 기타 줄은

for _ in range(N):
    n, p = map(int, sys.stdin.readline().split())
    while lst[n] and lst[n][-1] > p:  # 현재 줄의 마지막 프렛이 입력받은 프렛보다 높은 경우
        lst[n].pop()  # 프렛을 하나 빼고 손가락을 떼는 동작을 카운트합니다.
        cnt += 1
    if not lst[n] or lst[n][-1] < p:  # 현재 줄이 비어있거나 마지막 프렛이 입력받은 프렛보다 낮은 경우
        lst[n].append(p)  # 새로운 프렛을 누르고, 그 동작을 카운트합니다.
        cnt += 1

print(cnt)
