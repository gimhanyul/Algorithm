def solution(n, k):
    서비스 = n//10
    실음료수 = k-서비스
    answer = (12000*n)+(2000*실음료수)
    return answer