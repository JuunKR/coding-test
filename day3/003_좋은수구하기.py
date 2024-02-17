"""
주어진 N개의 수에서 다른 두 수의 합으로 표현되는 수가 있다면 그 수를 '좋은 수'라고 한다. N개의 수중 좋은 수가 총 몇개인지 출력하시오.

입력: 1번째 줄에 수의 개수 N, 2번째 줄에 N개의 수의 값이 주어진다.

출력: 좋은 수의 개수를 출력한다.

시간복잡도 : O(nlog)
"""

import sys
input = sys.stdin.readline
N = int(input())
Result = 0
A = list(map(int, input.split()))
A.sort()

for k in range(N):
    find = A[k]
    i = 0
    j = N - 1
    while i < j:
        if A[i] + A[j] == find:
            if i != k and j != k:
                Result += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif A[i] + A[j] < find:
            i += 1
        else: 
            j -= 1