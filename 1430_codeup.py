a_n = int(input())
a = list(map(int, input().split()))
q_n = int(input())
q = list(map(int, input().split()))
for i in q:
    if i in a:
        print(1, end=' ')
    else:
        print(0, end=' ')

# 동일한 값이 존재하는지 찾기
# 메모리 초과... 