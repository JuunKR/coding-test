"""
N개의 숫자가 공백 없이 써있다. 이 숫자를 모두 합해 출력하는 프로그램을 작성하시오.

입력: 1번째 줄에 숫자의 개수, 2번째 줄에 숫자 N개가 공백 없이 주어짐
출력: 입력으로 주어진 숫자 N개의 합을 출력한다.
"""

n = input()
numbers = list(input())
sum = 0
for i in numbers:
    sum = sum + int(i)
print(sum)
