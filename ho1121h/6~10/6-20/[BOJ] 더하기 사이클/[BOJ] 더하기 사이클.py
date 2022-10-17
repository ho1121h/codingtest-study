''' 시간초과
n = input() #문자열로 받음
m = n
a = 0

while 1:
    if len(m) ==1  :# 1자리 수 라면
        m = '0' +m
    더하기 = str(int(m[0]) + int(m[1]))
    m = m[-1] + 더하기[-1]
    a +=1

    if m == n :
        print(a)
        break # 반복문 탈출'''


N =str(input())
RN = int(N)
N2 = None # 빈값

if int(N) <10 :
    N='0' + N
cnt  = 0

while N2!=RN:
    R=int(N[0])+int(N[1])
    R = str(R)
    if int(R) <10:
        R ='0' + R
    N = N[1]+R[1]
    N2 = int(N)
    cnt +=1
print(cnt)