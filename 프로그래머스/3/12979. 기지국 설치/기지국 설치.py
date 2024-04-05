import math

def solution(n, stations, w):
    answer = 0
    last = 0  # 마지막으로 전파가 닿는 위치
    전파가능거리 = 2 * w + 1 

    for station in stations:
        전파시작 = max(station - w, 1) 
        전파끝 = min(station + w, n) 

        if 전파시작 > last + 1:
            남은아파트 = 전파시작 - (last + 1)
            answer += math.ceil(남은아파트 / 전파가능거리)

        last = 전파끝 

    if n > last:
        answer += math.ceil((n - last) / 전파가능거리)

    return answer
