n = input()
n_left = 0    # 여는 괄호
n_right = 0   # 닫는 괄호
for i in n:
  if i == '(':
    n_left += 1
  else:
    n_right += 1
print(n_left, n_right)   

# 여는 괄호와 닫는 괄호의 갯수를 출력