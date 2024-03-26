def solution(citations):
    citations.sort(reverse=True)
    h_index = 0
    for i , 논문인용 in enumerate(citations):
        if i+1 <= 논문인용:
            h_index = i+1
        else:
            break
    return h_index