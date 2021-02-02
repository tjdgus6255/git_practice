n = int(input())
a = int((n-1) / 2)           # 몇 줄을 출력해야하는지 알기 위해
for i in range(a+1):         
    print(" "*(a-i), end='') # 공백을 먼저 출력 후 
    print("*"*(2*i+1))       # '*' 출력

#   *
#  ***
# *****  다음과 같은 삼각형 출력
