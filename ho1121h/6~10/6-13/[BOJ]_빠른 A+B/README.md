# 빠른 A+B
[문제링크](https://www.acmicpc.net/problem/15552)
- for 문이라 간단하게
```py
n = int(input())

for _ in range(n):
    A,B=map(int, input().split())
    print(A+B)
```
- 로 풀려고 하니 시간 초과 오류 발생
- 문제에 쓰여진대로 sys 사용하여 해결함
- 왜그런지 찾아보니, 인풋으로 입력받을때 여러줄로 받으면 시간초과가 일어난다고 한다. 그래서 sys.stdin.readline()을 사용한다고 한다.
```py
import sys

t = int(input())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)

```