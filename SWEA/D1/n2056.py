#
# 2056
# 연월일 달력
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QLkdKAz4DFAUq

m = [i for i in range(1, 13)]
d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(1, int(input()) + 1):
    cal = input()
    year = cal[: 4]
    month = cal[4 : 6]
    date = cal[6 : ]

    print("#" + str(i), end=" ")
    if int(month) not in m: print(-1)
    else:
        if int(date) <= d[int(month) - 1]: 
            print(year, month, date, sep="/")
        else: print(-1)