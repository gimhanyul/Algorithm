arr = []
for _ in range(9):
    num = int(input())
    arr.append(num)

max_value = max(arr)
print(max_value)
max_index = arr.index(max_value)
print(max_index+1)