## https://www.acmicpc.net/problem/2839
## 설탕 배달
## 입력문 | 조건문 | if,else
N = int(input())

봉지 = 0

while N >= 0:
    if N % 5 == 0 : # 5로 나뉘어 진다면  | ex )18 => 안됨 |
        봉지 += (N // 5) # N = 15 -> 봉지 = 3
        print(봉지)     # 4
        break 
    N -= 3 # 18-> 15
    봉지 += 1 # 5 의 배수가 될 때까지 설탕 -3 / 봉지 +1
else:
    print(-1) # 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.