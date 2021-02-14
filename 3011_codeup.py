import copy

def bubbleSort(x, count):    # 위키백과 bubble sort 가져옴
    length = len(x) - 1
    x_1 = copy.deepcopy(x)   # 정렬 이전과 정렬 이후의 배열 비교
    for i in range(length):
        for j in range(length-i):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
        if x != x_1:                 # 한 단계 완료시점에서 이전 배열, 이후 배열 비교
            count += 1               # 두 개의 배열이 다르면 count
            x_1 = copy.deepcopy(x)   # 정렬 이후의 배열을 이전 배열에 삽입
    return count
n = int(input())
arr = list(map(int, input().split()))

print(bubbleSort(arr, 0))

# Bubble Sort
# 이웃하는 숫자들끼리 크기를 비교하여 자리를 바꾸는 정렬 기법
# 정렬이 완료된 시점 출력하기
# Bubble Sort에 대한 개념 이해하기