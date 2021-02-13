N = int(input())
arr = list(map(int, input().split()))
arr_rank = sorted(arr)

for i in range(N):
    print(arr_rank.index(arr[i]), end=' ')
###########################################
def binarysearch(arr, target, first, last):
    if first > last:
        return 1
    mid = int((first+last)/2)
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return binarysearch(arr, target, first, mid-1)
    else:
        return binarysearch(arr, target, mid+1, last)
num=int(input())
arr=list(map(int, input().split()))
arr2=sorted(arr)
for i in range(num):
    print(binarysearch(arr2, arr[i], 0, num-1),end=' ') 
############################################

# N개의 데이터를 0 ~ N-1로 재정렬하여 출력
# 위에는 내가 쓴 코드, 밑에는 가져온 코드
# 내가 쓴 코드는 index 때문에 시간복잡도 O(n)으로 인해 시간초과
# 이를 해결하기 위해 이진탐색트리를 사용해야 함
# 이진탐색트리의 개념 이해하기