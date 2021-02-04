from operator import itemgetter

n = int(input())
name_score = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    name_score.append([name, score])
name_score.sort(key=itemgetter(1), reverse=True) # itemgetter(index) - index를 기준으로 내림차순
print(name_score[2][0]) # 세번째 큰값 중 이름 출력

# 세번째로 점수가 높은 학생의 이름 출력
#####################################################
num = int(input())
score_list = []
for i in range(num):
    name, score = input().strip().split()
    score_list.append((name, int(score)))

score_list.sort(key=lambda x:x[1], reverse=True) # y축을 기준으로 내림차순 정렬
print(score_list[2][0])

# 다른사람의 코드, lambda식 사용하여 문제 해결