def solution(N, number):
    # 문자열 N을 숫자로 변환
    N = int(N)

    if N == number:
        return 1

    # 각 단계에서 생성된 모든 결과를 저장할 집합의 리스트
    results = [set() for _ in range(9)]
    results[1].add(N)

    for i in range(2, 9):
        for j in range(1, i):
            for op1 in results[j]:
                for op2 in results[i-j]:
                    results[i].add(op1 + op2)
                    results[i].add(op1 - op2)
                    results[i].add(op1 * op2)
                    if op2 != 0:
                        results[i].add(op1 // op2)
        
        # N을 i번 이어붙인 결과 추가
        results[i].add(int(str(N) * i))

        if number in results[i]:
            return i

    return -1

