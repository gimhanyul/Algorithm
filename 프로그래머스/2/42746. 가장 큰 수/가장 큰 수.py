def solution(numbers):
    정렬된숫자 = sorted(map(str, numbers), key= lambda x:x*3, reverse=True)

    answer = ''.join(정렬된숫자)
    return str(int(answer))