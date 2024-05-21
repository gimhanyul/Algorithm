def solution(s):
    char_map = {}  
    answer = []  

    for i, char in enumerate(s):
        if char in char_map:
            answer.append(i - char_map[char])
        else:
            answer.append(-1)

        char_map[char] = i

    return answer