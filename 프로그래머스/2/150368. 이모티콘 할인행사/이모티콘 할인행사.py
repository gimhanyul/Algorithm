from itertools import product

def solution(users, emoticons):
    할인비율 = [10, 20, 30, 40]
    result=[]

    for 할인조합 in product(할인비율, repeat=len(emoticons)):
        가입자수 = 0
        이모티콘구매 = 0
        
        for 요구할인율, 한정금액 in users:
            임티판매금액 = sum((emoticons[i] - emoticons[i] * 할인조합[i] / 100) for i in range(len(emoticons)) if 요구할인율 <= 할인조합[i])
            
            if 임티판매금액 >= 한정금액:
                가입자수 += 1
            else:
                이모티콘구매 += 임티판매금액
        
        result.append((가입자수, 이모티콘구매))
    #가입자 수 내림차순(5->4->3...)
    answer = sorted(result, reverse=True, key=lambda x: (x[0], x[1]))
    return answer[0]