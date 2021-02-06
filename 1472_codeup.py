n, m = map(int, input().split())
for i in range(n, 0, -1):
    if i % 2:
        for j in range(i*m,i*m-m,-1):
            print(j, end=' ')
    else:
        for j in range(i*m-m+1, i*m+1):
            print(j, end=' ')
    print()

# n*m 지그재그 배열
# 큰 값 -> 작은 값 순으로 출력