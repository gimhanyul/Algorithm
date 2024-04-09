n = int(input()) # 설탕 수
count = 0 #정답 출력
while n>=0:
    if (n%5==0): #5kg로 들 수 있다면
        count +=(n//5) #5로 나눈 몫만큼 봉지를 든다
        print(count)
        break #5kg경우는 다 경험
    n-=3 #3kg로 들고 다니기
    count+=1
else: #안되는 경우
    print(-1)
        
        