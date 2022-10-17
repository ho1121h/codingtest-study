

n_l = [] # 빈리스트 생성
for i in range(10):# 10개의 수를 받기 위함

    a = int(input()) #정수 입력
    n = a % 42      # 42로 나눈 나머지
    n_l.append(n)   # 리스트에 추가후
print(len(set(n_l)))# 서로 다른 수의 합을 구하기위해 set으로 중복 제거