import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))

half = sum(arr)//2

if n ==1 and arr[0] ==1:
    print("Happy")
elif max(arr) <= half:
    print("Happy")
else:
    print("Unhappy")