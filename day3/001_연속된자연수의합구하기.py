"""
어떠한 자연수 N은 몇개의 연속된 자연수의 합으로 나타낸다.
자연수 N을 몇개의연속된 자연수의 합으로 나타내는 가짓수를 알고 싶다.
ex) 15 = 7 + 8, 4 + 5 + 6, 1 + 2 + 3 + 4 + 5
자연수 N을 입력받아 연속된 자연수의 합으로 나타내는 가짓수를 출력하는 프로그램 작성할 것.


입력: 1번째 줄에 정수 N이 주어진다.
출력: 입력된 자연수 N을 연속된 자연수의 합으로 나타내는 가짓수를 출력한다.
제한시간: 2초
N의 최대값 : 10,000,000
"""

n = int(input())
count = 1
start_index = 1
end_index = 1
sum = 1


while end_index != n:
    if sum == n:
        count += 1
        end_index += 1
        sum += end_index
    elif sum > n:
        sum -= start_index
        start_index += 1
    else:
        end_index += 1
        sum += end_index
    print("################################")
    print("count: ", count)
    print("start_index: ", start_index)
    print("end_index: ", end_index)
    print(f"sum: + {end_index} =", sum)


print(count)
