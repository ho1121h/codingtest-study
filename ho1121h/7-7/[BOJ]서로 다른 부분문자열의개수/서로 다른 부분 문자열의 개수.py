S = input()
A = set()

for i in range(len(S)):
    for j in range(i,len(S)):
        N= S[i:j+1]
        A.add(N)
#print(A) # 중복이 제거된채로 출력됨
print(len(A))