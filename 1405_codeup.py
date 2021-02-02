n = int(input())
arr = input().split()

for i in range(n):
  for j in range(n):
    print(arr[j], end=' ')
  print()
  arr.insert(n-1, arr.pop(0))

# n개의 숫자가 입력되면
# n개의 숫자를 왼쪽으로 하나씩 돌려서 출력