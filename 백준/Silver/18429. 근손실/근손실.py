from itertools import permutations

N, K = map(int, input().split())
A = list(map(int, input().split()))

# 모든 운동 키트 순서의 순열을 생성
모든운동키트순서배열 = permutations(A, N)

# 가능한 경우의 수를 세는 변수
answer = 0

for permutation in 모든운동키트순서배열:
    현재중량 = 500 # 초기 중량 설정
    for 증가량 in permutation:
        현재중량 += 증가량 - K  # 중량 증가량 반영 및 운동 키트 사용으로 인한 감소량 반영
        if 현재중량 < 500:
            break  # 중량이 500 미만이면
    else:
        # 모든 운동 키트 사용 후 중량이 500 이상인 경우
        answer += 1

print(answer)

