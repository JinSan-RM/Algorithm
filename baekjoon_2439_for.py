N = int(input())
res = 0
star = "*"
blank = " "
rev_res = N - 1
for i in range(1, N+1):
    res = res + 1
    print(blank * rev_res, end='')
    print(res * star)
    rev_res = rev_res - 1
