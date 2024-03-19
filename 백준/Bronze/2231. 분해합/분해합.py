def solutino(N):
    for i in range(1, N):
        # 각 자리수의 합을 구함
        digit_sum = sum(map(int, str(i)))
        # i와 각 자리수의 합이 N과 같은지 확인
        if i + digit_sum == N:
            return i
    return 0 
N = int(input())
print(solutino(N))