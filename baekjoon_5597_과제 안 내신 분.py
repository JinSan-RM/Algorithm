lst = [0] * 30
for i in range(28):
    j = int(input())
    lst[j - 1] = 1

for k in range(30):
    if lst[k] == 0:
        print(k + 1)
    
