# 197p
# 실전문제
# 부품 찾기

import sys

# N, N 개의 정수, M, M 개의 정수 입력
N = int(input())
list_N = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(input())
list_M = list(map(int, sys.stdin.readline().rstrip().split()))

# list_N 을 정렬
list_N.sort()


# 이진 탐색 재귀 함수
def bin_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return bin_search(array, target, start, mid - 1)
    else:
        return bin_search(array, target, mid + 1, end)


# list_N 에서 list_M 의 각 원소가 존재하는지를 이진 탐색으로 찾는다.
for i in range(M):
    target_index = bin_search(list_N, list_M[i], 0, N - 1)
    if target_index is None:
        print('no')
    else:
        print('yes')