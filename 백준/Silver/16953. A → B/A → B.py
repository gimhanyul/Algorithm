def convert_A_to_B(A, B):
    count = 0
    while B > A:
        # B가 2로 나누어 떨어지면 2로 나눈다.
        if B % 2 == 0:
            B //= 2
        # B의 마지막 숫자가 1이면 1을 제거한다.
        elif B % 10 == 1:
            B //= 10
        else:
            # 위의 두 조건에 모두 해당하지 않으면 A를 B로 만들 수 없음
            return -1
        count += 1

    # 루프를 빠져나왔을 때, B가 A와 같아야 함. 그렇지 않으면 만들 수 없음
    if B == A:
        return count + 1  # 문제의 요구사항에 따라 연산 횟수에 1을 더해서 반환
    else:
        return -1

A, B = map(int, input().split())

print(convert_A_to_B(A, B))
