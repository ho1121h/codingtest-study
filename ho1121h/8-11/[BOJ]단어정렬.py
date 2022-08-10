import sys

word = []

N = int(sys.stdin.readline())

for i in range(N):
    M = sys.stdin.readline().strip()

    word.append(M)
set(word)
# sorted(word)
word.sort(key= lambda x: (len(x),x))
for i in word:
    print(i)