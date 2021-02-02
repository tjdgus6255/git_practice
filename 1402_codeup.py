n = int(input())
arr = input().split()

arr.reverse()
for i in range(n):
  print(arr[i], end=' ')

# 설명
# n개의 데이터가 들어오고 그 n개의 데이터가 거꾸로 출력