####
# https://www.acmicpc.net/problem/11557
####
t = int(input()) # 전체 테스트 케이스 수

for i in range(t):
    a = int(input()) # 테스트 케이스수 입력
    oh = [] # 

    for j in range(a):

        b = input().split() # Yonsei 10 -> ['Yonsei', '10']
        c = b[0] # 학교이름
        d = b[1] # 술 소비양
        oh.append([b,int(d)]) #1차원 리스트로 추가
    oh.sort(key= lambda x: x[1]) # 소비가 가장많은 학교의 이름 정렬 key는 술의 양으로 설정
    print(oh[-1][0][0]) # 3차원이 생성됐으므로 이렇게 접근