arr = [[0]*9 for i in range(9)]
for i in range(9):
    arr[i] = list(map(int, input().split()))

r, c = map(int, input().split())   # 입력되는 좌표

count = 0
def inspection(x, y, x_1, y_1):    # 본인을 제외하기 위한 함수
    if x == x_1 and y == y_1:
        return 0
    else:
        return 1

for k in range(-1, 2):
    for l in range(-1, 2):
        if r-1+k >= 0 and r-1+k <= 8 and c-1+l >= 0 and c-1+l <= 8 and inspection(r-1+k, c-1+l, r-1, c-1) == True:   # index를 초과하지 않기 위한 범위 설정 및 본인을 제외하고 count하기 위한 검사
            if arr[r-1+k][c-1+l]:
                count += 1

if arr[r-1][c-1]:
    print(-1)
else:
    print(count)

# 입력되는 좌표 (r, c) 주변의 지뢰 개수를 출력, (r, c) 자리에 지뢰가 있다면 -1 출력