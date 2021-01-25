a , b = map(int, input().split())
list_cal = []
def cal(value1, value2):
    list_cal.append(value1 + value2)
    list_cal.append(value1 - value2)
    list_cal.append(value1 * value2)
    list_cal.append(value1 / value2)
    list_cal.append(value1 ** value2)
cal(a, b) # a, b의 연산 결과를 list_cal에 입력
cal(b, a) # a, b의 위치를 바꾼 연산 결과를 list_cal에 입력
print("%.6f" %max(list_cal)) # 최댓값, 소수점 6자리

# 설명
# 두 실수 a, b가 입력되면 그 두수를 더하거나 빼거나 곱하거나 나누거나 제곱을 해서 가장 큰 수 출력
