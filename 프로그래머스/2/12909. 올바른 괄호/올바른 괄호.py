def solution(s):
    if len(s) == 0: return False
    
    if s[0] == ')' or s[-1] == '(': return False
    else:
        remain = []
        for i in s:
            if i == '(': remain.append(i)
            else:
                if len(remain) != 0 and remain[-1] == '(': remain.pop()
                else: return False
        if len(remain) == 0: return True
        else: return False

    return True