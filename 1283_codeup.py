a = int(input())   # 투자 액수
a_first = a
b = int(input())   # 투자 일 수 
p = list(map(int, input().split()))  # 일별 변동폭
for i in p:
  a = a + a * (i/100)
a_last = a - a_first    # 순수익(총수익(최종 값) - 총비용(투자 비용))
print("%.0f" %a_last)
if a_last < 0:
  print("bad")
elif a_last == 0:
  print("same")
else:
  print("good") 

# 설명
# 투자한 돈의 액수와, 그 주식의 하루간의 변동을 퍼센트로 알 때 순수익, 이득/손해 판단