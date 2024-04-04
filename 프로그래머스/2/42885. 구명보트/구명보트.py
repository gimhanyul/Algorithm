def solution(people, limit):
    answer = 0
    people.sort() #작은 무게부터 큰 무게 정렬
    i , j = 0, len(people)-1
    
    while i<=j:
        if people[i] + people[j] <= limit:
            i += 1 #가장 가벼운 사람
        j -= 1 #가장 무거운 사람
        answer+= 1 # 둘의 합이 1
    return answer