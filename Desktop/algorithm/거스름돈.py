N = int(input())
N = 1000 - N
array = [500, 100, 50, 10 ,5, 1]
count = 0
for money in array:
    count += N // money
    N %= money
print(count)
