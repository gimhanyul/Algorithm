def solution1(array, commands):
    answer = []
    for num in commands:
        first = num[0]-1
        last = num[1]
        find = num[2]-1
        new_array = sorted(array[first:last])
        answer.append(new_array[find])
    return answer

def solution2(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
