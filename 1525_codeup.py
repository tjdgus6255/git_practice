arr = [[0]*10 for i in range(10)]
for i in range(10):
    arr[i] = list(map(int, input().split())) 
n = int(input())                    # player 수
r_c = [[0]*2 for i in range(n)]     # 좌표 받기 위한 배열
for i in range(n):                   
    r_c[i] = list(map(int, input().split()))
def index(value):                   # index 범위 내에 있는지 검사
    if value >= 0 and value <= 9:
        return 1
    else:
        return 0
def bomb(value, x, y):              # 물풍선 터트리기
    for i in range(0, value+1):     # 우 -> 좌 -> 상 -> 하 순으로 써놨어욤  
        if index(x+i) == True:      # index 범위 내 검사 먼저 실시
            if arr[x+i][y] == -1:   # -1 만나면 멈춤 
                break
            else: arr[x+i][y] = -2  # 안만나면 -2 입력하며 진행
        if index(x-i) == True:    
            if arr[x-i][y] == -1:
                break
            else: arr[x-i][y] = -2
        if index(y+i) == True:    
            if arr[x][y+i] == -1:
                break
            else: arr[x][y+i] = -2
        if index(y-i) == True:
            if arr[x][y-i] == -1:
                break
            else: arr[x][y-i] = -2

def player_check(order, x, y):      # dead, survive 출력을 위해
    if arr[x-1][y-1] == -2:
        print("player {0} dead".format(order+1))
    else:
        print("player {0} survive".format(order+1))
    
def player_xy(order, x, y):        # survive한 player 좌표 표시
    if arr[x-1][y-1] != -2:
        arr[x-1][y-1] = order + 1


        
for i in range(10):
    for j in range(10):
        if arr[i][j] >= 1:
            bomb(arr[i][j], i, j)

for i in range(n):
    player_xy(i, r_c[i][0], r_c[i][1])

for i in range(10):
    for j in range(10):
        print(arr[i][j], end=' ')
    print()

print("Character Information")
for i in range(n):
    player_check(i, r_c[i][0], r_c[i][1])