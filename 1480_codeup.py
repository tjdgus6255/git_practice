# n, m = map(int, input().split())
n, m = 3, 4
arr = [[0]*m for _ in range(n)]
cnt = 0

for i in range(n+m-2, -1, -1):
    for j in range(m-1, -1, -1):
        for k in range(n-1, -1, -1):
            if j+k == i:
                cnt += 1
                arr[k][j] = cnt

for i in range(0, n):                  
    for j in range(0, m):
        print(arr[i][j], end=' ')
    print()       