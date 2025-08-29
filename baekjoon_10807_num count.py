import sys
N = int(input())
lst = sys.stdin.readline().split()
v = int(input())

count = 0
for i in lst:
    if int(i) == int(v):
        count += 1

print(count)
