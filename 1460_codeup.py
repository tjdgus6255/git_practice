n = int(input())
a = [i for i in range(1,n*n+1)]
for j in a:
    print(j,end=' ')
    if j % n == 0:
        print()
# memory : 34600, time : 34
###############################
n = int(input())
for j in range(1, n*n+1):
    print(j,end=' ')
    if j % n == 0:
        print()
# memory : 34024, time : 27

# n*n 크기의 배열 출력