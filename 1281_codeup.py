a, b = map(int,input().split())
sum = 0

for i in range(a, b+1):
  if i % 2==0:                 # 짝수인 경우 빼기
    sum -= i
    print("-%d" %i, end='')
  else:                        # 홀수인 경우 더하기
    sum += i
    if i == a:                 # 맨 처음에 오는 값이 홀수(양수로 나타내야하는 수)인 경우 앞에 '+'표시 x
      print("%d" %i, end='')
    else:  
      print("+%d" %i, end='')
print("=%d" %sum)  

# 설명
# 자연수 a, b사이의 구간에 대해서 홀수는 더하고 짝수는 빼는 식을 보여준 후 결과 출력
# 식 나열시 양수인 경우 불필요하게 '+'를 붙이지 않는다