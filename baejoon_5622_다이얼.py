S = str(input())

l_1 = ['A','B','C']
l_2 = ['D','E','F']
l_3 = ['G','H','I']
l_4 = ['J','K','L']
l_5 = ['M','N','O']
l_6 = ['P','Q','R','S']
l_7 = ['T','U','V']
l_8 = ['W','X','Y','Z']

res = 0
for i in S:
    if i in l_1:
        res += 3
    elif i in l_2:
        res += 4
    elif i in l_3:
        res += 5
    elif i in l_4:
        res += 6
    elif i in l_5:
        res += 7
    elif i in l_6:
        res += 8
    elif i in l_7:
        res += 9
    elif i in l_8:
        res += 10

print(res)
        
