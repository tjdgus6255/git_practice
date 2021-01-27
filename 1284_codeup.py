import math

n = int(input())
a = []         
index = 0
sq = int(math.sqrt(float(n)))    # 제곱근 구하기

for i in range(0, 30):           # 0으로 리스트 초기화
    a.append(0)

for i in range(2, sq+1):         
    while n % i == 0:            # n을 나누었을 때 나누어 떨어지는 수 찾기
        n /= i                   # 두개의 인자만 남도록 하기 위해서
        a[index] = i             # list a에 추가 
        index += 1
if n != 1:                       # n이 1이 아닌 경우 list a에 n값 추가  
    a[index] = n
    index += 1
if index == 2:                   # list a값이 소수 2개와 자기자신을 포함한 경우,즉 값이 총 세개로 나오는 겨우
    print(int(a[0]), int(a[1]))
else:
    print("wrong number")