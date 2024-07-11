def solution(s):
    strArr = s.split(" ")
    numArr = list(map(int, strArr))
    answer = str(min(numArr)) + " " + str(max(numArr))
    
    return answer