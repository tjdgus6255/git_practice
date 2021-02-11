import copy # 깊은 복사를 위해서

arr = [[0]*25 for i in range(25)]
for i in range(25):
    arr[i] = list(map(int, input().split()))
arr_tem = copy.deepcopy(arr)       # arr_tem = arr은 주소 복사(얕은 복사)
def inspection(x, y, x_1, y_1):    # 본인을 제외하기 위한 함수
    if x == x_1 and y == y_1:
        return 0
    else:
        return 1
        
for i in range(25):
    for j in range(25):
        count = 0
        for k in range(-1, 2):
            for l in range(-1, 2):
                if i+k >= 0 and i+k <= 2 and j+l >= 0 and j+l <= 2 and inspection(i+k, j+l, i, j) == True:   # index를 초과하지 않기 위한 범위 설정 및 본인을 제외하고 count하기 위한 검사
                    if arr[i+k][j+l]:
                        count += 1
        if arr[i][j]:
            if count <= 1 or count >= 4:
                arr_tem[i][j] = 0
        else:
            if count == 3:
                arr_tem[i][j] = 1    
for i in range(25):
    for j in range(25):
        print(arr_tem[i][j], end=' ')
    print()

# 생명 게임
# 생명이 있는 칸 : 1, 생명이 없는 칸 0
# 생명이 있는 칸 주위 8칸에 2 또는 3의 생명이 있으면 다음 세대에도 생명 존재
# 생명이 없는 칸 주위 8칸에 3의 생명이 있으면 다음 세대에 생명 존재

# 얕은 복사와 깊은 복사의 개념을 이해해야한다.(이를 몰라서 삽질을 했다...;;)