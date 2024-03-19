import sys

def is_possible(arr, distance, N, C):
    last_pos = arr[0]
    count = 1

    for i in range(1, len(arr)):
        if arr[i] - last_pos >= distance:
            count += 1
            last_pos = arr[i]
            if count >= C: 
                return True
    return False

def max_distance(arr, N, C):
    arr.sort()  

    low = 1 
    high = arr[-1] - arr[0]

    result = 0
    while low <= high:
        mid = (low + high) // 2
        if is_possible(arr, mid, N, C):
            result = mid  
            low = mid + 1
        else:
            high = mid - 1

    return result

N, C = map(int, sys.stdin.readline().split())
homes = []
for _ in range(N):
    homes.append(int(sys.stdin.readline().strip()))

max_dist = max_distance(homes, N, C)
print(max_dist)
