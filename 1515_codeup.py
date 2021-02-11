import copy

arr = [[0]*25 for i in range(25)]
for i in range(25):
    arr[i] = list(map(int, input().split()))
arr_tem = copy.deepcopy(arr)
def inspection(x, y, x_1, y_1):
    if x == x_1 and y == y_1:
        return 0
    else:
        return 1
        
for i in range(25):
    for j in range(25):
        count = 0
        for k in range(-1, 2):
            for l in range(-1, 2):
                if i+k >= 0 and i+k <= 2 and j+l >= 0 and j+l <= 2 and inspection(i+k, j+l, i, j) == True:
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
