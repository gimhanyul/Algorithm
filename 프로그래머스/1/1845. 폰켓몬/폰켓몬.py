def solution(nums):
    types = set(nums) #set자료형은 중복을 허용하지 않음
    bring_cat = len(nums)//2
    result = min(len(types), bring_cat)
    return result