
# https://www.acmicpc.net/problem/2292
import sys
input = sys.stdin.readline

A = int(input())

bee_house =1  # 1부터 시작함
count = 1 #1 부터 세면됨
## 벌집은 육각형

while A > bee_house: # 벌집갯수는 입력값을 넘어선 안된다. | ex) 13
    bee_house += 6*count # bee = 7 | 13 

    count += 1  # count = 2 | 3 // 2회전

print(count)
