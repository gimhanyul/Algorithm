'''
1.스트라이크와 볼이 0인 경우를 필터링
2.모든 가능한 3자리 숫자에 대해 각 조건과 비교하여 가능성 있는 숫자를 찾기
3.조건에 따라 스트라이크 위치를 확인하고, 해당 숫자를 보관
4.최종적으로 가능한 숫자 조합을 확인하여 결과를 출력
'''

N = int(input()) 
Q = []

for _ in range(N):
    numbers, strike, ball = input().split()
    Q.append((numbers, int(strike), int(ball)))

# 가능한 모든 숫자 조합 생성
candidates = [str(i).zfill(3) for i in range(123, 988) if len(set(str(i))) == 3 and '0' not in str(i)]

# 조건에 맞는 숫자 필터링
def check(candidate, numbers, strike, ball):
    strike_count = sum(c == n for c, n in zip(candidate, numbers))
    ball_count = sum(c in numbers for c in candidate) - strike_count
    return strike_count == strike and ball_count == ball

for numbers, strike, ball in Q:
    candidates = [c for c in candidates if check(c, numbers, strike, ball)]

# 결과 출력
print(len(candidates))