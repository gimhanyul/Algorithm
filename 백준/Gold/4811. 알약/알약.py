import math

def solution(n):
    if n == 0:
        return 1
    return math.comb(2*n, n) // (n + 1)

while True:
    T = int(input())
    if T == 0:
        break
    print(solution(T))