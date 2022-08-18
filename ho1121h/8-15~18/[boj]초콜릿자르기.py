##초콜릿 자르기
## n*m의 크기의 초콜릿을 1*m으로 자를려면... n-1번 자름 됨
## ex) 2*2= 4 -> 4-1
n, m = map(int,input().split())

print ((m*n)-1)