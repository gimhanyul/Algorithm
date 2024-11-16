def solution(numbers, exchange_count):
    numbers = list(map(int, str(numbers))) 
    n = len(numbers)  
    visited = set()  # 방문한 상태 저장

    def dfs(cnt, nums):
        num_key = ''.join(map(str, nums)) + str(cnt)
        if num_key in visited:
            return 0

        visited.add(num_key)

        if cnt == exchange_count:  # 교환 횟수만큼 변경가능
            return int(''.join(map(str, nums)))

        max_value = 0
        # 교환수만큼 교환해서 가장 큰 수 만들기
        for i in range(n):
            for j in range(i+1, n):
                nums[i], nums[j] = nums[j], nums[i]
                max_value = max(max_value, dfs(cnt+1, nums[:]))
                nums[i], nums[j] = nums[j], nums[i] 
        return max_value

    result = dfs(0, numbers)
    return result

T = int(input()) 
for test_case in range(1, T + 1):
    numbers, exchange_count = map(int, input().split())
    max_value = solution(numbers, exchange_count)
    print(f"#{test_case} {max_value}")