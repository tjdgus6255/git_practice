n = int(input())                                       
m_i = []
for i in range(n):
    m_i = list(map(int, input().split()))             # 수학과 정보과목 점수 받음
    m_i.append(i+1)                                   # 학생 번호를 추가로 넣음
m_i.sort(key = lambda x : (x[0], x[1]), reverse=True) # 먼저 수학을 기준으로 내림차순, 그 다음은 정보
                                                      # 학생번호는 굳이 안해도 될거 같아서 제외함(정확하지는 않음..)
for i in range(n):                                    # 이를 출력
    print(m_i[i][2], m_i[i][0], m_i[i][1])            # visual studio에서 실행해보았는데 성공하였다.
                                                      # 그런데 제출하면 출력자체가 안된다..왜지?
#####################################################
num=int(input())
number=1
score_list=[]
for i in range(num):
    math,info=map(int,input().split())
    score_list.append([number,math,info])                      # 추측하건데 여기에서의 차이때문에 그러지 않았나 싶다.
    number+=1                                                  # number(학생번호)는 계속 증가함
score_list.sort(key=lambda x:(x[1],x[2],-x[0]), reverse=True)  # x[*]앞에 -를 붙이면 정렬이 반대로 되는걸 이 코드를 보고 알게됨
for element in score_list:
    print(element[0],element[1],element[2])                    # 내 코드에도 이렇게 하면 훨씬 깔끔해보일듯!

# 학생 번호, 수학, 정보 점수를 가진 데이터가 있다.
# 정렬 기준은 수학점수가 높은 순으로 정렬하되, 수학점수가 같으면 정보점수가 높은 순,
# 정보점수도 같으면 번호가 빠른 순서로 정렬
# 다른사람의 코드를 가져와 비교(위 : 나, 아래 : 타인)