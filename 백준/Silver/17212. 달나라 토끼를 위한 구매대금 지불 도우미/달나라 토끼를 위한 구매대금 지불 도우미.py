#1원, 2원, 5원, 7원
#7원을 내야한다면 C[pay-7] = C[pay-d1] 7원에 동전 추가
#5원을 내야한다면 C[pay-5] = C[pay-d2] 5원에 동전 추가
#2원을 내야한다면 C[pay-2] = C[pay-d3] 2원에 동전 추가
#1원을 내야한다면 C[pay-1] = C[pay-d4] 1원에 동전 추가

pay = int(input())
coins = [1,2,5,7]
dp = [float('inf')] *(pay+1) #최소 동전 개수를 저장할 배열 초기화
dp[0] = 0 #0원을 거슬러 주는데 필요한 동전 개수는 0개

for p in range(1, pay + 1):
    for coin in coins:
        if p - coin >= 0:
            dp[p] = min(dp[p], dp[p - coin] + 1)
print(dp[pay])

