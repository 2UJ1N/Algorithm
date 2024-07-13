def solution(n):
    binn = str(bin(n)[2:])
    cnt1 = binn.count("1")
    tmp, cnttmp = n + 1, 0
    
    while cnt1 != cnttmp:
        bintmp = str(bin(tmp)[2:])
        cnttmp = bintmp.count("1")
        tmp += 1
    
    return tmp - 1