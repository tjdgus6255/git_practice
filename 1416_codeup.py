n = int(input())
arr = []
if n == 0:           # n이 0일 경우 그대로 출력
  print(n)
while n >= 1:        # 1이상 일 경우
  arr.append(n%2)    # 2로 나눈 나머지를 추가
  n = n // 2         # 몫을 n에 대입 
arr.reverse()        # arr 배열 뒤집기 
for i in arr:        
    print(i, end='')


# 10진수가 주어지면 2진수로 변환
##############################################
num = int(input())    # 2진수 변환을 위해서 int로 변환
num = str(bin(num))   # 2진수 변환 및 문자형 변환
print(num[2:])        # 앞의 부분을 제거하여 출력 (ex.'0b')

# 두번째 코드는 google에서 다른 사람의 코드를 가져옴