N = int(input())
cards = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

#key와 value로 설정해서 answer 배열에 숫자를 출력
def solution(N, cards, M, targets):
    card_counts = {}
    for card in cards:
        if card in card_counts:
            card_counts[card] += 1
        else:
            card_counts[card] = 1
            
    answer = []
    for target in targets:
        if target in card_counts:
            answer.append(card_counts[target])
        else:
            answer.append(0)
    return answer

print(" ".join(map(str, solution(N, cards, M, targets))))