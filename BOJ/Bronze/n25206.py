#
# 25206
# 너의 평점은
# https://www.acmicpc.net/problem/25206

total_credit = 0
total_grade = 0

grade_dict = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0.0
}

for _ in range(20):
    subject, credit, grade = input().split()

    if grade != "P":
        total_credit += float(credit)
        total_grade += float(credit) * float(grade_dict[grade])

print("{:.6f}".format(total_grade / total_credit))
        