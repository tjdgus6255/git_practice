n, m = map(int, input().split())
for i in range(n, 0, -1):
    if i % 2:
        for j in range(i*m,i*m-m,-1):
            print(j, end=' ')
    else:
        for j in range(i*m-m+1, i*m+1):
            print(j, end=' ')
    print()