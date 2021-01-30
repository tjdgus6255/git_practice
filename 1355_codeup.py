# my code [Expression Error]
a = int(input())
b = 0
arr = [["*"]*a for i in range(a)]
for i in range(a):
  for j in range(b):
    arr[i][j] = ' '
  b += 1
  print(' ')
for i in range(a):
  for j in range(a):
    print(arr[i][j], end='')
  print()
# 답이 나오기는 하나 공백처리에서 에러 발생
#######################################

n = int(input())

for i in range(n, 0, -1):
  print(" "*(n-i), end='')
  print("*"*i)

# 블로그에 올라온 답과 비교

# 설명
# 역삼각형 출력하기