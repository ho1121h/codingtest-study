import sys

word = []

N = int(sys.stdin.readline())

for i in range(N):
    M = sys.stdin.readline().strip()

    word.append(M)
set(word)
# sorted(word)
word.sort(key= lambda x: (len(x),x)) # 키설정
new_word = []
for i in word:
    if i not in new_word: # 중복제거
        new_word.append(i)
for i in new_word:
    print(i)