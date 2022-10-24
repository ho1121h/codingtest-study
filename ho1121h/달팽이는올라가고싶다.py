import sys

input = sys.stdin.readline
# A 낮에 A미터 올라감
# B 밤에 B미터 내려감
# V 높이가 V 미터임
# 시간 제한 : 0.15 초
A, B, V = map(int, input().split()) # ex : 2 1 5

X = (V-B) / (A-B)
# print(X)
if X == int(X): # 만약 정수 = 딱맞아 떨어지면 출력
    print(int(X))
else:
    print(int(X)+1) # 실수면 +1 해서 출력

print("한줄코드 : ",int((V-B-1) / (A-B) + 1)) # 3 / 1 = 3 +1 =4



