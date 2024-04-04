N = int(input())
songs = [tuple(map(int, input().split())) for _ in range(N)]

기다리는_시간 = 0
연속재생 = 0

for D , V in songs:
    연속재생 -=V
    if 연속재생 < 0:
        기다리는_시간 -= 연속재생
        연속재생 = 0
    연속재생 += D

print(기다리는_시간)