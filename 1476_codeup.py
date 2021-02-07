n, m = map(int, input().split())
matrix = [[0]*m for i in range(n)]
cnt = 0

for i in range(0, n+m-1):              # index 활용을 위해
    for j in range(0, m):              # 열
        for k in range(0, n):          # 행
            if j+k == i:               # 행과 열의 합이 비교 값과 일치할 경우
                cnt += 1               
                matrix[k][j] =cnt
for i in range(0, n):                  
    for j in range(0, m):
        print(matrix[i][j], end=' ')
    print()

# 2차원 배열 빗금 방식으로 표시하기
# 다른 사람의 코드를 그대로 가져옴
