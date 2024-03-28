#
# 10101
# 삼각형 외우기
# https://www.acmicpc.net/problem/10101

ang1 = int(input())
ang2 = int(input())
ang3 = int(input())

if ang1 == 60 and ang2 == 60 and ang3 == 60: print("Equilateral")
elif ang1 + ang2 + ang3 == 180:
    if ang1 != ang2 and ang2 != ang3 and ang3 != ang1: print("Scalene")
    else: print("Isosceles")
else: print("Error")