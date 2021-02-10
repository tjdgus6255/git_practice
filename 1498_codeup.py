from math import ceil
n, g = map(int, input().split())
arr = list(map(int, input().split()))
r = ceil(n / g)   # loop문을 몇번 작동 시킬지 결정 - ceil은 오름차순
arr_n = []
for i in range(r):          
    arr_l = arr[:g]           # slice한 값을 또 다른 배열에 넣음
    arr_l.sort()              # 오름차순 정렬
    print(arr_l[0],end=' ')   # 인덱스 첫번째의 값을 출력
    del arr[:g]               # slice한 부분은 삭제

# n개의 데이터를 배열에 입력 받은 후
# g개씩 묶어 비교한 후, 작은 값만 들어간 배열 만들기