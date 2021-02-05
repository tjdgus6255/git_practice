n, c = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
count = 0
for i in range(n):
  if count == c:        # 한줄이 채워질때마다 다음줄로 넘어감
    print()
    count = 0
  count += 1
  print(arr[i], end=' ')

  # 학생의 키순서대로 자리 배치
  # n은 학생 수, c는 한줄에 앉을 수 있는 자리수
  # 남은 자리는 공백