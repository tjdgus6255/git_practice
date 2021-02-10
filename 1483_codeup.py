n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]
cnt = n*m

for i in range(n+m-2, -1, -1):
    for j in range(m-1, -1, -1):
        for k in range(n-1, -1, -1):
            if j+k == i:
                arr[k][j] = cnt
                cnt -= 1

for i in range(n-1, -1, -1):        # 첫번째 for문은 그대로 유지              
    for j in range(m):              # 두번째 for문에서 print할 배열의 순서만 바꾸면 됨
        print(arr[i][j], end=' ')
    print()       
