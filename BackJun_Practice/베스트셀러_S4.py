# 오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때
# 가장 많이 팔린 책의 제목을 출력하는 프로그램 작성하기

# Input
# 첫째 줄 : 오늘 하루 동안 팔린 책의 개수 N (1000보다 작거나 같은 자연수)
# 둘째 줄 : N개의 줄에 책의 제목이 입력으로 들어온다 (길이는 50보다 작거나 같고 알파벳 소문잘로만)

# Output
# 첫째 줄에 가장 많이 팔린 책의 제목 출력
# 가장 많이 팔린 책이 여러 개일 경우 사전 순으로 가장 앞서는 제목 출력

import sys
input = sys.stdin.readline

N = int(input())

sell = {}

for i in range(N):
    name = input()
    if name not in sell:
        sell[name] = 1
    else:
        sell[name] += 1

max_value = max(sell.values())

best = []
for key, value in sell.items():
    if value == max_value:
        best.append(key)

best = sorted(best)
print(best[0])
