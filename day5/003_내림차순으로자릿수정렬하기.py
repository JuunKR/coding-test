"""
배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

입력:
첫째 줄에 정렬하려고 하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

출력:
첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.

"""

import sys

print = sys.stdout.write

A = list(input())

for i in range(len(A)):
    Max = i
    for j in range(i+1, len(A)):
        if A[j] > A[Max]:
            Max = j
    if A[i] < A[Max]:
        temp = A[i]
        A[i] = A[Max]
        A[Max] = temp
for i in range(len(A)):
    print(A[i])