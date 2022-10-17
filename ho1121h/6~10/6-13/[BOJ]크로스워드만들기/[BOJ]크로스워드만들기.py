A,B = map(str,input().split())
#주어진 2개의 단어

# 공유 글자 찾기 ,ex) MAMA TATA 가 입력됐을때
for i in range(len(A)):# 첫단어 하나씩 검토하면서 공유글자 매칭
    if A[i] in B: #0=false,1=True
        a = i #                      ex)a = 1
        b = B.index(A[i]) #          ex) 공유된글자 위치 기억 b=1
        break
# 반복하면서 점찍기(윗 블록에서 공유글자 찾은 위치에 첫단어가 출력됨)
for i in range(len(B)):
    if i == b: # i= 0,1,2,3 중 1이 True
        print(A) #MAMA 출력
    else:
        print("."*a+B[i]+"."*(len(A)-1-a))#공유단어 위치 빼고 전부 글자수만큼 점 찍기