N = 20

total_score = 0
GPA = 0.0
for i in range(N):
    subject, score, grade = input().split()
    score = float(score)
    if grade != "P":
        total_score += score
    #print(f"{i} : {subject}, {score}, {grade}")
    
    if grade == 'A+':
        score *= 4.5
    elif grade == 'A0':
        score *= 4.0
    elif grade == 'B+':
        score *= 3.5
    elif grade == 'B0':
        score *= 3.0
    elif grade == 'C+':
        score *= 2.5
    elif grade == 'C0':
        score *= 2.0
    elif grade == 'D+':
        score *= 1.5
    elif grade == 'D0':
        score *= 1.0
    elif grade == 'F':
        score *= 0.0
    else:
        score = 0
    
    
    if grade == "P":
        #print("Grade is P pass")
        pass
    else:
        #print(i, "total score : ", total_score)
        GPA += score
        #print(i, "GPA", GPA)
                

#print("total score : ", total_score)
#print("GPA", GPA)
result = float(GPA / total_score)
print(f"{result:.6f}")
