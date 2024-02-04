'''
배열의 주어진 범위의 합을 2로 나눈 몫을 구함
'''
# 잘못된 코드
import random

testcase = int(input("input: "))  # testcase 5
answer = 0 # 오류 1. 초기화

A = [0] * (100001)

for i in range(0, 10001): # 오류 2. 인덱스 범위
    A[i] = random.randrange(1, 101)

for t in range(1, testcase + 1): 
    start, end = map(int, input("input 2 nums: ").split()) # start 1, end 10
		# start, end = map(int, sys.argv[2].split())

    for i in range(start, end + 1):
        answer = answer + A[i]

    print(str(testcase) + " " + str(answer / 2)) # 오류 3. 잘못된 변수 # 오류4. 형변환