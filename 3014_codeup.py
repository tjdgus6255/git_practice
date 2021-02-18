n = int(input())
arr = list(map(int, input().split()))
n = 5
arr = [2, 5, 8, 1, 2]
arr_a = []
for i in range(n): 
    arr_a.append(min(arr))     # 최소값을 다른 배열에 넣음
    arr.remove(min(arr))       # 최소값을 하나씩 제거
    print(arr_a[i], end=' ')   # 최소값이 들어간 다른배열을 출력

# memory error
# sort 사용 없이 오름차순 정렬
# O(nlogn) 사용하라지만 어떻게 해야할지... 