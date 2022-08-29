a, i = map(int, input().split())
# https://www.acmicpc.net/problem/2914
#  평균 x 앨범에 수록된 곡수 = 멜로디 갯수
# 예제를 살펴보니 -1 하고 다시 1을 더하니 예제출력처럼 출력됨
# try => 성공
m = a*(i-1)
print(m+1)