def solution(citations):
    a = sorted(citations)
    if max(a) == 0:
        return 0
    for n in range(len(a)):
        if a[n] >= len(a[n:]):
            return len(a[n:])
            
print(solution([3, 0, 6, 1, 5]))