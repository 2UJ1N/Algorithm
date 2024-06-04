def solution(n):
    base = ''
    while n:
        base += str(n % 3)
        n //= 3
        
    answer = int(base, 3)
    return answer