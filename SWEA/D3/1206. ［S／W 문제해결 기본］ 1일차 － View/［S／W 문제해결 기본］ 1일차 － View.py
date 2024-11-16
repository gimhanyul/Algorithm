T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    height = list(map(int, input().split()))

    answer = 0  # 조망권 확보된 수

    for i in range(2, n - 2):
        max_height = max(
            height[i - 2],
            height[i - 1],
            height[i + 1],
            height[i + 2]
        )
        if height[i] > max_height:
            answer += height[i] - max_height
    print(f'#{test_case} {answer}')
                   
