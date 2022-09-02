# 잃어 버린 괄호 

# 그리디 알고리즘 : 정한 기준에 따라 가장 좋아 보인느 답을 선택하는 알고리즘

# https://www.acmicpc.net/problem/1541
# 입력 예 : 55-50+40
math = input().split("-") # 먼저 - 기준으로 스플릿을 함

math_plus = math[0].split("+") # 왼쪽값은 무조건 양수이기도하고, 만약 전부 + 연산인 경우 + 로 스플릿함

# print(math) : 55, 50+40
# print(math_1) :55

result = 0

for i in math_plus: #
    result += int(i)
# print(result)

for i in  math[1:]: 
    for j in i.split('+'): # i.split => '55' , '40'
        result -= int(j)
# 미리 result 에 더하고 빼면 최솟값이 구해진다
print(result)
