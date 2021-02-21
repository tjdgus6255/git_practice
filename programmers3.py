num, base = map(int, input().strip().split(' '))
num3 = num // 1000 * base**3
num = num % 1000
num2 = num // 100 * base**2
num = num % 100
num1 = num // 10 * base
num = num % 10
print(num3 + num2 + num1 + num)
################################################
num, base = map(int, input().strip().split(' '))
answer = 0
for idx, i in enumerate(num[::-1]):         # enumerate : index 번호와 원소를 같이 출력하고자 할 때 사용
    answer += int(i) * ( base ** idx )
################################################
num = '3212'
base = 5
answer = int(num, base)    # python의 int함수는 진법 변환을 지원

# 내 코드(상), 평균 코드(중), 답지(하)
# 더 노력하기