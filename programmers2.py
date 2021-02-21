a, b = map(int, input().strip().split(' '))
print(a // b, a % b)
##########################################
a, b = map(int, input().strip().split(' '))
print(divmod(a, b))

# 가독성이나 팀의 코드 스타일에 따라서는 위 코드가 더 좋을 수 있음
# divmod는 작은 숫자를 다룰 때는 위 코드보다 느림, 큰 숫자를 다룰 때는 divmod가 더 빠름