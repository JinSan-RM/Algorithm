N = int(input())

cnt = N - 1
star = 1
for i in range(N):
    p = ''
    p += ' ' * cnt
    p += '*' * star
    print(p)
    cnt -= 1
    star += 2

cnt += 1
star -= 2
for j in range(N - 1):
    p = ''
    cnt += 1
    star -= 2
    p += ' ' * cnt
    p += '*' * star
    print(p)    
