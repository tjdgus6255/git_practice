import copy 
a, b = map(int, input().split())
x, y, z = map(int, input().split())
arr = [[0]*a for i in range(b)]
for i in range(a):
    arr[i] = list(map(int, input().split()))
k_count = 0
k = int(input())
arr_tem = copy.deepcopy(arr)       
def inspection(x, y, x_1, y_1):    # 본인을 제외하기 위한 함수
    if x == x_1 and y == y_1:
        return 0
    else:
        return 1
while k_count < k:       # 세대 변경을 위해서
    for i in range(a):
        for j in range(b):
            count = 0
            for k in range(-1, 2):          # 주위 값 count
                for l in range(-1, 2):      # 주위 값 count 
                    if i+k >= 0 and i+k <= a-1 and j+l >= 0 and j+l <= b-1 and inspection(i+k, j+l, i, j) == True:   # index를 초과하지 않기 위한 범위 설정 및 본인을 제외하고 count하기 위한 검사
                        if arr[i+k][j+l]:
                            count += 1
            if arr[i][j]:                       # 생명이 존재하는 경우
                if count < y or count >= z:     # 유지여부 판단
                    arr_tem[i][j] = 0
                if count >= y and count < z:    # 유지여부 판단 - 지워도 될 거 같은 부분...
                    arr_tem[i][j] = 1
            else:                               # 생명이 존재하지 않는 경우
                if count == x:                  # 생명 탄생 조건 판단
                    arr_tem[i][j] = 1
    k_count += 1                                # 다음 세대로 가기 위해..
    arr = copy.deepcopy(arr_tem)                # 세대가 2이상일 경우 필요..
for i in range(a):
    for j in range(b):
        print(arr_tem[i][j], end=' ')           # arr = copy.deepcopy(arr_tem)코드 덕분에 arr, arr_tem 둘다 사용 가능
    print()

# 생명게임
# 아직 풀지 못했다..... 
