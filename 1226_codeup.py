count = 0

lucky_num = [13, 23, 24, 35, 40, 45, 7]
lucky_bonus = lucky_num[6]
lucky_num = lucky_num[0:6]

user_num = [2, 6, 7, 23, 40, 44]
for i in user_num:
  if i in lucky_num:
      count += 1

if count == 6:
  print(1)
elif count == 5:
  for i in  user_num:
    if i in lucky_bonus:
      print(2)
    else:
      print(3)
elif count == 4:
  print(4)
elif count == 3:
  print(5)
else:
  print(0) 