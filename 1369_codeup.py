n, k = map(int, input().split()) 

arr = [[" "]*n for i in range(n)]    # n*n 배열 생성

for i in range(n):
  for j in range(n):
    if i == 0 or i == n-1 or j == 0 or j == n-1: # 사각형 테두리 '*' 삽입
      arr[i][j]="*"
  for j in range(k-1, n*2, k):                   # k 간격만큼 빗금(*) 표시
    if j-i >= 0 and j-i < n and i < n and i >= 0:
      arr[i][j-i]="*"  

for i in range(n):              # '*'삽입시 띄어쓰기
  for j in range(n):
    print(arr[i][j],end='')
  print()