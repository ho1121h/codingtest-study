n = int(input())

for i in range(n):
    s = input().lower()
    if s == s[::-1]:
        print("Yes")
    else:
        print("No")