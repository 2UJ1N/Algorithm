def solution(n, m):
    answer = [gcd(n,m), lcm(n,m)]
    return answer

def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)

def lcm(a, b):
    return int(a * b / gcd(a, b))