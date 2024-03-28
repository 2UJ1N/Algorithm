# #
# # 11718
# # 그대로 출력하기
# # https://www.acmicpc.net/problem/11718

# while 1:
#     try:
#         print(input())
#     except:
#         exit()

a = 3
b = 5

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sumArr = [0]

for i in range(len(arr)):
	sumArr.append(sumArr[i] + arr[i])

print(sumArr)
answer = sumArr[b] - sumArr[a - 1]
print(answer)