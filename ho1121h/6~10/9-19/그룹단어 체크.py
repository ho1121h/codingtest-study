#https://www.acmicpc.net/problem/1316
# 
N = int(input())


# 연속되지 않은 곳에서 문자가 다시 나타날 경우 그 문자열은 그룹 단어가 아니라는 것을 조건으로 인식


chk = N # ex =3
# 아닌 단어 확인하면 -1 씩함

for _ in range(N):

    str = input() # happy

    for i in range(0,len(str)-1):
        if str[i] == str[i+1]:
            pass
        elif str[i] in str[i+1:]:
            chk -= 1
            break

print(chk)