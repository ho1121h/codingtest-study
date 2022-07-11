'''import  sys
from queue import Queue 

N = int(sys.stdin.readline()) # 반복횟수 입력
que = Queue()
for _ in range(N): 
    M = sys.stdin.readline().split() # 명령어 입력
    o = M[0] #명령어는 무조건 앞에 옴

    if o == 'push': 
        value = M[1] # 밸류값
        que.put(value) # 큐에 추가

    elif o == 'pop':
        if que.qsize() == 0:
            print(-1)
        else:
            print(que.get())

    elif o == 'size':
        print(que.qsize())

    elif o == 'empty':
        if que.empty() =='True':
            print(1)
        elif que.empty() =='False':
            print(0)
    elif o == 'front': # 제일 앞 숫자 출력
        if que.qsize() == 0 :
            print(-1)
        else:
            q_f= que
            print(q_f.get())
    elif o == 'back': # 제일 뒤 숫자 출력
        if que.qsize() ==0 :
            print(-1)
        else:
            q_b=que
            print(q_b.get())

print(que.qsize())'''

from sys import stdin
input()
s, com= [], stdin.readlines()
cnt = 0
for x in com:
    c = x.split()
    if c[0] == "push":
        s.append(c[1])
    elif c[0] == 'pop':
        if len(s) > cnt:
            print(s[cnt])
            cnt += 1
        else: print(-1)
    elif c[0] == 'size':
        print(len(s)-cnt)
    elif c[0] == 'empty':
        if len(s) == cnt :
            print(1)
            cnt = 0
            s = []
        else: print(0)
    elif c[0] == 'front':
        if len(s) > cnt: print(s[cnt])
        else: print(-1)
    elif c[0] == 'back':
        if len(s) > cnt: print(s[-1])
        else: print(-1)