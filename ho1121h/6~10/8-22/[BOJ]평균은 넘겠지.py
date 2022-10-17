# https://www.acmicpc.net/problem/4344

import sys 
input = sys.stdin.readline
t = int(input())
for i in range(t): 
     
    a = input().split() #입력
    m= [] # 숫자 리스트
    for j in a:
        j =int(j)
        m.append(j)
    b = m.pop(0) # 학생수 제거
    avg = sum(m)/b # 평균 구함 
    avg_l= []   # 평균을 넘는 학생 수
    for k in m:
        if k > avg: # 평균이 넘으면
            avg_l.append(k) # 추가
    평균비율 = (len(avg_l)/b)*100 # 비율 계산
    print(f'{평균비율:.03f}%') # 소숫점 3자리까지 
    # print(f'{round(len(avg_l)/b)}%')