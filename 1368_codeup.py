h, k, d = input().split()        # h : 높이, k : 밑변, d : 방향 정보
h_2 = int(h)                    
k_2 = int(k)
for i in range(h_2):             
  if d == 'L':
    print(' '*i, end='')
    print("*"*k_2)
  else:
    print(' '*(k_2-i), end='')
    print("*"*k_2)

# 설명
# 평행사변형 출력
# L = 왼쪽 아래 공백, R = 오른쪽 아래 공백