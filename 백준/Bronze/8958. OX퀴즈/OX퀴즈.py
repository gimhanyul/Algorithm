N = int(input())

Q = []

for _ in range(N):
    row = input()
    Q.append(row)

for row in Q:
    score = 0
    cnt = 0
    for i in row:
        if i == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)
