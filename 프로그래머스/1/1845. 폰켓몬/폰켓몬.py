def solution(nums):
     # 고유한 종류의 수
    a = len(set(nums))
    # 선택 가능한 폰켓몬 수
    b = len(nums) // 2
    
    # 최종 선택 가능한 폰켓몬 종류 수 반환
    return min(a, b)