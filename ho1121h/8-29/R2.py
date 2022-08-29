# https://www.acmicpc.net/problem/3046
R1 ,S = map(int,input().split())
# S = 평균
# R2 는 평균 x r1,2의 갯수 에서  R1을 뺀 값
R2 = (S*2) - R1

print(R2)