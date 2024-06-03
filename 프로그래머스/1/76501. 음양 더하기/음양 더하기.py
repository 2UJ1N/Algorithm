def solution(absolutes, signs):
    return sum([ab if sign else -ab for ab, sign in zip(absolutes, signs)])