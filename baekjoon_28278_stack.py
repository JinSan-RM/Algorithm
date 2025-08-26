import sys
N = int(sys.stdin.readline()) # 들어오는 명령의 수 를 N으로 받음

stack = [] # 스택을 관리할 리스트

for i in range(N): # 명령의 수 만큼 반복
    p = sys.stdin.readline().split() # 들어온 명령의 줄들을 나눠서 리스트로
    
    if int(p[0]) == 1: # 1 X: 정수 X를 스택에 넣는다.
        num = int(p[1])
        stack.append(int(p[1]))
        
    elif int(p[0]) == 2: # 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
        
        if len(stack) > 0:
            num = stack.pop()
            print(num)
            
        else:
            print("-1")
            
    elif int(p[0]) == 3: # 3: 스택에 들어있는 정수의 개수를 출력한다.
        print(len(stack))

    elif int(p[0]) == 4: # 4: 스택이 비어있으면 1, 아니면 0을 출력한다
        
        if len(stack) == 0:
            print("1")

        else:
            print("0")

    elif int(p[0]) == 5: # 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
        if len(stack) != 0:
            num = stack[-1]
            print(num)

        else:
            print("-1")


