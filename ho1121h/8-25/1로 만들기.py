# https://www.acmicpc.net/problem/1463
import sys
input = sys.stdin.readline

X = int(input())
# count = 0
# while X:
#     if X%3 == 0: 
        
d= [0] * (X + 1)

for i in range(2, X + 1):
    d[i] = d[i - 1] + 1 # 2와 3으로 나누어지지 않을 경우 무조건 1을 빼기때문에 사용
    
    if i % 3 ==0: # 3으로 나누어 떨어지면 사용
        d[i] = min(d[i], d[i //3] + 1)
    if i % 2 ==0: # 2로 나누어 떨어지면 사용
        d[i] = min(d[i], d[i //2] + 1)

print(d[X])# min 으로 저장되니... 최소 연산 횟수가 출력됨