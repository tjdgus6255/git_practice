def GuguClass():
  for j in range(1, 10):
    for i in range(2, 6):
      print("%d x %d = %2d" %(i, j, i*j), end='\t')
    print("")
  print("\n")

GuguClass()

# 설명
# 구구단 출력
# 연산자와 피연산자 사이에는 공백이 한칸 존재한다.
# 곱셈 기호는 소문자 x
# 곱셈 결과는 두 칸으로 봤을 때 우측 정렬(%2d)
# 단과 단 사이에는 탭(\t)으로 분리
# 각 행의 마지막인 5단의 곱셈 결과 출력 후 공백없이 줄 바꿈