N = int(input())


result = 0

for i in range(N):
    word = list(str(input()))
    res = []
    b_word = None
    is_group_word = True
    for j in range(len(word)):
        if j == 0:
            b_word = word[j]
        else:
            if word[j] != b_word:
                res.append(b_word)
                b_word = word[j]
                if word[j] in res:
                    is_group_word = False
                    break
    if is_group_word:
        result += 1
        

print(result)
        
                
                
        

