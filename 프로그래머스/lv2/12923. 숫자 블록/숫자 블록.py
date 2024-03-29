from math import sqrt
LIMIT = 10000000

def fac(num):
    for i in range(2,int(sqrt(num))+1):
        if num % i == 0:
            if num // i > LIMIT:
                continue
            return num // i
    return 1

def solution(begin, end):
    answer = []
    if begin == 1:
        answer.append(0)
        begin += 1
        
    for i in range(begin, end+1):
        answer.append(fac(i))
    return answer