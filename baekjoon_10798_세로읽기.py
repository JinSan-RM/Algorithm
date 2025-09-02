import sys

line = 5

temp = []

for i in range(line):
    lst = list(str(input()))
    temp.append(lst)

max_length = max(len(row) for row in temp)

for i in range(max_length):
    for j in range(len(temp)):        
        if i < len(temp[j]):
            print(temp[j][i], end='')
        
    
