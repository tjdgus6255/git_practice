lucky_num = list(map(int, input().split())) # 당첨 번호
lucky_bonus = lucky_num[6] # 마지막 인덱스 값은 lucky_bonus에 추가로 지정
del lucky_num[6] # lucky_num의 마지막 인덱스 값 삭제
user_num = list(map(int, input().split())) # 사용자 번호
count = 0 
bonus = False 

lucky_num.sort() # 오름차순 정렬
user_num.sort()
for i in lucky_num:            # 당첨 번호와 사용자 번호 비교
  for j in user_num:
      if i == j:
          count += 1

if count == 6:                 # 6개 모두 맞힌 경우 1등
  print('1')
elif count == 5:               # 5개 맞힌 경우 보너스 값 비교하여 2등 또는 3등 할당
  for i in user_num:
    if i == lucky_bonus:
      bonus = True
      break
    else:
      bonus = False
  if bonus:
      print('2')
  else:
      print('3')
elif count == 4:               # 4개 맞힌 경우 4등
  print('4')
elif count == 3:               # 3개 맞힌 경우 5등
  print('5')
else:                          # 나머지 0
  print('0')  

# 설명
# 첫줄 로또 당첨번호 6개, 보너스 번호 1개
# 둘째 줄 사용자 로또 번호 6개